import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Import Sklearn Library(for ML)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

#Load the dataset from csv file
data = pd.read_csv("E:\AQI.csv")
print(data)

#Display concise summary of the data
print("\nDataFrame Info: ")
print(data.info())

#Display discriptive statistics to understand the data
print("\nSummary Statistics:\n", data.describe())

#Display top and bottom row of the datset for initial glance
print(data.head())
print(data.tail())

#Identify the NAs or null values in the data
print(data.isna().sum())

#Handles NA's in the data
data["pollutant_min"].fillna(data["pollutant_min"].mean(), inplace=True)
data["pollutant_max"].fillna(data["pollutant_max"].mean(), inplace=True)
data["pollutant_avg"].fillna(data["pollutant_avg"].mean(), inplace=True)
print(data.info())

# ---------------- Objective 1 ----------------
# Find average pollutant level per state

state_pollution = data.groupby("state")["pollutant_avg"].mean().sort_values()
print(state_pollution)

# Bar Chart
plt.figure(figsize=(12,6))
state_pollution.tail(10).plot(kind='bar', color='skyblue')
plt.title("Top 10 States with Highest Average Pollution")
plt.xlabel("State")
plt.ylabel("Pollutant Avg")
plt.xticks(rotation=45)
plt.show()

# ---------------- Objective 2 ----------------
#Identify the top cities with the highest average pollution levels

city_pollution = data.groupby("city")["pollutant_avg"].mean().sort_values()
print(city_pollution)

#Bar Chart
plt.figure(figsize=(12,6))
city_pollution.tail(10).plot(kind='bar', color='khaki')
plt.title("Top 10 Most Polluted Cities")
plt.xlabel("City")
plt.ylabel("Pollution Level")
plt.xticks(rotation=45)
plt.show()

# ---------------- Objective 3 ----------------
# Visualize the distribution of pollution levels across all regions

plt.figure(figsize=(12,6))
sns.histplot(data["pollutant_avg"], bins=20, kde=True, color="purple")
plt.xlabel("Pollutant Average Level")
plt.ylabel("Frequency")
plt.title("Distribution of Pollution Levels Across Regions")
plt.show()

# ---------------- Objective 4 ----------------
# Analyze the relationship between minimum and maximum pollution levels

plt.figure(figsize=(12,6))
plt.scatter(data["pollutant_min"], data["pollutant_max"], color="green")
plt.xlabel("Minimum Pollution Level")
plt.ylabel("Maximum Pollution Level")
plt.title("Relationship Between Minimum and Maximum Pollution Levels")
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------------- Objective 5 ----------------
#Correlation heatmap between different pollution parameters

plt.figure(figsize=(12,6))
sns.heatmap(data[["pollutant_min","pollutant_max","pollutant_avg"]].corr(),
            annot=True, cmap="coolwarm")
plt.title("Correlation Between Pollution Parameters")
plt.show()

# ---------------- Objective 6 ----------------
# Detect outliers in pollution data

plt.figure(figsize=(12,6))
sns.boxplot(data=data[["pollutant_min","pollutant_max","pollutant_avg"]])
plt.xlabel("Pollution Parameters")
plt.ylabel("Values")
plt.title("Outlier Detection in Pollution Data")
plt.show()

# ---------------- Outlier Removal (Fixed) ----------------

cols = ['pollutant_min','pollutant_max','pollutant_avg']
condition = pd.Series(True, index=data.index)

for col in cols:
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    condition &= (data[col] >= lower) & (data[col] <= upper)

# Apply filter
data = data[condition]
print("Outliers removed correctly from all columns")

# ---------------- Objective 6 (After) ----------------
# Visualize data after removing outliers

plt.figure(figsize=(12,6))
sns.boxplot(data=data[["pollutant_min","pollutant_max","pollutant_avg"]])
plt.xlabel("Pollution Parameters")
plt.ylabel("Values")
plt.title("Outlier Detection After Removing Outliers")
plt.show()

# ---------------- Objective 7 ----------------
# Compare pollution levels across different pollutant types
#Bar Chart

plt.figure(figsize=(10,6))
avg_values = data[['pollutant_min','pollutant_max','pollutant_avg']].mean()
avg_values.plot(kind='bar', color=['#ff9999','#66b3ff','#99ff99'])
plt.xlabel("Pollutant Type")
plt.ylabel("Average Value")
plt.title("Average Pollution Levels Comparison")
plt.xticks(rotation=0)
plt.show()

# ---------------- Normalization ----------------
# Scaling the features so that all values are in the same range (0 to 1)

scaler = MinMaxScaler()
data[['pollutant_min', 'pollutant_max']] = scaler.fit_transform(data[['pollutant_min', 'pollutant_max']])

print("\nAfter Normalization:")
print(data[['pollutant_min', 'pollutant_max']].describe())

# ---------------- Scatter Plot ----------------
# Visualizing relationship between pollutant_min and pollutant_avg

plt.figure(figsize=(8,4))
plt.scatter(data['pollutant_min'], data['pollutant_avg'])
plt.title('Scatter Plot of Min Pollution vs Average Pollution')
plt.xlabel('Pollutant Min (Normalized)')
plt.ylabel('Pollutant Avg')
plt.grid(True)
plt.show()

# ---------------- Linear Regression Model ----------------
# Using pollutant_min and pollutant_max to predict pollutant_avg

x = data[['pollutant_min','pollutant_max']]
y = data[['pollutant_avg']]

# Splitting data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=34)

#Training the model
model = LinearRegression()
model.fit(x_train, y_train)

# ---------------- Prediction ----------------
# Predicting for a sample value
sample = pd.DataFrame({'pollutant_min': [0.5], 'pollutant_max': [0.7]})
result = model.predict(sample)
print("Predicted Pollution Level:", result)

# ---------------- Model Evaluation ----------------
# Checking model performance
y_pred = model.predict(x_test)

# ---------------- Model Visualization ----------------
# Visualizing Actual vs Predicted values
plt.figure(figsize=(8,5))
plt.scatter(y_test, y_pred, color='blue')
# Perfect prediction line
plt.plot([y_test.min(), y_test.max()],[y_test.min(), y_test.max()],color='red', linewidth=2)
plt.xlabel('Actual Pollution Values')
plt.ylabel('Predicted Pollution Values')
plt.title('Actual vs Predicted (Linear Regression)')
plt.show()

# Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE): {mse:.4f}")

# R-Square Score (Goodness of Fit)
r2 = r2_score(y_test, y_pred)
print(f"R-Square Score: {r2:.4f}")

# Mean Absolute Error
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error (MAE): {mae:.4f}")
