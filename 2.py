import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
dataset = pd.read_csv('HeightWeight.csv')
heights, weights = dataset['Height'].values, dataset['Weight'].values

# Calculate slope and intercept
slope = np.sum((heights - np.mean(heights)) * (weights - np.mean(weights))) / np.sum((heights - np.mean(heights)) ** 2)
intercept = np.mean(weights) - slope * np.mean(heights)

# Predict weight for user input height
user_height_inches = float(input("Enter the height in inches: "))
predicted_weight = slope * user_height_inches + intercept
print(f"Predicted weight for a height of {user_height_inches} inches: {predicted_weight:.2f} pounds")

# Plot
plt.scatter(heights, weights, color='black', label='Actual data')
plt.plot(heights, slope * heights + intercept, color='blue', linewidth=3, label='Regression line')
plt.scatter(user_height_inches, predicted_weight, color='red', marker='x', label='Predicted weight')
plt.xlabel('Height (inches)')
plt.ylabel('Weight (pounds)')
plt.title('Linear Regression: Height vs Weight')
plt.legend()
plt.show()