import os
import numpy as np
import pandas as pd

def summary_data_withings(subject_id, data_path):
   """
   Process and summarize Withings sleep data for a given subject.
   
   Args:
       subject_id: Subject identifier
       data_path: Base path to the data directory
       
   Returns:
       DataFrame with subject ID, date, and total recording time (TRT) for each day
   """
   # Initialize empty DataFrame to store processed data
   df_sleep_all = pd.DataFrame()
   
   # Construct path to subject's Withings directory
   withings_dir = f'{data_path}{subject_id}/withings/'
   
   # Iterate through files in the directory
   for filename in sorted(os.listdir(withings_dir)):
       
       # Process only files starting with 'withings_report'
       if filename.startswith('withings_report'):
           # Read individual CSV file
           df_sleep = pd.read_csv(f'{withings_dir}{filename}')
           
           # Calculate Total Recording Time (TRT) in minutes by summing sleep stages
           df_sleep['TRT'] = df_sleep[['light (s)', 'deep (s)', 'awake (s)']].sum(axis=1)/60
           
           # Keep only records with more than 3 hours (180 minutes) of data
           df_sleep = df_sleep.loc[df_sleep['TRT'] > 180]
           
           if len(df_sleep) > 1:
               # Extract date from 'to' timestamp (first 19 characters)
               df_sleep['date'] = df_sleep['to'].str[:19]
               
               # Create final DataFrame with processed data
               df_sleep_all['date'] = pd.to_datetime(df_sleep['to'].str[:19]).dt.date
               df_sleep_all['subject'] = subject_id
               df_sleep_all['TRT'] = df_sleep['TRT']
               
               return df_sleep_all