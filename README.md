# Athlete Performance Analysis

This Python script analyzes athlete performance data retrieved from an Excel file. It performs various operations such as data cleaning, statistical calculations, and visualizations using Pandas and Matplotlib.

## Code Explanation

### Data Loading and Cleaning

The script reads data from an Excel file (`coureur1.xls`) containing columns for time, altitude, heart rate, and speed. It then removes rows containing NaN values to ensure data quality.

### Statistical Calculations

1. **Maximum and Minimum Speed**: Calculates the maximum and minimum speed attained by the athlete during the recorded sessions.

2. **Data Transformation**: Converts the 'Time' column to datetime format and extracts hours, minutes, and seconds for further analysis.

### Visualizations

The script generates three types of plots using Matplotlib:

1. **Speed vs Time**: Line plot showing how the athlete's speed varied over time.
   
2. **Altitude vs Time**: Line plot depicting changes in altitude over the recorded sessions.
   
3. **Heart Rate vs Time**: Line plot illustrating the athlete's heart rate progression throughout the sessions.

### Additional Calculations

Calculates the average speed achieved by the athlete over the recorded sessions.

## How to Use

1. Ensure you have Python installed on your system.
2. Install required dependencies:
   ```
   pip install pandas matplotlib numpy
   ```
3. Place your Excel file (`coureur1.xls`) in the same directory as the script.
4. Run the script:
   ```
   python athlete_performance_analysis.py
   ```
5. The script will perform data analysis, generate plots, and display statistics related to the athlete's performance.

## Output

The script will save the generated plots (`Vitesse en fonction du temps.png`, `Altitude en fonction du temps.png`, `Pulsation en fonction du temps.png`) in the current directory. It will also print statistical information such as maximum speed, minimum speed, average speed, and display cleaned data.
