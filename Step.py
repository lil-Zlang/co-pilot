import pandas as pd

def classify_activity(steps_list):
    # Initialize counters for each activity level
    none_count = 0
    a_little_count = 0
    low_count = 0
    moderate_count = 0
    high_count = 0

    # Iterate through the list of steps and classify each value
    for steps in steps_list:
        if steps is None:  # Check if the value is None
            none_count += 1
        elif 1 <= steps <= 300:  # Check if the value is between 1 and 300 (inclusive)
            a_little_count += 1
        elif 301 <= steps <= 1000:  # Check if the value is between 301 and 1000 (inclusive)
            low_count += 1
        elif 1001 <= steps <= 6000:  # Check if the value is between 1001 and 6000 (inclusive)
            moderate_count += 1
        elif steps > 6000:  # Check if the value is greater than 6000
            high_count += 1

    # Print the counts for each activity level
    print(f"activity level counts:")
    print(f"None: {none_count}")
    print(f"A little: {a_little_count}")
    print(f"Low: {low_count}")
    print(f"Moderate: {moderate_count}")
    print(f"High: {high_count}")




def count_days_and_steps(dates_list, steps_list_W, steps_list_I):
    # Initialize an empty dictionary to store the counts and indices of each date
    date_counts = {}

    # Iterate through the list of dates
    for index, date_val in enumerate(dates_list):
        # Convert the value to a string if it's not already
        if not isinstance(date_val, str):
            date_str = str(date_val)
        else:
            date_str = date_val

        # Extract the date part (month/day/year) from the date string
        date_only = date_str.split()[0]

        # Check if the date is already in the dictionary, if not, add it with a count of 1 and a new list for indices
        if date_only not in date_counts:
            date_counts[date_only] = {'count': 1, 'indices': [index]}
        else:
            # If the date is already in the dictionary, increment the count by 1 and append the index to the list of indices
            date_counts[date_only]['count'] += 1
            date_counts[date_only]['indices'].append(index)

    # Print the counts and steps for each date
    print(f"Total days: {len(date_counts)}")
    print("Dates:")
    for date, date_info in date_counts.items():
        count = date_info['count']
        indices = date_info['indices']
        steps_sum_W = sum([steps_list_W[i] for i in indices])
        steps_sum_I = sum([steps_list_I[i] for i in indices])

        print(f"{date}: {count} records, Iwatch {steps_sum_W} steps, Iphone {steps_sum_I} steps")

file_path = '/Users/langgui/Downloads/Hours-Step-14days.csv'
data = pd.read_csv(file_path)

# Extract the values in column B (ignoring the header)
column_b_data = data.iloc[:, 2].tolist()

# Extract the values in column C (ignoring the header)
column_c_data = data.iloc[:, 1].tolist()

# Call the classify_activity function with the extracted steps data
classify_activity(column_b_data)

# Extract the values in column A (ignoring the header)
column_a_data = data.iloc[:, 0].tolist()

# Call the count_days_and_steps function with the extracted dates and steps data
count_days_and_steps(column_a_data, column_b_data, column_c_data)









# def read_csv_data(file_path):
#     ''' Read CSV file and return a list of lists '''
#     import csv
#     with open(file_path, newline='') as csvfile:
#         data = list(csv.reader(csvfile))
#     return data
