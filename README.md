# STUDY 0: Study on possible palette to story correlations in anime trailers

## Assumptions
- There is a correlation between color palette and genre of anime

## Gathering of Dataset
### Trailer
Collect trailers of at least 1000 different anime. 
Several seasons of the same major anime story line are considered different anime.

### Meta Information
- Title
- Feature
	- Release date
	- Length of trailer in frames
	- Genre tags
	- AniDB tags
	- AniList tags
	- Rating

### Scope
- Color anime, no black and white renderings
- No anime older than 2000

## Random Split of Dataset
The dataset will be randomly split into a teaching set and a verification set.
The teaching set will be used to teach one or more classificators which will have to be defined. The verification set will be used to verify or falsify assumptions made based on the previously tought features.

## Processing
### Meta Information
Tags describing the same feature characteristic but differing in tag representation (eg. "Mecha", "mecha", "Mecha-Anime") will be consolidated.
Tags describing more than one feature characteristic will be split up (eg. "Space/Mecha" will be "Space" and "Mecha").
### Data processing
Each frame of a given trailer will be dumped to an individual image.
Images will then be analyzed based on color histograms using a fixed bin width across the whole study to determine by-frame color distribution.
The study will focus on the HSV color space.
We'll follow the basic methods outlined in [Oranges and Blues](http://boxofficequant.com/oranges-and-blues/) and adapt them to anime.

# Installation Instructions
This study needs python3 and virtualenvwrapper.

1. Create a virtualenv: `mkvirtualenv --no-site-packages --python=$(which python3) studyzero`
1. Activate this environment: `workon studyzero`
1. Then `cd` to where the code lies and run `pip install -r requirements.txt`
    * You can also `setvirtualenvproject` here to set the current directory as project directory for the virtualenv. 'workon studyzero' will then automatically change into this directory.
1. Download 'anime-titles.xml.gz' from anidb. (I am not linking to this file so they won't get hammered needlessly)
1. Run `python converttodict.py`; it should print a long list of main titles and the number of processed main titles at the end.
