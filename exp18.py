mport matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()

# Sepal length is the first column in the data
sepal_length = iris.data[:, 0]

# Plot histogram
plt.hist(sepal_length, bins=10, edgecolor='black')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Histogram of Sepal Length in Iris Dataset')
plt.show()
