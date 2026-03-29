PROJECT TITLE 

Clustering: Customer Segmentation

Description: 

In this project, clustering analysis is performed to group customers based on their similarities. The goal is to identify meaningful customer segments using behavioral and demographic data, and compare different clustering techniques to understand which method provides better insights.

Dataset:

Source: Kaggle

Link: https://www.kaggle.com/code/sachinbhardwaj97/customer-segmentation-k-means-pca-4-segments/input?select=marketing_campaign.csv

Description:

The dataset contains customer information related to demographics, purchasing behavior, and marketing interactions. It is used to segment customers into groups based on similarities.

Steps Performed:

1. Import Required Libraries

2. Load Data

3. Data Cleaning

-Removed missing values

-Handled outliers (Age, Income)

-Feature engineering (Total_Spent, Total_Purchases, Age, Tenure)

-Dropped redundant columns

4. Exploratory Data Analysis

-Summary statistics

-Distribution and correlation analysis

5. Data Visualization

-Boxplots and histograms

-Cluster comparison plots

-PCA visualization

6.Model Building

-K-Means clustering (k = 4)

-Feature refinement (removed Recency)

-Hierarchical clustering (k = 2 and k = 4)

-Model comparison using silhouette score


Results:

-K-Means (k = 4):

  -Meaningful segmentation

  -Silhouette Score ≈ 0.21

-Improved K-Means:

   -Slight improvement after removing Recency

-Hierarchical Clustering (k = 2):

   -Best silhouette score ≈ 0.305

   -Clear separation into high-value and low-value customers

-PCA:

   - ~63.6% variance explained

   - Moderate cluster separation observed

Tools Used:

-Python

-NumPy

-Pandas

-Matplotlib

-Seaborn

-Scikit-learn

Conclusion:

The analysis shows that while K-Means provides more detailed segmentation, the clusters are not strongly separated. Hierarchical clustering reveals that the data naturally forms two main groups with better separation. However, for practical applications, a balance between cluster quality and interpretability is important, making both approaches useful in different contexts.

Author:

Sidharth Gautam
