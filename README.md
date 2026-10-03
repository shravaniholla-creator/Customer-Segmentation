# Customer Segmentation using K-Means Clustering

## 📌 Project Overview

Customer Segmentation is a data analysis and machine learning project that groups customers based on their behavior and demographic information.

This project uses **K-Means Clustering** to identify different customer groups based on factors such as age, annual income, spending score, purchase frequency, and total purchase amount.

## 🎯 Objective

The main objectives of this project are:

* Analyze customer demographic and purchasing data.
* Group customers into meaningful segments.
* Identify customer spending patterns.
* Understand purchasing behavior.
* Generate visual insights that can help businesses make better marketing decisions.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn

## 📊 Dataset

The dataset contains customer information including:

* Customer ID
* Age
* Gender
* Annual Income
* Spending Score
* Purchase Frequency
* Total Purchase Amount

## ⚙️ Methodology

### 1. Data Loading

The customer dataset is loaded using Pandas.

### 2. Data Exploration

The dataset is checked for:

* Missing values
* Basic statistics
* Dataset structure
* Customer information

### 3. Feature Selection

The following features are used for clustering:

* Age
* Annual Income
* Spending Score
* Purchase Frequency
* Total Purchase Amount

### 4. Feature Scaling

`StandardScaler` is used to scale the numerical features so that features with larger values do not dominate the clustering process.

### 5. Finding the Number of Clusters

The **Elbow Method** is used to analyze different numbers of clusters.

### 6. K-Means Clustering

The K-Means algorithm is used to divide customers into **4 clusters**.

### 7. Visualization

The results are visualized using:

* Customer segmentation scatter plot
* Cluster distribution bar chart

## 📈 Project Output

The project generates two main visualizations:

### Customer Segmentation

The scatter plot shows customers based on annual income and spending score, with different colors representing different clusters.

### Cluster Distribution

The bar chart shows the number of customers belonging to each cluster.

## 💡 Key Insights

The segmentation helps identify groups of customers with different:

* Income levels
* Spending behavior
* Purchase frequency
* Purchasing patterns

These insights can help businesses understand their customers and plan targeted marketing strategies.

## 🚀 How to Run the Project

### Step 1: Clone or download the project

Download this repository to your computer.

### Step 2: Open the project folder

Open the `Customer-Segmentation` folder in VS Code.

### Step 3: Install required libraries

Open the terminal and run:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Python program

```bash
python customer_segmentation.py
```

The program will perform the clustering analysis and generate the visualization files.

## 📁 Project Structure

```text
Customer-Segmentation/
│
├── customer_segmentation.py
├── customers.csv
├── customer_segments.png
├── cluster_distribution.png
├── requirements.txt
└── README.md
```

## 🔮 Future Enhancements

* Add a larger real-world customer dataset.
* Create an interactive dashboard using Power BI or Streamlit.
* Compare different clustering algorithms.
* Add customer recommendations based on segments.
* Use additional customer behavior features.

## 👩‍💻 Author

**Shravani Holla**

Computer Science Engineering Student
