from sklearn.cluster.bicluster import SpectralCoclustering
import numpy as np, pandas as pd

whisky = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@whiskies.csv", index_col=0)
correlations = pd.DataFrame.corr(whisky.iloc[:,2:14].transpose())
correlations = np.array(correlations)

#----------WHISKY CLASSIFICATION-------------
# Exercise 1
# Exercise 2
# Exercise 3
# Exercise 4
# Exercise 5
# Exercise 6
# Exercise 7

#----------BIRD MIGRATION-------------


#----------SOCIAL NETWORK ANALYSIS-------------
