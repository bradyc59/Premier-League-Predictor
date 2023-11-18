import pandas
import matplotlib.pyplot as plt
import os

cur_path = os.path.dirname(__file__)

# create a sample pandas dataframe
df = pandas.read_csv(cur_path + '/datasets/train/20-21.csv')
# Group the DataFrame by home team and away team and calculate the sum of home goals and away goals
home_conceded = df.groupby('HomeTeam')['FTAG'].sum().reset_index()
away_conceded = df.groupby('AwayTeam')['FTHG'].sum().reset_index()


# Merge the home conceded and away conceded DataFrames
conceded = pandas.merge(home_conceded, away_conceded, left_on='HomeTeam', right_on='AwayTeam')
conceded = conceded[['HomeTeam', 'FTAG', 'FTHG']]
conceded.columns = ['Team', 'Goals Conceded at Home', 'Goals Conceded Away']

conceded.set_index('Team', inplace=True)

# Plot a bar chart of the goals and conceded
conceded.plot(kind='bar', figsize=(12,8))
plt.title('Premier League Goals Conceded 20-21')
plt.xlabel('Team')
plt.ylabel('Goals')
plt.show()