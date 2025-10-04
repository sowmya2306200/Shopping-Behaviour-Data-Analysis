# Shopping Behaviour Data Analysis using python
 
#Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
#file_path = "shopping_behavior_updated.csv"   # Change path if needed
df = pd.read_csv("shopping_behavior_updated.csv")

# 2. Explore dataset
print("Shape of dataset:", df.shape)
print("\nFirst 5 rows:\n", df.head())
print("\nSummary:\n", df.describe(include='all'))

# 3. Add age groups
df['AgeGroup'] = pd.cut(df['Age'], bins=[0,18,30,50,70,100],
labels=['Teen','Young Adult','Adult','Middle Age','Senior'])

# -----------------------
# Analysis & Visualization
# -----------------------

# 4. Basic analysis
gender_counts = df['Gender'].value_counts()
age_group_counts = df['AgeGroup'].value_counts()
avg_purchase_gender = df.groupby('Gender')['Purchase Amount (USD)'].mean()

# --- Chart 1: Bar chart (Gender distribution)
plt.figure(figsize=(6,4))
gender_counts.plot(kind='bar', color=["#1fb447","#3e0eff"])  # blue & orange
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# --- Chart 2: Histogram (Purchase Amount distribution)
plt.figure(figsize=(6,4))
plt.hist(df['Purchase Amount (USD)'].dropna(), bins=20, 
color="#a02c5c", edgecolor='black', alpha=0.75)  # green with black edges
plt.title("Histogram of Purchase Amount")
plt.xlabel("Purchase Amount (USD)")
plt.ylabel("Frequency")
plt.show()

# --- Chart 3: Scatter Plot (Age vs Purchase Amount)
plt.figure(figsize=(6,4))
plt.scatter(df['Age'], df['Purchase Amount (USD)'], 
alpha=0.6, c=df['Age'], cmap='plasma')  # color varies by Age
plt.colorbar(label="Age")  # add color bar
plt.title("Age vs Purchase Amount")
plt.xlabel("Age")
plt.ylabel("Purchase Amount (USD)")
plt.show()

# ---Chart 4: Pie Chart:Shopping Category Distribution
category_counts = df['Category'].value_counts()
plt.figure(figsize=(7,7))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%',
colors=plt.cm.Set3.colors, startangle=90, shadow=True)
plt.title("Shopping Category Distribution (Pie Chart)")
plt.show()

# 5. NumPy stats
purchase_values = df['Purchase Amount (USD)'].dropna().values
print("\nNumPy Stats on Purchase Amount:")
print("Mean:", np.mean(purchase_values))
print("Median:", np.median(purchase_values))
print("Std Dev:", np.std(purchase_values))
