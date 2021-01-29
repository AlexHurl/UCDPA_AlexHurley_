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

# Information about the CSV file
# birddata.info()

# print(birddata.values)

# print(birddata.head())

# print(birddata.index)

# print(birddata.describe())

# print(birddata.sort_values("speed_2d", ascending=False))

# Eric_MaxSpeed = birddata[(birddata["bird_name"] == "Eric") | (birddata["speed_2d"])]
# print(Eric_MaxSpeed)

# Max and Min dates
# print(birddata["date_time"].max())
# print(birddata["date_time"].min())

# print(birddata.drop_duplicates(subset="bird_name"))

#
# print(birddata["bird_name"].value_counts(sort=True))

# Perecentages of data
# print(birddata["bird_name"].value_counts(normalize=True))

# Mean speed
# print(birddata[birddata["bird_name"] == "Eric"]["speed_2d"].mean())
# print(birddata[birddata["bird_name"] == "Sanne"]["speed_2d"].mean())
# print(birddata[birddata["bird_name"] == "Nico"]["speed_2d"].mean())

# Grouping by name with mean speed
# print(birddata.groupby("bird_name")["speed_2d"].mean())

# Aggregating data (Multiple grouped summaries
# bird_stats = birddata.groupby("bird_name")["speed_2d"].agg([np.mix, np.max, np.mean, np.median])
# print(bird_stats)


# Grouping with agg
# print(birddata.groupby("bird_name")["speed_2d"].agg([min, max]))

# Indexing
# birddata_2 = birddata.set_index("bird_name")
# print(birddata_2)

# print(birddata_2.loc[["Eric", "Sanne"]])

# Multi Level index
# birddata_index = birddata.set_index(["bird_name", "altitude"]).sort_index()
# birddata_sorted = ["Eric", "Sanne", "Nico"]
# print(birddata_index.loc[birddata_sorted])

# subsetting by date
# Bird_Dates = birddata.set_index("date_time").sort_index()
# print(Bird_Dates)
# print(Bird_Dates.loc["2014-01-01 00:00:00+00":"2014-06-01 00:00:00+00"])







# Plot latitude and longitude
# # ix = birddata.bird_name == "Nico"
#
# # x, y = birddata.longitude[ix], birddata.latitude[ix]
#
# # plt.figure(figsize=(7,7))
# # plt.plot(x,y,".")
#
# # bird_names = pd.unique(birddata.bird_name)
#
# # bird_names = pd.unique(birddata.bird_name)
# # plt.figure(figsize=(7,7))
#  # for bird_name in bird_names:
#   #  ix = birddata.bird_name == bird_name
#   #  x, y = birddata.longitude[ix], birddata.latitude[ix]
#
#  #   plt.plot(x, y, ".", label=bird_name)
# # plt.xlabel("Birds Longitude")
# # plt.ylabel("Birds Latitude")
# # plt.legend(loc="lower right")
# plt.savefig("3Birds.pdf")




# DATE TIME CALCS
#
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
#     (birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))
#


