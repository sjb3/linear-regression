# funny thing at csv file hence import re was used(?)

import re
import numpy as np
import matplotlib.pyplot as plt

X = []
Y = []

# use regex to elimiate non decimal characters
non_deciomal = re.compile(r'[^\d]+')

for line in open('moore.csv'):
  r = line.split('\t')

  x = int(non_deciomal.sub('', r[2].split('[')[0])) # third column
  y = int(non_deciomal.sub('', r[1].split('[')[0])) # second column

  X.append(x)
  Y.append(y)

X = np.array(X)
Y = np.array(Y)

plt.scatter(X, Y)
plt.show()

Y = np.log(Y)
plt.scatter(X, Y)
plt.show()

# solutions for Linea Regression
denominator = X.dot(X) - X.mean() * X.sum()
a = ( X.dot(Y) - Y.mean() * X.sum()) / denominator
b = ( Y.mean() * X.dot(X) - X.mean() * X.dot(Y)) / denominator

Yhat = a*X + b

plt.scatter(X, Y)
plt.plot(X, Yhat)
plt.show()

d1 = Y - Yhat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d1) / d2.dot(d2)

print("a: ", a, "b: ", b)
print("The r-squared is: ", r2)

# log(tc) = a*year + b
# tc = exp(b) * exp(a * year)
# 2*tc = exp(ln(2)) * exp(b) * exp(a * year) = exp(b) * exp(a*year + ln(2))

# exp(b)*exp(a*year2) = exp(b)*exp(a*year1 + ln2)
# a*year2 = a*year1 + ln2
# year2 = year1 + ln2/a

print("Time to double: ", np.log(2)/a)