# import pandas as pd
# from pandas import ExcelFile

# Cars_Path = '/Users/langgui/Downloads/steps.xlsx'



data = [(20262, 17083, 3179),
    (11709, 7251, 4458),
    (19447, 16248, 3199),
    (7000, 5447, 1553),
    (13291, 9459, 3832),
    (14076, 9633, 4443),
    (14574, 11478, 3096),
    (10481, 8254, 2227),
    (9470, 7010, 2460),
    (23482, 12009, 11473),
    (14764, 11002, 3762),
    (5322, 3378, 1944),
    (15862, 10787, 5075),
    (13245, 10517, 2728),
    (16257, 14587, 1670),
    (12677, 10180, 2497),
    (14226, 8702, 5524),
    (17155, 5990, 11165),
    (22836, 16221, 6615),
    (19633, 11930, 7703),
    (15308, 13025, 2283),
    (23564, 21784, 1780),
    (10581, 9511, 1070),
    (10701, 9389, 1312),
    (3712, 1732, 1980),
    (9153, 8201, 952),
    (13196, 11657, 1539),
    (8836, 6432, 2404),
    (5706, 2215, 3491),
    (4589, 3641, 948),
    (11941, 10090, 1851),
    (7609, 5647, 1962),
    (14780, 12255, 2525),
]
#find the average of the first column of data and print out the result
# def average_iwatch_steps(data):
#     total = 0
#     num_days = len(data)
#     for iwatch, iphone, diff in data:
#         total += iwatch
#     return total / num_days

# print("Average iWatch steps per day:", average_iwatch_steps(data))




# def analyze_steps(data):
#     total_iwatch_steps = 0
#     total_iphone_steps = 0
#     total_difference = 0
#     num_days = len(data)
 
#     for iwatch, iphone, diff in data:
#         total_iwatch_steps += iwatch
#         total_iphone_steps += iphone
#         total_difference += diff

#     average_iwatch_steps = total_iwatch_steps / num_days
#     average_iphone_steps = total_iphone_steps / num_days
#     average_difference = total_difference / num_days

#     return average_iwatch_steps, average_iphone_steps, average_difference

# avg_iwatch, avg_iphone, avg_diff = analyze_steps(data)
# print("Average iWatch steps per day:", avg_iwatch)
# print("Average iPhone steps per day:", avg_iphone)
# print("Average difference per day:", avg_diff)


# chatgpt code
import pandas as pd
from io import StringIO

def load_data(data: str) -> pd.DataFrame:
    return pd.read_csv(StringIO(data), sep="\t")

def average_steps(data: pd.DataFrame) -> float:
    return data[["Iwatch(step)", "Iphone(step)"]].mean(axis=1).mean()

def average_steps_weekday_weekend(data: pd.DataFrame) -> dict:
    weekday_data = data[data["Weekday/Weekend"] == "Weekday"]
    weekend_data = data[data["Weekday/Weekend"] == "Weekend"]
    return {
        "Weekday": average_steps(weekday_data),
        "Weekend": average_steps(weekend_data),
    }

def consistency_ratio(data: pd.DataFrame) -> float:
    consistent = len(data[data["Consistency"].str.contains("consistent")])
    total = len(data)
    return consistent / total

def major_difference_days(data: pd.DataFrame) -> pd.DataFrame:
    return data[data["Consistency"] == "Major differences"]
