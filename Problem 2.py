import pandas as pd
from pathlib import Path
import os



#  **** Step 1 output every csv file to dataframe **** #
# open survey 2020 and store it to a dataframe
file2020 = Path('Kaggle') / 'kaggle_survey_2020_responses.csv'
df0 = pd.read_csv(file2020)


# Step 2 Cancat 2019 dataframe together

# Step 3 Compare questions in each dataframe and change them to be the same questions

# Step 4 Compare three data frame, save the intersection columns(questions)