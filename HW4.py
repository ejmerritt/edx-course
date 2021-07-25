from sklearn.cluster import SpectralCoclustering
import numpy as np, pandas as pd

whisky = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@whiskies.csv", index_col=0)
correlations = pd.DataFrame.corr(whisky.iloc[:,2:14].transpose())
correlations = np.array(correlations)

#----------WHISKY CLASSIFICATION-------------
# Exercise 1
# Execute the following code and follow along with the comments. We will later adapt this code to plot the correlations among distillery flavor profiles as well as plot a geographical map of distilleries colored by region and flavor profile.
# Once you have plotted the code, hover, click, and drag your cursor on the plot to interact with it. Additionally, explore the icons in the top-right corner of the plot for more interactive options!
# First, we import a tool to allow text to pop up on a plot when the cursor hovers over it.  Also, we import a data structure used to store arguments of what to plot in Bokeh.  Finally, we will use numpy for this section as well!
from bokeh.models import HoverTool, ColumnDataSource
# Let's plot a simple 5x5 grid of squares, alternating between two colors.
plot_values = [1,2,3,4,5]
plot_colors = ['#0173b2', '#de8f05']
# How do we tell Bokeh to plot each point in a grid?  Let's use a function that finds each combination of values from 1-5.
from itertools import product
grid = list(product(plot_values, plot_values))
print(grid)
# The first value is the x coordinate, and the second value is the y coordinate.
xs, ys = zip(*grid)
print(xs)
print(ys)
# Now we will make a list of colors, alternating between red and blue.
colors = [plot_colors[i%2] for i in range(len(grid))]
print(colors)
# Finally, let's determine the strength of transparency (alpha) for each point where 0 is completely transparent.
alphas = np.linspace(0, 1, len(grid))
# Bokeh likes each of these to be stored in a special dataframe, called
# ColumnDataSource.  Let's store our coordinates, colors, and alpha values.
source = ColumnDataSource(
    data = {
        "x": xs,
        "y": ys,
        "colors": colors,
        "alphas": alphas,
    }
)
# We are ready to make our interactive Bokeh plot!
from bokeh.plotting import figure, output_file, show
output_file("Basic_Example.html", title="Basic Example")
fig = figure(tools="hover")
fig.rect("x", "y", 0.9, 0.9, source=source, color="colors",alpha="alphas")
hover = fig.select(dict(type=HoverTool))
hover.tooltips = {
    "Value": "@x, @y",
    }
show(fig)

# Exercise 2
# Create a dictionary region_colors with regions as keys and cluster_colors as values.
# Print region_colors.
cluster_colors = ['#0173b2', '#de8f05', '#029e73', '#d55e00', '#cc78bc', '#ca9161']
regions = ["Speyside", "Highlands", "Lowlands", "Islands", "Campbelltown", "Islay"]

region_colors = dict(zip(regions, cluster_colors))
print(region_colors["Campbelltown"])

# Exercise 3
#Edit the code to define correlation_colors for each distillery pair to have input 'white' if their correlation is less than 0.7.
#whisky is a pandas dataframe, and Group is a column consisting of distillery group memberships. For distillery pairs with correlation greater than 0.7, if they share the same whisky group, use the corresponding color from cluster_colors. Otherwise, the correlation_colors value for that distillery pair will be defined as 'lightgray'.
distilleries = list(whisky.Distillery)
correlation_colors = []
for i in range(len(distilleries)):
    for j in range(len(distilleries)):
        if np.any(correlations[j]) < 0.7:                     # if low correlation,
            correlation_colors.append('white')         # just use white.
        else:                                          # otherwise,
            if whisky.Group[i] == whisky.Group[j]:                  # if the groups match,
                correlation_colors.append(cluster_colors[whisky.Group[i]]) # color them by their mutual group.
            else:                                      # otherwise
                correlation_colors.append('lightgray') # color them lightgray.

# Exercise 4
#correlation_colors is a list of string colors for each pair of distilleries. Set this as color in ColumnDataSource.
#Define correlations in source using correlations from the previous exercise. To convert correlations from a np.array to a list, use the flatten() method. This correlation coefficient will be used to define both the color transparency as well as the hover text for each square.
source = ColumnDataSource(
    data = {
        "x": np.repeat(distilleries,len(distilleries)),
        "y": list(distilleries)*len(distilleries),
        "colors": correlation_colors,
        "correlations": correlations.flatten()
    }
)

output_file("Whisky Correlations.html", title="Whisky Correlations")
fig = figure(title="Whisky Correlations",
    x_axis_location="above", x_range=list(reversed(distilleries)), y_range=distilleries,
    tools="hover,box_zoom,reset")
fig.grid.grid_line_color = None
fig.axis.axis_line_color = None
fig.axis.major_tick_line_color = None
fig.axis.major_label_text_font_size = "5pt"
fig.xaxis.major_label_orientation = np.pi / 3
fig.rect('x', 'y', .9, .9, source=source,
     color='colors', alpha='correlations')
