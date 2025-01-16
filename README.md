<div style="display: flex; justify-content: space-between; align-items: center;">
  <img src="./images/Simons_logo.png" width="300"/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

  <img src="./images/BGU_logo.png" width="300">
</div>

  
# Simons Sleep Project (SSP) Analysis Tools

## Overview
The Simons Sleep Project (SSP) is a comprehensive open resource designed to accelerate sleep research in autism and other neurodevelopmental conditions. The project contains data collected from 102 autistic adolescents and 98 of their non-autistic siblings, offering unique insights into sleep patterns and their relationship with neurodevelopmental symptoms.

## Dataset Description

### Multi-Device Recording System
The SSP utilizes three complementary devices selected for their ability to record and save raw sensor-level data:

1. **Dreem3 EEG Headband (Beacon Inc.)**
   - Electroencephalogram (EEG) recordings
   - Head movement data
   - Enables direct identification of sleep stages and sleep architecture

2. **EmbracePlus Smartwatch (Empatica Inc.)**
   - Multi-sensor recordings including:
     - Accelerometer data
     - Electrodermal activity
     - Skin temperature
     - Blood volume pulse

3. **Withings Sleep Mat**
   - Non-contact sleep monitoring
   - Breathing patterns
   - Movement detection
   - Heart rate

### Additional Data Sources
- Daily sleep diary entries
- Nine parent questionnaires completed at baseline
- Comprehensive demographic and clinical information

## Repository Contents

This repository provides Python notebooks and scripts for:
1. Basic data exploration and visualization of summarized sleep metrics
2. Demographics analysis of the study population
3. Assessment of recording coverage across devices

## Sample Characteristics
- Age range: 10-17 years
- Balanced sex distribution
- Includes siblings living in the same household
- Documentation of ADHD comorbidity
- Over 3,600 nights of recordings


## Objectives 

This repository provides a comprehensive recreation of the analyses presented in the paper "Simons Sleep Project (SSP): An open science resource for accelerating scalable digital health research in autism and other psychiatric conditions." The analyses are organized into separate notebooks, each corresponding to a specific figure from the paper, making it easy to understand and reproduce the results step by step.

### Analysis Notebooks

#### Figure 1: Demographics Analysis
- `figure1_demographics.ipynb`
- Explores and visualizes the demographic characteristics of the study sample
- Includes age distribution, sex ratios, and other key population metrics

#### Figure 2: Behavioral Symptoms Comparison
- `figure2_behavioral_symptoms.ipynb`
- Analyzes parent-reported behavioral symptoms and abilities
- Compares metrics between autistic children and their siblings
- Includes statistical analyses and visualization of key differences

#### Figure 3: Multi-Modal Data Visualization
- `figure3_data_gallery.ipynb`
- Provides a 24-hour visualization gallery from a single subject
- Demonstrates the various types of data collected:
  - EEG recordings from Dreem3
  - Smartwatch sensor data from EmbracePlus
  - Sleep mat measurements from Withings
  
#### Figure 4: Device Agreement Analysis
- `figure4_device_agreement.ipynb`
- Calculates Concordance Correlation Coefficients (CCCs)
- Analyzes agreement between devices, sleep diary, and CSHQ for:
  - Sleep Onset
  - Final Awakening
  - Wake After Sleep Onset
  - Total Sleep Time

#### Figure 5: Sleep Patterns Comparison
- `figure5_sleep_patterns.ipynb`
- Compares key sleep metrics between autistic children and siblings:
  - Total Sleep Time (TST)
  - Wake After Sleep Onset (WASO)
- Includes statistical analyses and visualizations

#### Figure 6: Sleep-Behavior Relationships
- `figure6_sleep_behavior.ipynb`
- Analyzes relationships between sleep disturbances and behavioral symptoms
- Explores correlations with parent-reported questionnaire data
- Provides detailed statistical analyses and visualizations

Each notebook is self-contained and includes:
- Data loading and preprocessing steps
- Detailed analysis procedures
- Code for generating visualizations
- Statistical analyses where applicable
- Explanatory markdown cells documenting each step

Users can follow these notebooks to:
1. Understand the analysis methodology
2. Reproduce the paper's findings
3. Extend the analyses for their own research questions
4. Learn about sleep research data analysis techniques

**Important Note:** The visualizations and analyses in this repository are conducted on summarized sleep metrics (e.g., total sleep time, wake after sleep onset, sleep onset latency) and demographic data. The raw sensor data (EEG signals, accelerometer data, etc.) are not included in these basic visualization tools but are available in the complete dataset.
