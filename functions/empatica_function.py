import os
import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta

def summary_data_empatica(subject_id, data_path):
   """
   Process and summarize Empatica device data for a given subject.
   
   Args:
       subject_id: Subject identifier 
       data_path: Base path to the data directory
       
   Returns:
       DataFrame with subject ID, date, and total recording time (TRT) for each day
   """
   # Initialize empty list to store processed data
   df_sleep_all = []
   
   # Construct path to subject's Empatica summarized data directory
   empatica_dir = f'{data_path}{subject_id}/empatica/summarized_data/'
   
   # Iterate through files in the directory
   for filename in sorted(os.listdir(empatica_dir)):
       
       # Process only files starting with 'empatica_measures'
       if filename.startswith('empatica_measures'):
           # Read individual CSV file
           df_sleep = pd.read_csv(f'{empatica_dir}{filename}')
           
           # Check if there's at least 6 hours of activity data (360 minutes)
           # by counting non-null activity_counts entries
           if len(df_sleep.dropna(subset='activity_counts')) > 360:
               # Get total minutes recorded
               minutes_recoreded = len(df_sleep.dropna(subset='activity_counts'))
               
               # Extract date from ISO timestamp (first 19 characters)
               df_sleep['date'] = df_sleep['timestamp_iso'].str[:19]
               
               # Get the date of the final aawakening of the recording (taking first entry's date and adding 1 day)
               date = pd.to_datetime(df_sleep['date']).dt.date[0] + timedelta(days=1)
               
               # Append summary data: [subject_id, date, total_minutes]
               df_sleep_all.append([subject_id, date, minutes_recoreded])
   
   # Convert list of summaries to DataFrame with labeled columns            
   return pd.DataFrame(df_sleep_all, columns=['subject', 'date', 'TRT'])