hover = fig.select(dict(type=HoverTool))
hover.tooltips = {
    "Whiskies": "@x, @y",
    "Correlation": "@correlations",
}
show(fig)

# Exercise 5
#Run the following code, to be adapted in the next section. Compare this code to that used in plotting the distillery correlations.
points = [(0,0), (1,2), (3,1)]
xs, ys = zip(*points)
colors = ['#0173b2', '#de8f05', '#029e73']

output_file("Spatial_Example.html", title="Regional Example")
location_source = ColumnDataSource(
    data={
        "x": xs,
        "y": ys,
        "colors": colors,
    }
)

fig = figure(title = "Title",
    x_axis_location = "above", tools="hover, save")
fig.plot_width  = 300
fig.plot_height = 380
fig.circle("x", "y", size=10, source=location_source,
     color='colors', line_color = None)

hover = fig.select(dict(type = HoverTool))
hover.tooltips = {
    "Location": "(@x, @y)"
}
show(fig)

# Exercise 6
#Adapt the given code beginning with the first comment and ending with show(fig) to create the function location_plot(), as described above.
#Region is a column of in the pandas dataframe whisky, containing the regional group membership for each distillery. Make a list consisting of the value of region_colors for each distillery, and store this list as region_cols.
#Use location_plot to plot each distillery, colored by its regional grouping.
def location_plot(title, colors):
    output_file(title+".html")
    location_source = ColumnDataSource(
        data = {
            "x": whisky[" Latitude"],
            "y": whisky[" Longitude"],
            "colors": colors,
            "regions": whisky.Region,
            "distilleries": whisky.Distillery
        }
    )

    fig = figure(title = title,
        x_axis_location = "above", tools="hover, save")
    fig.plot_width  = 400
    fig.plot_height = 500
    fig.circle("x", "y", size=9, source=location_source, color='colors', line_color = None)
    fig.xaxis.major_label_orientation = np.pi / 3
    hover = fig.select(dict(type = HoverTool))
    hover.tooltips = {
        "Distillery": "@distilleries",
        "Location": "(@x, @y)"
    }
    show(fig)

region_cols = []
for i in whisky.Region:
    region_cols.append(region_colors[i])
location_plot("Whisky Locations and Regions", region_cols)

# Exercise 7
#Create the list region_cols consisting of the color in region_colors that corresponds to each whisky in whisky.Region.
#Similarly, create a list classification_cols consisting of the color in cluster_colors that corresponds to each cluster membership in whisky.Group.
#Create two interactive plots of distilleries, one using region_cols and the other with colors defined by called classification_cols. How well do the coclustering groupings match the regional groupings?
classification_cols = []
for i in whisky.Group:
    classification_cols.append(cluster_colors[i])

location_plot("Whisky Locations and Regions", region_cols)
location_plot("Whisky Locations and Groups", classification_cols)

#----------BIRD MIGRATION-------------
import pandas as pd
import numpy as np
birddata = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@bird_tracking.csv", index_col=0)
birddata.head()


#----------SOCIAL NETWORK ANALYSIS-------------
# Exercise 1
    #Create a function marginal_prob that takes a dictionary chars with personal IDs as keys and characteristics as values; it should return a dictionary with characteristics as keys and their marginal probability (frequency of occurence of a characteristic divided by the sum of frequencies of each characteristic) as values.
    #Create a function chance_homophily(chars) that takes a dictionary chars defined as above and computes the chance homophily (homophily due to chance alone) for that characteristic.
    #A sample of three peoples' favorite colors is given in favorite_colors. Use your function to compute the chance homophily in this group, and store it as color_homophily.
    #Print color_homophily.
from collections import Counter
import numpy as np

def marginal_prob(chars):
    frequencies = dict(Counter(chars.values()))
    sum_frequencies = sum(frequencies.values())
    return {char: freq / sum_frequencies for char, freq in frequencies.items()}

def chance_homophily(chars):
    marginal_probs = marginal_prob(chars)
    return np.sum(np.square(list(marginal_probs.values())))

favorite_colors = {
    "ankit":  "red",
    "xiaoyu": "blue",
    "mary":   "blue"
}

color_homophily = chance_homophily(favorite_colors)
print(color_homophily)

# Exercise 2
#In the remaining exercises, we will calculate actual homophily in these village and compare the obtained values to those obtained by chance. In Exercise 2, we subset the data into individual villages and store them.
#Note that individual_characteristics.dta contains several characteristics for each individual in the dataset such as age, religion, and caste. Use the pandas library to read in and store these characteristics as a dataframe called df.
    #Store separate datasets for individuals belonging to Villages 1 and 2 as df1 and df2, respectively.
    #Note that some attributes may be missing for some individuals.
    #Use the head method to display the first few entries of df1.
