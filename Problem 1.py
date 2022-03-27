from zipfile import ZipFile
from pathlib import Path
import os

file_name = "kaggle-survey.zip"

# find the path of this directory
directory = Path("Kaggle")
# make a new directory called "Kaggle"
directory.mkdir()

# extract all files in the zip files and store them to Klaggle
with ZipFile(file_name, 'r') as zip:
    zip.printdir()
    print('Extracting all the files now!! Yay :D!')
    zip.extractall('')
    print('Finish extracting the mother file! Yay! :D!')
    files = os.listdir(Path('kaggle-survey'))
    for file in files:
        if file.endswith('.zip'):
            with ZipFile(Path('kaggle-survey') / file, 'r') as zip:
                zip.extractall(directory)
                print('Finish extracting the children files! Yay! :D!')
    
