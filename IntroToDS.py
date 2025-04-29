

print("Welcome to the Intro to Data Science project!")

# Create a basic structure for a Python project

#main.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample data
data = {'Year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020], 
 'Sales': [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]}
df = pd.DataFrame(data)

# Preparing the data
X = df[['Year']]
y = df['Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predicting and plotting
y_pred = model.predict(X_test)
print("X_test:\n", X_test)
print("y_test:\n", y_test)
print("y_pred:\n", y_pred) 
print("Model Coefficients:\n", model.coef_)
print("Model Intercept:\n", model.intercept_)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.scatter(X_train, y_train, color='green')
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales Forecast')
plt.legend(['Predicted', 'Test Data', 'Train Data'])
plt.grid()
plt.savefig('sales_forecast.png')  # Save the plot as a PNG file
plt.show()  # Display the plot
       

