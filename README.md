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

  
# Simons Sleep Project (SSP) Manuscript

This Github repository contains data and code that was used to generate all results and figures in the pre-print "Simons Sleep Project (SSP): An open science resource for accelerating scalable digital health research in autism and other psychiatric conditions", which is availabe on BioArxiv at (link). The SSP is a comprehensive open-science resource with raw and processed data from Dreem3 EEG headbands, multi-sensor EmbracePlus smartwatches, and Withings Sleep mats, as well as parent questionnaires and daily sleep diaries. Data includes recordings from >3600 days/nights of 102 adolescents (10-17 years old) with idiopathic autism and 98 of their non-autistic siblings. All raw and processed data is freely available through the Simons Foundation Autism Research Initiative (SFARI). For further details about the project and the data please read the paper.

## SSP data includes:

1. **Dreem3 EEG Headband (Beacon Inc.) recordings**
   - Electroencephalogram (EEG) from 5 channels
   - Accelerometer data
   - Positiongram data

2. **EmbracePlus Smartwatch (Empatica Inc.) recordings**
     - Accelerometer data
     - Electrodermal activity
     - Skin temperature
     - Blood volume pulse

3. **Withings Sleep Mat (under the mattress) recordings**
   - Respiration
   - Heart rate and variability
   - Pressure changes (movements)

4. **Daily sleep diary reports**
    - Parent ratings of child mood and behavior
    - Parent reported sleep measures
    - Daily medication intake
 
5. **Parent questionnaires at baseline**
   - Vineland Adaptive Behaviors Scale
   - Child Behavior Check List
   - Social Responsiveness Scale 2
   - Repetitive Behaviors Scale - Revised
   - Child Sleep Habits Questionnaire
   - Family Inventory Sleep Habits
   - Aberrant Behaviors Checklist
   - Sensory Profile 2
   - Medical Update Questionnaire
  
## Repository Contents

This repository provides Python notebooks and scripts for:
1. Basic data exploration and visualization of available sleep metrics from the 3 wearable devices.
2. Comparison of questionnaire and sleep diary data across autism and sibling groups.
3. Comparison of device sleep measures across autism and sibling groups.
4. Examining relationships between objective sleep measures from the devices and subjective sleep measures from questionnaires.

Python notebooks are organized according to the analyses presented in the paper with each notebook corresponding to analyses presented in a specific figure.

#### Figure 1: Data overview
- Presents the availability of different data types and their overlap

#### Figure 2: Comparison of questionnaire data across groups
- Perform mixed linear model analysis per questionnaire to identify differences across autism and sibling groups
- Present findings using box plot graphs per questionnaire. 

#### Figure 3: Example of 24-hour Data 
- Presents multitude of harmonized data streams available for a single subject during a 24 hour period including:
  - EEG recording from Dreem3
  - Multiple sensor data from EmbracePlus
  - Sleep mat measurements from Withings
  
#### Figure 4: Device Agreement Analysis
- Calculates Concordance Correlation Coefficients (CCCs) for multiple sleep measures across devices, sleep diary, and CSHQ.
  - Sleep Onset
  - Final Awakening
  - Wake After Sleep Onset
  - Total Sleep Time

#### Figure 5: Comparison of device sleep measures across groups
- Compares objective sleep metrics between autistic children and their siblings including:
  - Total Sleep Time (TST)
  - Wake After Sleep Onset (WASO)
  - Includes statistical analyses and visualizations

#### Figure 6: Exploring Sleep-Behavior Relationships
- Analyzes relationships between objectively defined sleep disturbances (WASO and SOL) and behavioral symptoms as reported by parents
- Includes sleep measures extracted from raw EEG recordings using Yasa sleep staging algorithm
- Provides detailed statistical analyses and visualizations

Each notebook is self-contained and includes:
- Data loading and preprocessing steps
- Detailed analysis procedures
- Code for generating visualizations
- Statistical analyses where applicable
- Explanatory markdown cells documenting each step

Users can follow these notebooks to:
1. Understand the analysis methodology
2. Reproduce the results
3. Extend the analyses for their own research questions
4. Learn about sleep research data analysis techniques

**Important Note:** The visualizations and analyses in this repository are conducted on summarized sleep metrics (e.g., total sleep time, wake after sleep onset, sleep onset latency) and demographic data. The raw sensor data (EEG signals, accelerometer data, etc.) are not included in this repository but are available in the complete dataset on SFARI Base.
