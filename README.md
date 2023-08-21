# What is this repository about
When using Polar smart watches, the Polar Flow service can output single files in .gpx format. However, if one wants to output ALL data, it comes in a .zip file that contains everything json format. I couldn't find a script that formats them to .gpx, so I made one. Not much time was devoted to this, and I won't update it, but maybe this helps somebody.
Implemented on Python version 3.11.3, on 64-bit Windows 10.


## First, fire up your cmd.
Change to your directory (replace *your directory here* below) and create virtual environment.
```
cd *your directory here*
python -m venv venv
.\venv\Scripts\activate
```

## Install requirements
```
pip install -r requirements.txt
```

## Modify the DIRECTORY_IN (path to your Polar data export folder) and DIRECTORY_OUT (path to where you want converted files to appear in) in the .py file.

## Run script
```
python polar_to_gpx_converter_hack.py
```

## After this, install a GPS visualization software.
Recommendation: Viking, see links:
https://sourceforge.net/projects/viking/
https://viking-gps.github.io/

## Instructions for Viking:
File > Open > *select all tracks you want to visualize*
Then, right click Top Layer > New Layer > Map > *select map*
To see notes, click on a training session > Properties > Metadata.
