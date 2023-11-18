import operator
import sys
import os
import pytest
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import predict_table
import pandas

cur_path = os.path.dirname(__file__)

teams = {
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

bayes_results_dataset = pandas.read_csv(cur_path + '/../datasets/results/bayes_predicted_results.csv')

results_dataset = bayes_results_dataset.loc[:, ~bayes_results_dataset.columns.str.contains('^Unnamed')]

def test_bayes_add_points_to_teams():
    results = predict_table.bayes_add_points_to_teams(results_dataset)
    assert isinstance(results, dict)

def test_knn_add_points_to_teams():
    results = predict_table.knn_add_points_to_teams(results_dataset)
    assert isinstance(results, dict)

team_points = predict_table.bayes_add_points_to_teams(results_dataset)
sorted_d = dict(sorted(team_points.items(),
                    key=operator.itemgetter(1), reverse=True))

def test_tiebreaker():
    equal_teams = {107: ['Liverpool', 'Man City'], 43: ['Crystal Palace'], 42: ['Brighton', 'Wolves'], 41: ['Aston Villa', 'Leicester'], 17: ['Burnley'], 9: ['Norwich']}
    for points, teams in equal_teams.items():
        if len(teams) > 1:
            sorted = predict_table.tiebreaker(teams, bayes_results_dataset, sorted_d)
    assert isinstance(sorted, dict)

    with pytest.raises(TypeError):
        for teams, points in equal_teams.items():
            if len(teams) > 1:
                sorted = predict_table.tiebreaker(teams, bayes_results_dataset, sorted_d)
        assert isinstance(sorted, dict)