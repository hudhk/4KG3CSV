import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import plotly.express as px


data = pd.read_csv('aeromile_data.csv')

        # Extracting columns and data points for clustering

features = data[['Balance ', 'Qual_miles ', 'cc1_miles ', 'cc2_miles ',    'cc3_miles ', 'Bonus_miles ', 'Bonus_trans ', 'Flight_miles_12mo ', 'Flight_trans_12 ', 'Days_since_enroll ']]

        # Standardizing values for K-Means

scaler = StandardScaler
scaled_features = (features - features.mean()) / features.std()

        # Perform Heirarchical Clustering using Ward, Centroid, Average

methods = ['ward', 'centroid', 'average']
inertia_values = []

for method in methods:
            # Perform hierarchical clustering

    Z = linkage(scaled_features, method=method, metric='euclidean')

             # Calculate inertia for range of cluster nums

    inertia =[]
    for k in range (1, 11):
        cluster_labels = fcluster(Z, k, criterion='maxclust')
        cluster_centers = np.array([scaled_features[cluster_labels == i].mean(axis=0) for i in range (1, k + 1)])
        distance = np.sum((scaled_features - cluster_centers[cluster_labels - 1]) ** 2)
        inertia.append(distance)
    inertia_values.append(inertia)

         # Plot for Elbow Method Graph to Choose Optimal Num of Clusters

plt.figure(figsize=(12, 6))
for i, method in enumerate(methods):
    plt.subplot(1, len(methods), i + 1)
    plt.plot(range(1, 11), inertia_values[i], marker='o', linestyle='--')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia (Within-Cluster Sum of Squares)')
    plt.title(f'Elbow Method ({method} linkage)')
    plt.grid(True)

plt.tight_layout()
plt.show()

        # Performing hierarchical clustering using Ward Linkage

method = 'ward'
num_clusters = 4

Z = linkage(scaled_features, method=method, metric='euclidean')
cluster_labels = fcluster(Z, num_clusters, criterion='maxclust')
data['Cluster'] = cluster_labels

         # Data Visualization - Cluster Summaries

cluster_summary = data.groupby('Cluster').mean()
print("Cluster Summary (ward):")
print(cluster_summary)

         # Scatterplot Matrix Visualization

sns.set(style="ticks")
sns.pairplot(data, hue='Cluster', palette="husl", plot_kws={'alpha': 0.5})
plt.suptitle("Scatterplot Matrix (Ward 4C)", y = 1.02)
plt.show()

        # Parallel Coordinate Plots

fig = px.parallel_coordinates(data, dimensions=data.columns[1:-1], color="Cluster", color_continuous_scale=px.colors.qualitative.Set1)
fig.show()


        # Performing Hierarchical Clustering using Centroid Method

method = 'centroid'
num_clusters = 4

Z = linkage(scaled_features, method=method, metric='euclidean')
cluster_labels = fcluster(Z, num_clusters, criterion='maxclust')
data['Cluster'] = cluster_labels

cluster_summary = data.groupby('Cluster').mean()
print("Cluster Summary (centroid):")
print(cluster_summary)

sns.set(style="ticks")
sns.pairplot(data, hue='Cluster', palette="husl", plot_kws={'alpha': 0.5})
plt.suptitle("Scatterplot Matrix (Centroid 4C)", y = 1.02)
plt.show()
fig = px.parallel_coordinates(data, dimensions=data.columns[1:-1], color="Cluster", color_continuous_scale=px.colors.qualitative.Set1)
fig.show()

        # Performing Hierarchical Clustering using Average Method

method = 'average'
num_clusters = 4

Z = linkage(scaled_features, method=method, metric='euclidean')
cluster_labels = fcluster(Z, num_clusters, criterion = 'maxclust')
data['Cluster'] = cluster_labels

cluster_summary = data.groupby('Cluster').mean()
print("Cluster Summary (average):")
print(cluster_summary)

sns.set(style="ticks")
sns.pairplot(data, hue='Cluster', palette="husl", plot_kws={'alpha': 0.5})
plt.suptitle("Scatterplot Matrix (Average 4C)", y = 1.02)
plt.show()
fig = px.parallel_coordinates(data, dimensions=data.columns[1:-1], color="Cluster", color_continuous_scale=px.colors.qualitative.Set1)
fig.show()

        # Defining Cluster Range for K-Means Clustering

cluster_range = range(2, 11)

        # Initialize lists to store results
cluster_summaries = []
cluster_means = []
cluster_std_devs = []

for num_clusters in cluster_range:
            # Initialize and fit the K-Means model
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(scaled_features)

    data[f'Cluster_{num_clusters}'] = cluster_labels

            # Calculate cluster summaries, mean, and std. dev
    cluster_summary = data.groupby(f'Cluster_{num_clusters}').mean()
    cluster_mean = data.groupby(f'Cluster_{num_clusters}').mean().mean()
    cluster_std_dev = data.groupby(f'Cluster_{num_clusters}').std().mean()

    cluster_summaries.append(cluster_summary)
    cluster_means.append(cluster_mean)
    cluster_std_devs.append(cluster_std_dev)

for num_clusters, summary in zip(cluster_range, cluster_summaries):
    print(f"\nCluster Summary for {num_clusters} Clusters:")
    print(summary)

plt.figure(figsize=(12, 6))

plt.subplot(121)
plt.plot(cluster_range, [mean.mean() for mean in cluster_means], marker='o', linestyle='--')
plt.xlabel('Number of Clusters')
plt.ylabel('Mean of Cluster Means')
plt.title('Cluster means vs. Number of Clusters')

plt.subplot(122)
plt.plot(cluster_range, [std.mean() for std in cluster_std_devs], marker='o', linestyle='--')
plt.xlabel('Number of Clusters')
plt.ylabel('Means of Cluster Standard Deviations')
plt.title('Cluster Standard Deviations vs. Number of Clusters')

plt.tight_layout()
plt.show()