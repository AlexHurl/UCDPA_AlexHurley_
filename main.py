# Importing necessary packages
import pandas as pd

import datetime

birddata = pd.read_csv("bird_tracking.csv")

# Print name of each bird
bird_names = pd.unique(birddata.bird_name)
print(bird_names)

# Information about the CSV file
birddata.info()

# Import Matplotlib and Numpy
import matplotlib.pyplot as plt
import numpy as np


