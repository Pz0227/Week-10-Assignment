# Author: Polly Zheng
# Date: 2025-11-07
# Purpose: Week 10 Assignment

# Import pandas and dataset
import pandas as pd
df = pd.read_csv('weather.csv')
print(df.head(3))  # check if data loaded correctly

# Show basic info about dataset
print("\nDataset dimensions before cleaning:", df.shape)
print(df.info())

# Data cleaning
# 1.check for null values
print("\nNull values per column:")
print(df.isnull().sum())

# 2.remove rows with null values and duplicates (if any)
df = df.dropna().drop_duplicates()

print("\nDataset dimensions after cleaning:", df.shape)
print(df.head())  # display first 5 rows after cleaning

# Data analysis and aggregation
philly_data = df[df['Station.City'] == 'Philadelphia']
print(philly_data.head(3))  # check whether filtering worked

avg_temp = philly_data['Data.Temperature.Avg Temp'].mean()

hottest_row = philly_data['Data.Temperature.Max Temp'].idxmax()
hottest_day = philly_data.loc[hottest_row, 'Date.Full']
hottest_temp = philly_data.loc[hottest_row, 'Data.Temperature.Max Temp']

coldest_row = philly_data['Data.Temperature.Min Temp'].idxmin()
coldest_day = philly_data.loc[coldest_row, 'Date.Full']
coldest_temp = philly_data.loc[coldest_row, 'Data.Temperature.Min Temp']

total_precipitation = philly_data['Data.Precipitation'].sum()
rainy_days = (philly_data['Data.Precipitation'] > 0).sum()

# Summary table

print("\nPhiladelphia Weather Summary:")
print("=" * 45)
print(f"{'Average Temperature:':25} {avg_temp:.2f}°F")
print(f"{'Hottest Day:':25} {hottest_day} ({hottest_temp}°F)")
print(f"{'Coldest Day:':25} {coldest_day} ({coldest_temp}°F)")
print(f"{'Total Precipitation:':25} {total_precipitation:.2f} in")
print(f"{'Number of Rainy Days:':25} {rainy_days} days")
print("=" * 45)
