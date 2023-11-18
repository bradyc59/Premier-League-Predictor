import pandas
import matplotlib.pyplot as plt
import os

cur_path = os.path.dirname(__file__)

# create a sample pandas dataframe
df = pandas.read_csv(cur_path + '/datasets/train/20-21.csv')

# Group the DataFrame by home team and away team and calculate the sum of home goals and away goals
home_goals = df.groupby('HomeTeam')['FTHG'].sum().reset_index()
away_goals = df.groupby('AwayTeam')['FTAG'].sum().reset_index()

# Merge the home goals and away goals DataFrames
goals = pandas.merge(home_goals, away_goals, left_on='HomeTeam', right_on='AwayTeam')
goals = goals[['HomeTeam', 'FTHG', 'FTAG']]

# Set the team names as the index
goals.set_index('HomeTeam', inplace=True)

# Plot a bar chart of the home goals and away goals
goals.plot(kind='bar', figsize=(12,8))
plt.title('Premier League Goals 20-21')
plt.xlabel('Team')
plt.ylabel('Goals')
plt.show()