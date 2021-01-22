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


# Import Matplotlib and Numpy

import matplotlib.pyplot as plt
import numpy as np
import datetime