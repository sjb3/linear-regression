import numpy as np
import matplotlib.pyplot as plt

# load data
X = []
Y = []

for line in open('data_poly.csv'):
  x, y = line.split(',')
  x = float(x)
  X.append([1, x, x*x])
  Y.append(float(y))

# convert to numpy array
X = np.array(X)
Y = np.array(Y)

# plot them
plt .scatter(X[:,1], Y)
plt.show()
