import os
import numpy as np
import pandas as pd

def summary_data_dreem(subject_id, data_path):
    """
    Process and summarize sleep data from Dreem headband files for a given subject.
    
    Args:
        subject_id: Subject identifier
        data_path: Base path to the data directory
    """
    # Construct path to subject's dreem reports directory
    dreem_dir = f'{data_path}{subject_id}/dreem/dreem_reports/'
       
    # Initialize empty DataFrame to store all sleep data
    df_sleep_all = pd.DataFrame()
    
    # Iterate through each CSV file in the directory
    for filename in sorted(os.listdir(dreem_dir)):
        if filename.startswith('dream_report'):
            # Read individual sleep report CSV
            df_sleep = pd.read_csv(f'{dreem_dir}{filename}')
            
            # Reshape data using pivot - transforms from long to wide format
            # Groups data by STUDYID, SUBJID, REC_DATE_TIME, OFFHEAD and spreads ENDPOINT values
            df_pivot = df_sleep.pivot(
                index=['STUDYID', 'SUBJID', 'REC_DATE_TIME', 'OFFHEAD'],
                columns='ENDPOINT',
                values=['VALUE', 'QI_INDEX']
            )
            
            # Clean up column names after pivot
            # If column had 'QI_INDEX', name becomes 'ENDPOINT_QI_INDEX'
            # If column had 'VALUE', name becomes just 'ENDPOINT'
            df_pivot.columns = [f'{level2}_{level1}' if level1 == 'QI_INDEX' else f'{level2}' 
                              for level1, level2 in df_pivot.columns]
            
            # Convert pivot table back to regular DataFrame
            df_sleep = df_pivot.reset_index()
            
            # Append to main DataFrame
            df_sleep_all = pd.concat([df_sleep_all, df_sleep])

    # Process timestamps if REC_DATE_TIME column exists
    if 'REC_DATE_TIME' in df_sleep_all.columns:
        # Extract datetime string without timezone (first 19 characters)
        df_sleep_all['start_rec'] = df_sleep_all['REC_DATE_TIME'].str[:19]
        # Convert string to datetime
        df_sleep_all['start_rec'] = pd.to_datetime(df_sleep_all['start_rec'])
        
        # Remove rows with missing start_rec
        df_sleep_all.dropna(subset='start_rec', inplace=True)

        if len(df_sleep_all) > 1:
            # Remove timezone information from start_rec
            df_sleep_all['start_rec'] = df_sleep_all['start_rec'].dt.tz_localize(None)
            
            # Remove original REC_DATE_TIME column
            df_sleep_all.drop('REC_DATE_TIME', axis=1, inplace=True)
            
            # Convert Total Recording Time from minutes to hours
            df_sleep_all['TRT'] = df_sleep_all['TRT']/60
            
            # Calculate Sleep Onset time (start_rec + Sleep Onset Latency)
            df_sleep_all['SO'] = df_sleep_all['start_rec'] + pd.to_timedelta(df_sleep_all['SOL'], unit='m')
            
            # Calculate Final Awakening time (start_rec + Total Sleep Time + Wake After Sleep Onset)
            df_sleep_all['FA'] = df_sleep_all['start_rec'] + pd.to_timedelta(df_sleep_all['TST'], unit='m') + pd.to_timedelta(df_sleep_all['WASO'], unit='m')
            
            # Extract date from Final Awakening time
            df_sleep_all['date'] = pd.to_datetime(df_sleep_all['FA']).dt.date
            
            # Copy QUAL column to quality
            df_sleep_all['quality'] = df_sleep_all['QUAL']
            df_sleep_all['subject'] = subject_id
            
            # Reorder columns - put key metrics first
            reorder = ['subject','date','TRT', 'TST', 'WASO', 'SO', 'FA','quality'] + [col for col in df_sleep_all.columns 
                      if col not in ['subject','date','TRT', 'TST', 'WASO', 'SO', 'FA', 'quality']]
            df_sleep_all = df_sleep_all[reorder]
            
            return df_sleep_all