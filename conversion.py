
import pandas as pd
import numpy as np

# Read the file into a DataFrame: df
#df = pd.read_csv('HealthApp.log', sep='|', engine='python', names=['timestamp', 'code', 'message'])

file = open('HealthApp.log', 'r')
lines = file.read()
lines = lines.split('\n')
filt_lines = []
for f in lines:
    filt_lines.append(f)
array = [l.split('|') for l in filt_lines]
log_df = pd.DataFrame(array)
log_df.to_csv('HealthApp.csv')

