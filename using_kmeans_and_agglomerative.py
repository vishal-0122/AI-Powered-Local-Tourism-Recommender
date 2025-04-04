# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1R9Lm0SVG4NNCg_qJmIOlFjhaxJMOwSFF
"""

#Step 1: Import Libraries & Load Dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Load dataset
df = pd.read_csv("data.csv")

# Display basic info
print(df.info())
print(df.head())

# Step 2: Preprocessing the Data
# Encode categorical column (e.g., Zone)
le = LabelEncoder()
df['Zone_encoded'] = le.fit_transform(df['Zone'])

# Select features for clustering (Geographic Clustering Example: Zone + Google Reviews)
X_geo = df[['Zone_encoded', 'Number of google review in lakhs']].copy()

# Standardize the data
scaler = StandardScaler()
X_geo_scaled = scaler.fit_transform(X_geo)

#Step 3: Finding Optimal Clusters for K-Means
# Elbow Method to determine optimal K
inertia = []
K_range = range(1, 11)
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_geo_scaled)
    inertia.append(kmeans.inertia_)

# Plot Elbow Graph
#Step 3: Finding Optimal Clusters for K-Means
# Elbow Method to determine optimal K
inertia = []
K_range = range(1, 11)
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_geo_scaled)
    inertia.append(kmeans.inertia_)

# Plot Elbow Graph
plt.figure(figsize=(8, 5))
plt.plot(K_range, inertia, marker='o', linestyle='--', color='b')
plt.xlabel('Inertia (WCSS)')
plt.ylabel('Number of Clusters (K)')
#plt.xlabel('Number of Clusters (K)')
#plt.ylabel('Inertia (WCSS)')
plt.title('Elbow Method for Optimal K (Geographic Clustering)')
plt.show()
#plt.ylabel('Inertia (WCSS)')
plt.title('Elbow Method for Optimal K (Geographic Clustering)')
plt.show()

#Step 4: Apply K-Means Clustering
# Apply K-Means with optimal K (choose based on Elbow graph)
optimal_k = 3  # Adjust based on elbow method result
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df['Geo_Cluster'] = kmeans.fit_predict(X_geo_scaled)

# Scatter plot of clusters
plt.figure(figsize=(8, 6))
# The column name in the original dataframe is 'Number of google review in lakhs'
# Updated the column name to reflect the actual column name in the dataframe
sns.scatterplot(x=df['Zone_encoded'], y=df['Number of google review in lakhs'],
                hue=df['Geo_Cluster'], palette='viridis', s=100)
plt.xlabel("Number of Google Reviews (Lakhs)")
plt.ylabel("Zone (Encoded)")
#plt.xlabel("Zone (Encoded)")
#plt.ylabel("Number of Google Reviews (Lakhs)")
plt.title("Geographic Clustering (K-Means)")
plt.show()

#Step 5: Apply Hierarchical Clustering
# Perform Hierarchical Clustering
linked = linkage(X_geo_scaled, method='ward')

# Plot the dendrogram
plt.figure(figsize=(10, 5))
dendrogram(linked, orientation='top', distance_sort='ascending', show_leaf_counts=True)
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Tourist Places")
plt.ylabel("Distance")
plt.show()

#Step 6: Assign Clusters from Hierarchical Clustering
# Apply Agglomerative Clustering
# Removed affinity='euclidean' as it's implied with linkage='ward'
hierarchical = AgglomerativeClustering(n_clusters=optimal_k, linkage='ward')
df['Hierarchical_Cluster'] = hierarchical.fit_predict(X_geo_scaled)

# Scatter plot for Hierarchical Clustering
plt.figure(figsize=(8, 6))
# The original column name in the dataframe is 'Number of google review in lakhs'
# Updated column name in the scatterplot function to match the actual column name
sns.scatterplot(x=df['Zone_encoded'], y=df['Number of google review in lakhs'],
                hue=df['Hierarchical_Cluster'], palette='coolwarm', s=100)
plt.xlabel("Number of Google Reviews (Lakhs)")
plt.ylabel("Zone (Encoded)")
#plt.xlabel("Zone (Encoded)")
#plt.ylabel("Number of Google Reviews (Lakhs)")
plt.title("Geographic Clustering (Hierarchical)")
plt.show()
