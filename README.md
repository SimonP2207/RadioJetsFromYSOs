# Radio Jets from Young Stellar Objects
The primary purpose of this repository is to store data, images and scripts pertaining to publications studying the radio emission associated with the ionised jets of young stellar objects.

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
│   │   │   └───...             # A total of XX C-band .fits images are present in this directory
│   │   └───Q-band/             # Directory for 44GHz images
│   │       ├───G***.****.fits  # Q-band image for G***.***.fits where ***.**** is the galactic l-coordinate
│   │       └───...             # A total of XX Q-band .fits images are present in this directory
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
    └───(empty)                 # In development as of 20/08/2020
```
