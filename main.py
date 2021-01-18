# Importing necessary packages
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
birddata = pd.read_csv("bird_tracking.csv")

# Print name of each bird
bird_names = pd.unique(birddata.bird_name)
print(bird_names)


