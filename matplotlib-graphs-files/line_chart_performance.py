import pandas
import matplotlib.pyplot as plt
import os

cur_path = os.path.dirname(__file__)

# create a sample pandas dataframe
df = pandas.read_csv(cur_path + '/datasets/results/bayes_predicted_results.csv')

# Calculate the points for each team
home_points = df.groupby('HomeTeam')['FTR'].apply(lambda x: (x == 'H').sum() * 3 + (x == 'D').sum()).reset_index()
away_points = df.groupby('AwayTeam')['FTR'].apply(lambda x: (x == 'A').sum() * 3 + (x == 'D').sum()).reset_index()

# Merge the home and away points into a single dataframe
home_points.rename(columns={'HomeTeam': 'Team', 'FTR': 'Points'}), 
away_points.rename(columns={'AwayTeam': 'Team', 'FTR': 'Points'})

# Create a scatter plot of the points
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(home_points['FTR'], home_points['HomeTeam'], c='r', label='Home Points')
ax.scatter(away_points['FTR'], away_points['AwayTeam'], c='b', label='Away Points')


# Set the chart title and axis labels
ax.set_title('Football Results')
ax.set_xlabel('Points')
ax.set_ylabel('Team')
ax.legend()
# Show the chart
plt.show()




