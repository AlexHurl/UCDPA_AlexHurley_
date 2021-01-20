# Importing necessary packages
import pandas as pd

import datetime

seagulldata = pd.read_csv("bird_tracking.csv")

# Print name of each bird
seagull_names = pd.unique(seagulldata.bird_name)
print(seagull_names)

# Information about the CSV file
seagulldata.info()

# Import Matplotlib and Numpy
import matplotlib.pyplot as plt
import numpy as np

ix = seagulldata
