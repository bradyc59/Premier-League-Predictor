import csv
import operator
import pandas
import os
import numpy

cur_path = os.path.dirname(__file__)


bayes_teams = {
    'Arsenal': 0,
    'Aston Villa': 0,
    'Brentford': 0,
    'Brighton': 0,
    'Burnley': 0,
    'Chelsea': 0,
    'Crystal Palace': 0,
    'Everton': 0,
    'Leeds': 0,
    'Leicester': 0,
    'Liverpool': 0,
    'Man City': 0,
    'Man United': 0,
    'Newcastle': 0,
    'Norwich': 0,
    'Southampton': 0,
    'Tottenham': 0,
    'Watford': 0,
    'West Ham': 0,
    'Wolves': 0
}

knn_teams = {
    'Arsenal': 0,
    'Aston Villa': 0,
    'Brentford': 0,
    'Brighton': 0,
    'Burnley': 0,
    'Chelsea': 0,
    'Crystal Palace': 0,
    'Everton': 0,
    'Leeds': 0,
    'Leicester': 0,
    'Liverpool': 0,
    'Man City': 0,
    'Man United': 0,
    'Newcastle': 0,
    'Norwich': 0,
    'Southampton': 0,
    'Tottenham': 0,
    'Watford': 0,
    'West Ham': 0,
    'Wolves': 0
}


def bayes_add_points_to_teams(results):
    for index, row in results.iterrows():
        if row['FTR'] == 'H':
            home_team = row['HomeTeam']
            bayes_teams[home_team] += 3
        if row['FTR'] == 'A':
            away_team = row['AwayTeam']
            bayes_teams[away_team] += 3
        if row['FTR'] == 'D':
            home_team = row['HomeTeam']
            bayes_teams[home_team] += 1
            away_team = row['AwayTeam']
            bayes_teams[away_team] += 1
    return bayes_teams

def knn_add_points_to_teams(results):
    for index, row in results.iterrows():
        if row['FTR'] == 'H':
            home_team = row['HomeTeam']
            knn_teams[home_team] += 3
        if row['FTR'] == 'A':
            away_team = row['AwayTeam']
            knn_teams[away_team] += 3
        if row['FTR'] == 'D':
            home_team = row['HomeTeam']
            knn_teams[home_team] += 1
            away_team = row['AwayTeam']
            knn_teams[away_team] += 1
    return knn_teams

def tiebreaker(teams, results_dataset, sorted_d):
    equal_team = {teams[0] : 0, teams[1]: 0}
    matches = results_dataset[((results_dataset['HomeTeam'] == teams[0]) & (results_dataset['AwayTeam'] == teams[1])) 
                                    | ((results_dataset['HomeTeam'] == teams[1]) & (results_dataset['AwayTeam'] == teams[0]))]
    for index, row in matches.iterrows():
        if row['FTR'] == 'H':
            home_team = row['HomeTeam']
            equal_team[home_team] += 3
        if row['FTR'] == 'A':
            away_team = row['AwayTeam']
            equal_team[away_team] += 3
        if row['FTR'] == 'D':
            home_team = row['HomeTeam']
            equal_team[home_team] += 1
            away_team = row['AwayTeam']
            equal_team[away_team] += 1

    if len(set(equal_team.values())) == 1:
        i = 0
        epl_standings = pandas.read_csv(
        cur_path + '/datasets/epl_standings/EPLStandings.csv')
        avg_dict = {}
        avg_last_three = epl_standings[['2019', '2020', '2021']].mean(axis=1)
        first_column = epl_standings['Team']
        while i < len(avg_last_three):
            for team in first_column:
                avg_dict[team] = avg_last_three[i]
                i += 1 

        for key, value in avg_dict.items():
            # If the current key is the first team in the list, set team_1_pos to its value
            if key == teams[0]:
                team_1_pos = value
            # If the current key is the second team in the list, set team_2_pos to its value
            if key == teams[1]:
                team_2_pos = value

        if team_1_pos > team_2_pos:
            keys = list(sorted_d.keys())
            values = list(sorted_d.values())
            index = keys.index(teams[1])
            # Reorder the lists of keys and values so that the second team is placed before the first team
            new_keys = keys[:index-1] + [keys[index], keys[index-1]] + keys[index+1:]
            new_values = values[:index-1] + [values[index], values[index-1]] + values[index+1:]
            sorted_d = dict(zip(new_keys, new_values))

        if equal_team[teams[1]] > equal_team[teams[0]]:
            keys = list(sorted_d.keys())
            values = list(sorted_d.values())
            index = keys.index(teams[1])
            # Reorder the lists of keys and values so that the second team is placed before the first team
            new_keys = keys[:index-1] + [keys[index], keys[index-1]] + keys[index+1:]
            new_values = values[:index-1] + [values[index], values[index-1]] + values[index+1:]
            sorted_d = dict(zip(new_keys, new_values))

    return sorted_d           

def main():
    knn_results_dataset = pandas.read_csv(cur_path + '/datasets/results/predicted_reuslts.csv')
    bayes_results_dataset = pandas.read_csv(
        cur_path + '/datasets/results/bayes_predicted_results.csv')

    bayes_results_dataset = bayes_results_dataset.loc[:, ~
                                                bayes_results_dataset.columns.str.contains('^Unnamed')]
    knn_results_dataset = knn_results_dataset.loc[:, ~
                                                knn_results_dataset.columns.str.contains('^Unnamed')]
    bayes_team_points = bayes_add_points_to_teams(bayes_results_dataset)
    knn_team_points = knn_add_points_to_teams(knn_results_dataset)

    bayes_sorted_d = dict(sorted(bayes_team_points.items(),
                    key=operator.itemgetter(1), reverse=True))
    knn_sorted_d = dict(sorted(knn_team_points.items(),
                    key=operator.itemgetter(1), reverse=True))

    bayes_equal_teams = {}
    knn_equal_teams = {}


    for team, points in bayes_sorted_d.items():
        if points in bayes_equal_teams:
            bayes_equal_teams[points].append(team)
        else:
            bayes_equal_teams[points] = [team]
    
    for team, points in knn_sorted_d.items():
        if points in knn_equal_teams:
            knn_equal_teams[points].append(team)
        else:
            knn_equal_teams[points] = [team]
    
    for points, teams in bayes_equal_teams.items():
        if len(teams) > 1:
            bayes_sorted_d = tiebreaker(teams, bayes_results_dataset, bayes_sorted_d)
    for points, teams in knn_equal_teams.items():
        if len(teams) > 1:
            knn_sorted_d = tiebreaker(teams, knn_results_dataset, knn_sorted_d)

    with open(cur_path + '/datasets/tables/knn_table.txt', 'w') as f:
        for key, value in knn_sorted_d.items():
            f.write('%s:%s\n' % (key, value))
    with open(cur_path + '/datasets/tables/bayes_table.txt', 'w') as f:
        for key, value in bayes_sorted_d.items():
            f.write('%s:%s\n' % (key, value))
    i = 1
    with open(cur_path + '/datasets/tables/bayes_position_table.txt', 'w') as f:
        for key, value in bayes_sorted_d.items():
            f.write('%s:%s\n' % (key, i))
            i += 1
    j = 1
    with open(cur_path + '/datasets/tables/knn_position_table.txt', 'w') as f:
        for key, value in knn_sorted_d.items():
            f.write('%s:%s\n' % (key, j))
            j += 1
if __name__ == "__main__":
    main()
