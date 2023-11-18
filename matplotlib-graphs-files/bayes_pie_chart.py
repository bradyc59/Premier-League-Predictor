import pandas
import matplotlib.pyplot as plt
import os

cur_path = os.path.dirname(__file__)

# create a sample pandas dataframe
data = pandas.read_csv(cur_path + '/datasets/results/bayes_predicted_results.csv')


# Calculate the number of wins, losses, and draws for all teams
wins = (data['FTR'] == 'H').sum()
losses = (data['FTR'] == 'A').sum()
draws = (data['FTR'] == 'D').sum()

# Plot a pie chart of the results
labels = ['Wins', 'Losses', 'Draws']
sizes = [wins, losses, draws]
colors = ['green', 'red', 'orange']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Premier League Results')
plt.show()