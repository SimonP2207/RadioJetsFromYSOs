# Radio Jets from Young Stellar Objects
The primary purpose of this repository is to store data, images and scripts pertaining to publications studying the radio emission associated with the ionised jets of young stellar objects.

## Summary
This repository contains the data for the following publications:
- [Purser, S. J. D., Lumsden, S. L., Hoare, M. G., et al. 2016, MNRAS, 460, 1039](https://ui.adsabs.harvard.edu/abs/2016MNRAS.460.1039P/abstract) (corresponding directory in the file structure below is `ATCASurveyPurser2016`)
- [Purser, S. J. D., Lumsden, S. L., Hoare, M. G., Kurtz, S., 2021, MNRAS, 504, 338](https://ui.adsabs.harvard.edu/abs/2021MNRAS.504..338P/abstract) (corresponding directory in the file structure below is `VLASurveyPurser2020`)

For each of those works listed above, image .fits files for each object at each observed frequency, .csv/.fits tables for results and associated scripts for ease of data import are included. Should you use any of the data below, please cite the relevant work above. For a full description of the repository's directory tree, please see below.

## Contents
Below is the directory tree for this repository with folder/file descriptions as comments:
```perl
RadioJetsFromYSOs/              # Respository's parent directory
├───radiopy/                    # Git submodule containing the radiopy repo for use in data.py below
|   └───...                     # More details can be found on the radiopy repo or in the README
├───VLASurveyPurser2020/        # Directory containing material from Purser et al. (2020)
│   ├───fits/                   # Contains all clean images in .fits format
│   │   ├───C-band/             # Directory for 5.8GHz images
│   │   │   ├───G***.****.fits  # C-band image for G***.***.fits where ***.**** is the galactic l-coordinate
│   │   │   └───...             # A total of 64 C-band .fits images are present in this directory
│   │   └───Q-band/             # Directory for 44GHz images
│   │       ├───G***.****.fits  # Q-band image for G***.***.fits where ***.**** is the galactic l-coordinate
│   │       └───...             # A total of 43 Q-band .fits images are present in this directory
│   └───results/                # Contains image analysis results and associated scripts
│       ├───data.py             # Python script which imports results as pandas.DataFrame instance
│       └───tables/             # Contains all image analysis results in various table formats
│           ├───cband.csv       # Table of C-band results in .csv format
│           ├───cband.fits      # Table of C-band results in .fits table format
│           ├───qband.csv       # Table of Q-band results in .csv format
│           ├───qband.fits      # Table of Q-band results in .fits table format
│           ├───ancillary.csv   # Table of supporting data in .csv format
│           └───ancillary.fits  # Table of supporting data in .fits table format
└───ATCASurveyPurser2016/       # Directory containing material from Purser et al. (2016)
    ├───fits/                   # Contains all clean images in .fits format
    │   ├───5500/               # Directory for 5.5GHz images
    │   │   ├───G***.****.fits  # 5.5GHz image for G***.***.fits where ***.**** is the galactic l-coordinate
    │   │   └───...             # A total of 34 5.5GHz .fits images are present in this directory
    │   ├───9000/               # Directory for 9GHz images
    │   │   ├───G***.****.fits  # 9GHz image for G***.***.fits where ***.**** is the galactic l-coordinate
    │   │   └───...             # A total of 34 9GHz .fits images are present in this directory
    │   ├───17000/              # Directory for 17GHz images
    │   │   ├───G***.****.fits  # 17GHz image for G***.***.fits where ***.**** is the galactic l-coordinate
    │   │   └───...             # A total of 40 17GHz .fits images are present in this directory
    │   └───22800/              # Directory for 22.8GHz images
    │       ├───G***.****.fits  # 22.8GHz image for G***.***.fits where ***.**** is the galactic l-coordinate
    │       └───...             # A total of 40 22.8GHz .fits images are present in this directory
    └───results/                # Contains image analysis results and associated scripts
        └───(empty)             # In development as of 13/05/2022
```
