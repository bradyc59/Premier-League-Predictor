import pandas
import matplotlib.pyplot as plt
import os

cur_path = os.path.dirname(__file__)

# create a sample pandas dataframe
data = pandas.read_csv(cur_path + '/datasets/results/predicted_reuslts.csv')


# count the number of home wins, away wins, and draws
counts = data['FTR'].value_counts()

# create a bar chart
fig, ax = plt.subplots()
ax.bar(counts.index, counts.values)
ax.set_title('Results')
ax.set_xlabel('Result')
ax.set_ylabel('Number of Games')

plt.show()