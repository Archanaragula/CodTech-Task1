# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
from sklearn.datasets import load_iris
iris = load_iris()

# Create a DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Map the species from numbers to actual species names
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Display the first few rows of the DataFrame
print("First few rows of the dataset:")
print(df.head())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Checking for missing values
print("\nChecking for missing values:")
print(df.isnull().sum())

# Visualize the distribution of each feature
plt.figure(figsize=(12, 8))
df.hist(bins=20, figsize=(12, 8), layout=(2, 2))
plt.suptitle('Feature Distributions')
plt.show()

# Visualize the pairplot to see the relationships between features
sns.pairplot(df, hue='species', diag_kind='kde')
plt.suptitle('Pairplot of Features')
plt.show()

# Correlation matrix
print("\nCorrelation matrix:")
corr_matrix = df.corr()
print(corr_matrix)

# Visualize the correlation matrix with a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap of Feature Correlations')
plt.show()

# Check for outliers using boxplots
plt.figure(figsize=(12, 8))
for i, column in enumerate(df.columns[:-1], 1):
    plt.subplot(2, 2, i)
    sns.boxplot(x='species', y=column, data=df)
    plt.title(f'Boxplot of {column}')
plt.tight_layout()
plt.show()
