import pandas as pd
from datetime import datetime

#count_days_and_average_hr
def count_days_and_average_hr(dates_list, hr_list):
    date_counts = {}

    for index, date_val in enumerate(dates_list):
        if not isinstance(date_val, str):
            date_str = str(date_val)
        else:
            date_str = date_val

        date_obj = datetime.strptime(date_str, '%m/%d/%y %H:%M')
        date_only = date_obj.strftime('%Y-%m-%d')
        time_only = date_obj.strftime('%H:%M')  # get hour and minute

        if date_only not in date_counts:
            date_counts[date_only] = {'times': {time_only: {'count': 1, 'indices': [index]}}, 'rest_count': 0, 'active_count': 0}
        elif time_only not in date_counts[date_only]['times']:
            date_counts[date_only]['times'][time_only] = {'count': 1, 'indices': [index]}
        else:
            date_counts[date_only]['times'][time_only]['count'] += 1
            date_counts[date_only]['times'][time_only]['indices'].append(index)

    data = []
    for date, date_info in date_counts.items():
        for time, time_info in date_info['times'].items():
            count = time_info['count']
            indices = time_info['indices']
            hr_data = [hr_list[i] for i in indices]
            rest_count = len([hr for hr in hr_data if hr < 100])
            active_count = count - rest_count
            avg_hr = sum(hr_data) / count

            data.append({'Date': date, 'Time': time, 'Active Count': active_count, 'Rest Count': rest_count})

    df = pd.DataFrame(data)
    df.to_excel('HeartRateData.xlsx', index=False)

    print(f"Total days: {len(date_counts)}")
    print("Dates:")
    for date, date_info in date_counts.items():
        print(f"{date}:")
        for time, time_info in date_info['times'].items():
            count = time_info['count']
            indices = time_info['indices']
            hr_data = [hr_list[i] for i in indices]
            rest_count = len([hr for hr in hr_data if hr < 100])
            active_count = count - rest_count
            date_counts[date]['rest_count'] += rest_count
            date_counts[date]['active_count'] += active_count

            avg_hr = sum(hr_data) / count

            print(f"    Time {time}: {count} records, average hourly heart rate: {avg_hr:.2f}, Active count: {active_count}, Rest count: {rest_count}")
        print(f"    Total Active count: {date_counts[date]['active_count']}, Total Rest count: {date_counts[date]['rest_count']}")

#Read the csv file
file_path = '/Users/langgui/Downloads/14DAYS_MinHR.csv'
data = pd.read_csv(file_path)

column_a_data = data.iloc[:, 0].tolist()
column_d_data = data.iloc[:, 3].tolist()

count_days_and_average_hr(column_a_data, column_d_data)
