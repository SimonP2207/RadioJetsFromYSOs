import os
import numpy as np
import pandas as pd
import datetime as dt
import radiopy as rp

# ############################################################################ #
# ############################################################################ #
# ############################################################################ #
ul_sigma = 3.  # Upper limit multiples of the noise to use
# ############################################################################ #

# Establish paths to all data tables
table_dcy = os.sep.join([os.path.dirname(os.path.realpath(__file__)),
                         'tables'])
cband_csv = 'cband.csv'
qband_csv = 'qband.csv'
ancil_csv = 'ancillary.csv'

# Import separate data files into pandas.DataFrame objects
df_c = pd.read_csv(os.sep.join([table_dcy, cband_csv]), na_values=['-'])
df_q = pd.read_csv(os.sep.join([table_dcy, qband_csv]), na_values=['-'])
df_a = pd.read_csv(os.sep.join([table_dcy, ancil_csv]), na_values=['-'])

# Add frequency column to dataframes of radio data
df_c['Freq'] = 5.8e9
df_q['Freq'] = 44e9

# Add ancillary data to each radio dataframe
df_c = pd.concat([df_c, df_a], axis=1)
df_q = pd.concat([df_q, df_a], axis=1)

# Find entries in Q-band table where no Q-band data was observed or out of FOV
no_obs_q_mask = []
for i, r in df_q.iterrows():
    obsdate = r.Obs_Date
    rms = r.RMS

    try:
        od_isnan = np.isnan(obsdate)
    except TypeError:
        od_isnan = False

    try:
        rms_isnan = np.isnan(rms)
    except TypeError:
        rms_isnan = False

    no_obs_q_mask.append(od_isnan | rms_isnan)

# Drop Q-band rows where no Q-band data was observed, or out of FOV
df_q.drop(df_q.index[no_obs_q_mask], inplace=True)

# Concatenate C and Q-band dataframes into one dataframe
dataframe = pd.concat([df_c, df_q])

# Use radiopy's Flux and Size classes for relevant columns
fluxes, fluxes_3sig, sizes = [], [], []
for i, r in dataframe.iterrows():
    # Convert observation dates (str) to datetime.datetime instances
    tobs = r.Obs_Date.split(';')
    obs_date = [dt.datetime.strptime(_, '%d/%m/%Y')
                for _ in r.Obs_Date.split(';')]
    if len(obs_date) == 1:
        obs_date = obs_date[0]
    else:
        obs_date = abs(obs_date[0] - obs_date[1]) / 2 + \
                   obs_date[0] if obs_date[0] < obs_date[1] else obs_date[1]

    # Convert imfit-flux columns into radiopy.dataclasses.Flux instances
    f, fe, nu, ul = r.Flux, r.Flux_err, r.Freq, False

    if np.isnan(f):
        ul = True
        f = ul_sigma * r.RMS
        fe = r.RMS

    fluxes.append(rp.dataclasses.Flux(f, fe, nu, telescope='VLA', up_lim=ul,
                                      obs_date=obs_date))

    # Convert 3-sigma flux columns into radiopy.dataclasses.Flux instances
    f3s, fe3s, ul3s = r.Flux_3sig, r.Flux_3sig_err, False

    if np.isnan(f3s):
        ul = True
        f3s = ul_sigma * r.RMS
        fe3s = r.RMS

    fluxes_3sig.append(rp.dataclasses.Flux(f3s, fe3s, nu, telescope='VLA',
                                           up_lim=ul, obs_date=obs_date))

    # Convert deconvolved-size columns into radiopy.dataclasses.Size instances
    maj, maj_e = r.Theta_maj, r.Theta_maj_err
    min, min_e = r.Theta_min, r.Theta_min_err
    pa, pa_e = r.Theta_pa, r.Theta_pa_err
    ul = False

    if type(maj) is str:
        maj = float(maj.strip('<'))
        min = float(min.strip('<'))
        ul = True

    sizes.append(rp.dataclasses.Size(maj, maj_e, min, min_e, pa, pa_e, nu,
                                     up_lim=ul, obs_date=obs_date))

# Set relevant dataframe columns to list of instances of radiopy classes
dataframe['Flux'] = fluxes
dataframe['Flux_3sig'] = fluxes_3sig
dataframe['Size'] = sizes

# Drop deprecated columns
dataframe.drop(['Flux_err', 'N_cells_3sig', 'Area_3sig_as^2', 'Area_3sig_sr',
                'Sum_Flux_3sig', 'Flux_3sig_err', 'Theta_maj','Theta_maj_err',
                'Theta_min', 'Theta_min_err', 'Theta_pa', 'Theta_pa_err'],
               axis=1, inplace=True)
