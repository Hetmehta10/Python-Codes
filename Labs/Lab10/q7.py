# Create a program to emonstrate different visual forms using Matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for demonstration
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Line plot
plt.figure()
plt.plot(x, y)
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Scatter plot
plt.figure()
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Bar plot
x_bar = ['A', 'B', 'C', 'D', 'E']
y_bar = [10, 20, 15, 25, 30]
plt.figure()
plt.bar(x_bar, y_bar)
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')

# Histogram
data = np.random.normal(0, 1, 10)
plt.figure()
plt.hist(data, edgecolor='black')
plt.title('Histogram')
plt.xlabel('Values')
plt.ylabel('Frequency')

# Pie chart
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
plt.figure()
plt.pie(sizes, labels=labels)
plt.title('Pie Chart')

# Show plots
plt.show()