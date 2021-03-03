import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

birddata = pd.read_csv("bird_tracking.csv")
birddata.info()
print(birddata.head())

bird_names = pd.unique(birddata.bird_name)
plt.figure(figsize = (7,7))
for bird in bird_names:
    ix = birddata.bird_name == bird
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    plt.plot(x, y, ".")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
#plt.legend(loc="lower right")
# plotting the speed with matplotlib
plt.figure(figsize = (8,4))
speed = birddata.speed_2d[birddata.bird_name == "Eric"]
ind = np.isnan(speed)
plt.hist(speed[~ind], bins=np.linspace(0, 30, 20), normed=True)
plt.xlabel("2D speed (m/s)")
plt.ylabel("Frequency")
plt.savefig("speedhist.pdf")

#plotting the speed with pandas
birddata.speed_2d.plot(kind="hist", range=[0, 30])
plt.xlabel("2D speed")
plt.savefig("pd_speedhist.pdf")
