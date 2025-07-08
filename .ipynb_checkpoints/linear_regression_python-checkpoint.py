#!/usr/bin/env python3

import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Check command-line arguments
if len(sys.argv) != 4:
    print("Usage: python linear_regression_python.py <filename> <x_column> <y_column>")
    sys.exit(1)

filename = sys.argv[1]
x_col = sys.argv[2]
y_col = sys.argv[3]

# Load CSV data
data = pd.read_csv(filename)

# Fit the model
model = LinearRegression()
model.fit(data[[x_col]], data[[y_col]])

# Plot
plt.scatter(data[[x_col]], data[[y_col]], color='red', label='Data points')
plt.plot(data[[x_col]], model.predict(data[[x_col]]), color='blue', label='Regression line')
plt.title(f'{y_col} vs {x_col}')
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.savefig("linear_regression_output.png")  # Save to file
plt.show()
