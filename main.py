# Importing necessary packages
import pandas as pd

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
print(birddata["date_time"].max())
print(birddata["date_time"].min())

# Import Matplotlib and Numpy

import matplotlib.pyplot as plt
import numpy as np
import datetime