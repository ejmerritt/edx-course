import pandas as pd
import numpy as np
import datetime
birddata = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@bird_tracking.csv", index_col=0)
print(birddata.head())

#Exercise 1
# First, use `groupby()` to group the data by "bird_name".
grouped_birds = birddata.groupby("bird_name")

# Now calculate the mean of `speed_2d` using the `mean()` function.
mean_speeds = grouped_birds.speed_2d.mean()
print(mean_speeds.head())

# Find the mean `altitude` for each bird.
mean_altitudes = grouped_birds.altitude.mean()

#Exercise 2
# Convert birddata.date_time to the `pd.datetime` format.
birddata.date_time = pd.to_datetime(birddata.date_time)
print(birddata.head())

# Create a new column of day of observation
birddata["date"] = [datetime.datetime.date(d) for d in birddata['date_time']]
print(birddata.head())

# Use `groupby()` to group the data by date.
grouped_bydates = birddata.groupby("date")

# Find the mean `altitude` for each date.
mean_altitudes_perday = grouped_bydates.altitude.mean()
print(mean_altitudes_perday.loc[datetime.date(2013,9,12)])

#Exercise 3
#Note that birddata already contains the date column. To find the average speed for each bird and day, create a new grouped dataframe called grouped_birdday that groups the data by both bird_name and date.
# Use `groupby()` to group the data by bird and date.
grouped_birdday = birddata.groupby(["bird_name", "date"])

# Find the mean `altitude` for each bird and date.
mean_altitudes_perday = grouped_birdday.altitude.mean()
print(mean_altitudes_perday.head())

#Exercise 4
#Store the average speeds for each bird and day as three pandas Series objects, one for each bird, then use the plotting code provided to plot the average speeds for each bird.
import matplotlib.pyplot as plt

eric_daily_speed  = birddata[["speed_2d", "date"]][birddata.bird_name == "Eric"]
sanne_daily_speed = birddata[["speed_2d", "date"]][birddata.bird_name == "Sanne"]
nico_daily_speed  = birddata[["speed_2d", "date"]][birddata.bird_name == "Nico"]
print(nico_daily_speed.loc[pd.Timestamp(2014,4,4).date()])

#eric_daily_speed.plot(label="Eric")
#sanne_daily_speed.plot(label="Sanne")
#nico_daily_speed.plot(label="Nico")
#plt.legend(loc="upper left")
#plt.show()
