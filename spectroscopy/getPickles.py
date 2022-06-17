'''
GOAL: download the pickles spectra to a subdirectory directory



'''

import os
import wget

if not os.path.exists("Pickles"):
    os.mkdir("Pickles")
os.chdir("Pickles")

nmax = 132 # use this value to get all spectra
nmax = 46 # use this value to get MS stars only
for i in range(1,46):
    url = f"https://archive.stsci.edu/hlsps/reference-atlases/cdbs/grid/pickles/dat_uvi/pickles_{i}.fits"
    f = wget.download(url)
    print(f)
    

