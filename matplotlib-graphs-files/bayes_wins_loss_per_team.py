import pandas
import matplotlib.pyplot as plt
import os

cur_path = os.path.dirname(__file__)

# create a sample pandas dataframe
df = pandas.read_csv(cur_path + '/datasets/results/bayes_predicted_results.csv')
# Create a new column called "Winner" based on the FTR column
df.loc[df['FTR'] == 'H', 'Winner'] = df['HomeTeam']
df.loc[df['FTR'] == 'A', 'Winner'] = df['AwayTeam']
df.loc[df['FTR'] == 'D', 'Winner'] = df['HomeTeam']
df.loc[df['FTR'] == 'D', 'Winner'] = df['AwayTeam']


# Group the DataFrame by "Winner" and "FTR" columns and count the number of wins for each team
win_counts = df.groupby(['Winner', 'FTR'])['Winner'].count()

# Unstack the "FTR" column to create separate columns for home wins, away wins, and draws
win_counts = win_counts.unstack(level=-1, fill_value=0)

# Plot a stacked bar chart of the win counts
win_counts.plot(kind='bar', stacked=True, figsize=(12,8))
plt.title('Bayes Premier League Wins/Draws')
plt.xlabel('Team')
plt.ylabel('Wins')
plt.show()