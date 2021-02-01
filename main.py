# Importing necessary packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import datetime
birddata = pd.read_csv("bird_tracking.csv")

# Print name of each bird
bird_names = pd.unique(birddata.bird_name)
# print(bird_names)

# # Information about the CSV file
# birddata.info()
#
# print(birddata.values)
#
# print(birddata.head())
#
# print(birddata.index)
#
# print(birddata.describe())
#
#
# print(birddata.sort_values("speed_2d", ascending=False))

# Eric_MaxSpeed = birddata[(birddata["bird_name"] == "Eric") | (birddata["speed_2d"] == max)]
# print(Eric_MaxSpeed)

# Max and Min dates
# print(birddata["date_time"].max())
# print(birddata["date_time"].min())

# Drop dupilcates of speed
#Dupes_dropped = birddata.drop_duplicates(subset="speed_2d")
#print(Dupes_dropped)


# Value counts
# print(birddata["bird_name"].value_counts(sort=True))

# Perecentages of data
# print(birddata["bird_name"].value_counts(normalize=True))

# # Mean speed
# print(birddata[birddata["bird_name"] == "Eric"]["speed_2d"].mean())
# print(birddata[birddata["bird_name"] == "Sanne"]["speed_2d"].mean())
# print(birddata[birddata["bird_name"] == "Nico"]["speed_2d"].mean())

# Grouping by name with mean speed
# print(birddata.groupby("bird_name")["speed_2d"].mean())

# Aggregating data (Multiple grouped summaries
# bird_stats = birddata.groupby("bird_name")("speed_2d")agg([np.mix, np.max, np.mean, np.median])
# print(bird_stats)




# Grouping with agg stats on max and min for each bird
# print(birddata.groupby("bird_name")["speed_2d"].agg([min, max]))
#
# print(birddata.groupby("bird_name")["altitude"].agg([min, max]))
#
# print(birddata.groupby("bird_name")["longitude"].agg([min, max]))
#
# print(birddata.groupby("bird_name")["latitude"].agg([min, max]))


#Multi Level index .Here we can sort the bird data using  MLI so we can each bird from the persepective of how how long they were travelling for using the bird_name and date_time
# birddata_index = birddata.set_index(["bird_name", "date_time"]).sort_index()
# birddata_sorted = ["Sanne"]
# print(birddata_index.loc[birddata_sorted])

# subsetting by date
# Bird_Dates = birddata.set_index("date_time").sort_index()
# print(Bird_Dates)
# print(Bird_Dates.loc["2014-01-01 00:00:00+00":"2014-06-01 00:00:00+00"])







# Plot latitude and longitude of Eric Nice and Sanne
# ix = birddata.bird_name == "Eric"
#
# x, y = birddata.longitude[ix], birddata.latitude[ix]
#
# plt.figure(figsize=(7,7))
# plt.plot(x,y,".")
#
# bird_names = pd.unique(birddata.bird_name)

  ## store the unique bird name as vairable x and y.
# bird_names = pd.unique(birddata.bird_name)
# plt.figure(figsize=(7,7))

 ## Use X and Y labels for longitude and latitude respectively
# for bird_name in bird_names:
#   ix = birddata.bird_name == bird_name
#   x, y = birddata.longitude[ix], birddata.latitude[ix]
#   plt.plot(x, y, ".", label=bird_name)
# plt.xlabel("Birds Longitude")
# plt.ylabel("Birds Latitude")
# plt.legend(loc="lower right")
# plt.show()





# Calculating mean speed

# datetime.datetime.today()
#
# time_1 = datetime.datetime.today()
#
# time_2 = datetime.datetime.today()
#
# time_2 - time_1
#
# time_2 = datetime.datetime.today()
#
# time_2 - time_1
#
# date_str = birddata.date_time[0]
#
# date_str[:-3]
#
# datetime.datetime.strptime(date_str[:-3], "%Y-%m-%d %H:%M:%S")
#
# timestamps = []
# for k in range(len(birddata)):
#     timestamps.append(datetime.datetime.strptime\
#     # Slices the +00 from the time stamps
#     (birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))
#
# timestamps[0:3]
#
# birddata["timestamp"] = pd.Series(timestamps, index=birddata.index)
#
# birddata.head()
#
# birddata.timestamp[4] - birddata.timestamp[3]

# ix = birddata.bird_name == "Eric"
#
# speed = birddata.speed_2d[ix]

# seaborn to show frequency of speeds
# birddata["speed_2d"].plot.hist()
# plt.show()


#Make a list that captures the amount fo time since the start of the data collection
# times = birddata.timestamp[birddata.bird_name == "Eric"]
# elapsed_time = [time - times[0] for time in times]
#
# elapsed_time[1000]
#
# elapsed_time[1000] / datetime.timedelta(days=1)
#
# elapsed_time[1000] / datetime.timedelta(hours=1)
#
#
#
#
# #Length of entries
# print(len(elapsed_time))
# # date time today
# print(datetime.datetime.today())
#
#
#
#
# data = birddata[birddata.bird_name == "Eric"]
# times = data.timestamp
# elapsed_time = [time - times[0] for time in times]
# elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)
#
# next_day = 1
# inds = []
# daily_mean_speed = []
# for (i, t) in enumerate(elapsed_days):
#     if t < next_day:
#         inds.append(i)
#     else:
#         # compute mean speed
#         daily_mean_speed.append(np.mean(data.speed_2d[inds]))
#         next_day += 1
#         inds = []
#
# plt.figure(figsize=(8, 6))
# plt.plot(daily_mean_speed)
# plt.xlabel("Day")
# plt.ylabel("Mean speed (m/s)")
# plt.show()
#








