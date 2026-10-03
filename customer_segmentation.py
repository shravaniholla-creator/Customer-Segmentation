import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Step 1: Load the dataset
data = pd.read_csv("customers.csv")

# Display first 5 customers
print("First 5 Customers:")
print(data.head())

# Display information about the dataset
print("\nDataset Information:")
print(data.info())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Display basic statistics
print("\nBasic Statistics:")
print(data.describe())
# Step 2: Select features for clustering
features = data[
    ["Age", "AnnualIncome", "SpendingScore", "PurchaseFrequency", "TotalPurchaseAmount"]
]

# Step 3: Scale the data
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Step 4: Find the best number of clusters using the Elbow Method
inertia = []

for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

# Step 5: Plot the Elbow graph
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), inertia, marker="o")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.title("Elbow Method for Optimal Number of Clusters")
plt.grid(True)
plt.show()
# Step 6: Apply K-Means clustering with 4 clusters
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)

data["Cluster"] = kmeans.fit_predict(scaled_features)

# Display the clusters
print("\nCustomer Clusters:")
print(data[[
    "CustomerID",
    "AnnualIncome",
    "SpendingScore",
    "PurchaseFrequency",
    "Cluster"
]])
# Step 7: Analyze each customer segment

cluster_summary = data.groupby("Cluster")[
    ["Age", "AnnualIncome", "SpendingScore",
     "PurchaseFrequency", "TotalPurchaseAmount"]
].mean()

print("\nCustomer Segment Summary:")
print(cluster_summary.round(2))
# Step 8: Visualize customer segments

plt.figure(figsize=(9, 6))

sns.scatterplot(
    data=data,
    x="AnnualIncome",
    y="SpendingScore",
    hue="Cluster",
    palette="viridis",
    s=100
)

plt.title("Customer Segmentation")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.legend(title="Cluster")
plt.grid(True)

plt.savefig("customer_segments.png")
plt.show()
# Step 9: Display detailed information about each cluster

for cluster in sorted(data["Cluster"].unique()):
    print(f"\nCluster {cluster}:")

    cluster_data = data[data["Cluster"] == cluster]

    print("Number of Customers:", len(cluster_data))
    print("Average Age:", round(cluster_data["Age"].mean(), 2))
    print("Average Income:", round(cluster_data["AnnualIncome"].mean(), 2))
    print("Average Spending Score:", round(cluster_data["SpendingScore"].mean(), 2))
    print("Average Purchase Frequency:",
          round(cluster_data["PurchaseFrequency"].mean(), 2))
    print("Average Purchase Amount:",
          round(cluster_data["TotalPurchaseAmount"].mean(), 2))
# Step 10: Number of customers in each cluster

cluster_counts = data["Cluster"].value_counts().sort_index()

plt.figure(figsize=(8, 5))

cluster_counts.plot(kind="bar")

plt.title("Number of Customers in Each Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.grid(axis="y")

plt.savefig("cluster_distribution.png")
plt.show()

# Step 11: Customer Segment Interpretation

print("\n========== CUSTOMER SEGMENT INSIGHTS ==========")

for cluster in sorted(data["Cluster"].unique()):

    cluster_data = data[data["Cluster"] == cluster]

    avg_income = cluster_data["AnnualIncome"].mean()
    avg_spending = cluster_data["SpendingScore"].mean()
    avg_frequency = cluster_data["PurchaseFrequency"].mean()

    print(f"\nCluster {cluster}")
    print(f"Average Income: ₹{avg_income:.2f}")
    print(f"Average Spending Score: {avg_spending:.2f}")
    print(f"Average Purchase Frequency: {avg_frequency:.2f}")

    if avg_spending >= 70 and avg_frequency >= 15:
        print("Insight: Highly Engaged Customers")

    elif avg_spending >= 50:
        print("Insight: Regular Customers")

    elif avg_income >= 60000:
        print("Insight: High Income but Lower Spending Customers")

    else:
        print("Insight: Low Engagement Customers")
        