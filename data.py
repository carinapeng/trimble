
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
data.columns=['x','y']

mean = data['y'].mean()
mode = data['y'].mode()
median = data['y'].median()

# Plot histogram to show distribution
data.hist(column='y')
plt.show()

# Show quantile
print(data.quantile([.1,.25,.5,.75],axis=0,interpolation='linear'))
