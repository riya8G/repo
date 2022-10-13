import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

salary_data = pd.read_csv('Salary_Data.csv')

x = salary_data.YearsExperience
y = salary_data.Salary

plt.scatter(x, y)
plt.show()

m = 0
c = 0

L = 0.0001

no_of_iter = 1000
n = float(len(x))

for i in range(no_of_iter):
    y_pred = m*x + c

    dm = (-2/n)*sum(x*(y-y_pred))
    dc = (-2/n)*sum((y-y_pred))

    m = m - L*dm
    c = c - L*dc

print(n)
print(m,c)

y_pred = m*x + c

x_values = np.linspace(min(x), max(x), int(n))
y_values = np.linspace(min(y), max(y), int(n))

plt.scatter(x, y)
plt.plot(x_values, y_values, color='red')
plt.show()
