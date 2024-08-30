### NAME: ARCHANA RAGULA
### COMPANY: CODTECH IT SOLUTIONS
### ID:CT08DS5886
### DOMAIN:DATA ANALYTICS
### DURATION:AUGUST TO SEPTEMBER
### MENTOR: MUZAMMIL AHMED
### TASK1: Dataset Exploratory Data Analysis


## Dataset Exploratory Data Analysis (EDA)
This project performs an Exploratory Data Analysis (EDA) on the famous Iris dataset using Python libraries such as Pandas, NumPy, Matplotlib, and Seaborn. The goal is to explore the dataset's characteristics, distributions, correlations, and potential outliers through various visualizations.

## Prerequisites
Before running the script, make sure you have the following Python libraries installed:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

## Script Overview:
The script performs the following tasks:

## Importing Necessary Libraries:
The script starts by importing the essential Python libraries needed for data manipulation, analysis, and visualization.

## Loading the Iris Dataset:
The Iris dataset is loaded using the load_iris() function from the sklearn.datasets module. The dataset contains 150 observations of iris flowers with four features: sepal length, sepal width, petal length, and petal width, along with the species label.

## Creating a DataFrame:
A Pandas DataFrame is created from the Iris dataset for easier manipulation. The species labels are mapped from numerical values (0, 1, 2) to their respective species names (Setosa, Versicolor, Virginica).

## Displaying the First Few Rows:
The script displays the first few rows of the dataset to give a quick overview of the data.

## Summary Statistics:
Summary statistics for each numerical feature are computed using the describe() function. This provides information such as mean, standard deviation, min, max, and quartiles.

## Checking for Missing Values:
The script checks for any missing values in the dataset using the isnull().sum() function. This ensures that the data is clean before proceeding with further analysis.

## How to Run the Script
- Make sure you have installed all the required libraries.
- Copy the script into a .py file.

## Output:
- *First few rows of the dataset*: Provides an initial look at the data.
- *Summary statistics*: Offers insights into the statistical properties of the features.
- *Missing values check*: Ensures data completeness.
- *Histograms*: Displays the distribution of each feature.
- *Pairplot*: Shows relationships between features and how they differ across species.
- *Correlation matrix and heatmap*: Indicates the strength and direction of relationships between features.
- *Boxplots*: Helps detect outliers for each feature across different species.
