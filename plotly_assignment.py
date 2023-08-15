# -*- coding: utf-8 -*-
"""Plotly assignment

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xs2Xhu-q9p_IrGMq4fj4osnULnXZcYvN
"""

#Plotly assignment
#Question.1 Load the "titanic" dataset using the load_dataset function of seaborn. Use Plotly express to plot a
#scatter plot for age and fare columns in the titanic dataset.
#Answer.1 :
import seaborn as sns
import plotly.express as px

# Load the "titanic" dataset using Seaborn's load_dataset function
titanic_data = sns.load_dataset('titanic')

# Create a scatter plot using Plotly Express
fig = px.scatter(titanic_data, x='age', y='fare', title='Scatter plot for Age and Fare in Titanic dataset')

# Show the plot
fig.show()

#Question.2 Using the tips dataset in the Plotly library, plot a box plot using Plotly express.
#Answer.2 :
import seaborn as sns
import plotly.express as px

tips_data = px.data.tips()

# Create a box plot using Plotly Express
fig = px.box(tips_data, x='day', y='total_bill', title='Box plot for Total Bill on Each Day')

# Show the plot
fig.show()

#Question.3 Using the tips dataset in the Plotly library, Plot a histogram for x= "sex" and y="total_bill" column in
#the tips dataset. Also, use the "smoker" column with the pattern_shape parameter and the "day"
#column with the color parameter.
#Answer.3 :
import seaborn as sns
import plotly.express as px

tips_data = px.data.tips()

# Create a histogram using Plotly Express
fig = px.histogram(
    tips_data,
    x='sex',
    y='total_bill',
    color='day',
    pattern_shape='smoker',
    title='Histogram of Total Bill for Each Sex',
)

# Show the plot
fig.show()

#Question.4 Using the iris dataset in the Plotly library, Plot a scatter matrix plot, using the "species" column for
#the color parameter.
#Note: Use "sepal_length", "sepal_width", "petal_length", "petal_width" columns only with the
#dimensions parameter.
#Answer.4 :
import plotly.express as px

# Load the "iris" dataset from Plotly Express (No need to load separately)
iris_data = px.data.iris()

# Create a scatter matrix plot using Plotly Express
fig = px.scatter_matrix(
    iris_data,
    dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"],
    color="species",
    title="Scatter Matrix Plot for Iris Dataset",
)

# Show the plot
fig.show()

#Question.5 What is Distplot? Using Plotly express, plot a distplot.
#Answer.5 : A distplot (short for distribution plot) is a type of plot used in data visualization to show the distribution of a univariate (single variable)
#dataset. It combines multiple visual elements to provide insights into the shape, spread, and central tendency of the data.

#The main components of a distplot are:

#Histogram: A histogram is a bar plot that represents the distribution of the data by dividing it into intervals (bins) and displaying the frequency or
#count of data points falling into each bin. The height of each bar corresponds to the number of data points in that bin.

#Kernel Density Estimate (KDE) Plot: The KDE plot is a smoothed representation of the data's underlying probability density function. It provides an
#estimation of the continuous probability distribution that generated the observed data. The KDE plot is especially useful when dealing with continuous data,
#as it provides a smooth curve that approximates the distribution.

#Rug Plot: A rug plot is a one-dimensional scatter plot that places a small vertical tick or "rug" for each data point along the axis. It helps visualize the
#exact data points in the distribution.

#Combining these elements, a distplot provides a comprehensive view of the data distribution, allowing users to understand key characteristics such as
#central
#tendency, spread, skewness, and multimodality (presence of multiple peaks).
#Plotly Express does not have a direct distplot function like Seaborn. However, Plotly Express offers an alternative for creating a distribution plot
#using the histogram function, which can display the distribution of a single variable.

#Here's how you can create a distribution plot (histogram) using Plotly Express:

import plotly.express as px

# Sample data (replace this with your actual data)
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Create a distribution plot using Plotly Express
fig = px.histogram(data, nbins=10, title='Distribution Plot')

# Show the plot
fig.show()