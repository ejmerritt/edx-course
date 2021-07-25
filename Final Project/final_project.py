import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Import data
train_labels = pd.read_csv("train_labels.csv")
train_time_series = pd.read_csv("train_time_series.csv")
test_labels = pd.read_csv("test_labels.csv")
test_time_series = pd.read_csv("test_time_series.csv")

# Extract variables
time = train_time_series["timestamp"]
x = train_time_series[["x", "y", "z"]].iloc[::10,:]
y = train_labels

# Linear regression model
model = LinearRegression()
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.5)
model.fit(x_train, y_train)
model.score(x_test, y_test)

# Create classification model
#clf = RandomForestClassifier()