import pandas as pd
df  = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@individual_characteristics.csv", low_memory=False, index_col=0)
df1 = df[df.village == 1]
df2 = df[df.village == 2]

df1.head()

# Exercise 3
#Exercise 3, we define a few dictionaries that enable us to look up the sex, caste, and religion of members of each village by personal ID. For Villages 1 and 2, their personal IDs are stored as pid.
    #Define dictionaries with personal IDs as keys and a given covariate for that individual as values. Complete this for the sex, caste, and religion covariates, for Villages 1 and 2.
    #For Village 1, store these dictionaries into variables named sex1, caste1, and religion1.
    #For Village 2, store these dictionaries into variables named sex2, caste2, and religion2.
sex1 = df1.set_index("pid")["resp_gend"].to_dict()
caste1 = df1.set_index("pid")["caste"].to_dict()
religion1 = df1.set_index("pid")["religion"].to_dict()

sex2 = df2.set_index("pid")["resp_gend"].to_dict()
caste2 = df2.set_index("pid")["caste"].to_dict()
religion2 = df2.set_index("pid")["religion"].to_dict()

# Exercise 4
#Use chance_homophily to compute the chance homophily for sex, caste, and religion In Villages 1 and 2. Consider whether the chance homophily for any attribute is very high for either village.
chance_homophily(sex1)
chance_homophily(sex2)
chance_homophily(religion1)
chance_homophily(religion2)
chance_homophily(caste1)
chance_homophily(caste2)

# Exercise 5
#Complete the function homophily(), which takes a network G, a dictionary of node characteristics chars, and node IDs IDs. For each node pair, determine whether a tie exists between them, as well as whether they share a characteristic. The total count of these is num_ties and num_same_ties, respectively, and their ratio is the homophily of chars in G. Complete the function by choosing where to increment num_same_ties and num_ties.
def homophily(G, chars, IDs):
    """
    Given a network G, a dict of characteristics chars for node IDs,
    and dict of node IDs for each node in the network,
    find the homophily of the network.
    """
    num_same_ties = 0
    num_ties = 0
    for n1, n2 in G.edges():
        if IDs[n1] in chars and IDs[n2] in chars:
            if G.has_edge(n1, n2):
                num_ties += 1
                if chars[IDs[n1]] == chars[IDs[n2]]:
                    num_same_ties += 1
    return (num_same_ties / num_ties)

# Exercise 6
#In this dataset, each individual has a personal ID, or PID, stored in key_vilno_1.csv and key_vilno_2.csv for villages 1 and 2, respectively. data_filepath1 and data_filepath2 contain the URLs to the datasets used in this exercise. Use pd.read_csv to read in and store key_vilno_1.csv and key_vilno_2.csv as pid1 and pid2 respectively.
data_filepath1 = "https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@key_vilno_1.csv"
data_filepath2 = "https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@key_vilno_2.csv"

pid1 = pd.read_csv(data_filepath1)
pid2 = pd.read_csv(data_filepath2)
pid1.iloc[100]

# Exercise 7
# Use your homophily() function to compute the observed homophily for sex, caste, and religion in Villages 1 and 2. Print all six values.
# Use chance_homophily() to compare the observed homophily values to the chance homophily values. Are observed values higher or lower than those expected by chance?
import networkx as nx
A1 = np.array(pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@adj_allVillageRelationships_vilno1.csv", index_col=0))
A2 = np.array(pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@adj_allVillageRelationships_vilno2.csv", index_col=0))
G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

pid1 = pd.read_csv(data_filepath1, dtype=int)['0'].to_dict()
pid2 = pd.read_csv(data_filepath2, dtype=int)['0'].to_dict()

homophily(G1, [resp_gend, caste, religion], pid1)

print(f"The homophily for Sex in Village 1 is {homophily(G1, sex1, pid1)}")
print(f"Higher than chance? {(homophily(G1, sex1, pid1) > chance_homophily(sex1))}")
print(f"The homophily for Caste in Village 1 is {homophily(G1, caste1, pid1)}")
print(f"Higher than chance? {(homophily(G1, caste1, pid1) > chance_homophily(caste1))}")
print(f"The homophily for Religion in Village 1 is {homophily(G1, religion1, pid1)}")
print(f"Higher than chance? {(homophily(G1, religion1, pid1) > chance_homophily(religion1))}")

print(f"The homophily for Sex in Village 2 is {homophily(G2, sex2, pid2)}")
print(f"Higher than chance? {(homophily(G2, sex2, pid2) > chance_homophily(sex2))}")
print(f"The homophily for Caste in Village 2 is {homophily(G2, caste2, pid2)}")
print(f"Higher than chance? {(homophily(G2, caste2, pid2) > chance_homophily(caste2))}")
print(f"The homophily for Religion in Village 2 is {homophily(G2, religion2, pid2)}")
print(f"Higher than chance? {(homophily(G2, religion2, pid2) > chance_homophily(religion2))}")
