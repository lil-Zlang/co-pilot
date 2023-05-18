import pandas as pd
from collections import defaultdict
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/Users/langgui/Downloads/14DAYS_MinHR.csv')

# Convert the first column to datetime format
df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0])

# Set the date column as the index
df.set_index(df.iloc[:, 0], inplace=True)

# Resample the heart rate column every 10 minutes and calculate the mean
resampled_df = df.iloc[:, 3].resample('10T').mean()

# Initialize a counter
counter = defaultdict(lambda: defaultdict(int))

# Iterate over the resampled data
for time, avg_heart_rate in resampled_df.items():
    # If the average heart rate is over 100, increment the counter
    if avg_heart_rate > 100:
        counter[time.date()][time.hour] += 1

# Create a plot for each day
for date, hourly_counts in counter.items():
    # Create a list of counts for each hour of the day
    counts = [hourly_counts.get(hour, 0) for hour in range(24)]
    
    # Skip this day if there were no instances of heart rate exceeding 100
    if sum(counts) == 0:
        continue

    # Print the data
    for hour, count in hourly_counts.items():
        print(f'On {date}, at {hour:02d}:00, the average heart rate exceeded 100 in {count} ten-minute intervals.')

    # Create a bar plot
    plt.figure(figsize=(10, 5))
    plt.bar(range(24), counts)
    plt.xticks(range(24))
    plt.xlabel('Hour of the day')
    plt.ylabel('Number of ten-minute intervals')
    plt.title(f'Heart rate over 100 on {date}')
    plt.show()

    # Print the data and summary
    for hour, count in hourly_counts.items():
        print(f'On {date}, at {hour:02d}:00, the average heart rate exceeded 100 in {count} ten-minute intervals.')
    print(f'On {date}, the average heart rate exceeded 100 in {sum(counts)} ten-minute intervals in total.')
