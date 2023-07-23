import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('house_data.csv')
x = data['square_feet'].values
y = data['price'].values

# Calculate the means of x and y
x_mean = np.mean(x)
y_mean = np.mean(y)

# Calculate the slope and y-intercept using the least squares method
numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)
b1 = numerator / denominator
b0 = y_mean - b1 * x_mean

# Print the equation of the line
print(f"The equation of the line is y = {b0:.2f} + {b1:.2f}x")

# Plot the data and the line of best fit
plt.scatter(x, y)
plt.plot(x, b0 + b1 * x, color='red')
plt.xlabel('Square Footage')
plt.ylabel('Price')
plt.show()

# Predict the price of a house with a square footage of 2000
new_x = float(input("Enter the Square Footage: "))
new_y = b0 + b1 * new_x
print(f"The predicted price of a house with a square footage is {new_y:.2f}")