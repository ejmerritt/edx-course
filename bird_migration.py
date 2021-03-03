import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

birddata = pd.read_csv("bird_tracking.csv")
birddata.info()
print(birddata.head())
bird_names = pd.unique(birddata.bird_name)
plt.figure(figsize = (7,7))
for bird in bird_names:
ix = birddata.bird_name ==bird_name
x, y = birddata.longitude[ix], birddata.latitude[ix]
plt.plot(x, y, ".")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
