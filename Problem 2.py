import pandas as pd
from pathlib import Path
import os

# open survey 2020 and store it to a dataframe
file2020 = Path('Kaggle') / 'kaggle_survey_2020_responses.csv'
df = pd.read_csv(file2020)
print(df)
