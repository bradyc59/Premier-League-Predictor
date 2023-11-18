# from ...src.cleaning_data import get_goals_scored
import sys
import os

import pytest
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import cleaning_data
import pandas

cur_path = os.path.dirname(__file__)

dataset8 = pandas.read_csv(cur_path + '/../datasets/train/12-13.csv')
required_columns = ['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HF', 'AF', 'HS', 'AS', 'HST', 'AST', 'HY','AY','HR','AR', 'HC', 'AC']
playing_stat = dataset8[required_columns]   
def test_get_goals_scored():
    # Call the get_goals_scored function with the sample playing_stat dataframe
    goals_scored = cleaning_data.get_goals_scored(playing_stat)

    # Check that the output is a pandas DataFrame
    assert isinstance(goals_scored, pandas.DataFrame)

def test_get_goals_conceded():
    goals_conceded = cleaning_data.get_goals_conceded(playing_stat)

    assert isinstance(goals_conceded, pandas.DataFrame)

def test_get_goal_stats():
    goals_stats = cleaning_data.get_goal_stats(playing_stat)

    assert isinstance(goals_stats, pandas.DataFrame)

def test_get_match_points():
    win = cleaning_data.get_match_points("W")
    assert win == 3
    draw = cleaning_data.get_match_points("D")
    assert draw == 1
    loss = cleaning_data.get_match_points("L")
    assert loss == 0

def test_get_all_matches():
    get_all_matches = cleaning_data.get_all_matches(playing_stat)

    assert isinstance(get_all_matches, pandas.DataFrame)

def test_aggregate_match_points():
    aggregate_match_points = cleaning_data.aggregate_match_points(playing_stat)

    assert isinstance(aggregate_match_points, pandas.DataFrame)

def test_get_team_form():
    get_team_form_1 = cleaning_data.get_team_form(playing_stat, 1)
    assert isinstance(get_team_form_1, pandas.DataFrame)
    get_team_form_2 = cleaning_data.get_team_form(playing_stat, 2)
    assert isinstance(get_team_form_2, pandas.DataFrame)
    get_team_form_3 = cleaning_data.get_team_form(playing_stat, 3)
    assert isinstance(get_team_form_3, pandas.DataFrame)
    get_team_form_4 = cleaning_data.get_team_form(playing_stat, 4)
    assert isinstance(get_team_form_4, pandas.DataFrame)
    get_team_form_5 = cleaning_data.get_team_form(playing_stat, 5)
    assert isinstance(get_team_form_5, pandas.DataFrame)

def test_add_form():
    add_form_1 = cleaning_data.add_form(playing_stat, 1)
    assert isinstance(add_form_1, pandas.DataFrame)
    add_form_2 = cleaning_data.add_form(playing_stat, 2)
    assert isinstance(add_form_2, pandas.DataFrame)
    add_form_3 = cleaning_data.add_form(playing_stat, 3)
    assert isinstance(add_form_3, pandas.DataFrame)
    add_form_4 = cleaning_data.add_form(playing_stat, 4)
    assert isinstance(add_form_4, pandas.DataFrame)
    add_form_5 = cleaning_data.add_form(playing_stat, 5)
    assert isinstance(add_form_5, pandas.DataFrame)

def test_add_form_difference():
    add_form_difference = cleaning_data.add_form_difference(playing_stat)

    assert isinstance(add_form_difference, pandas.DataFrame)

league_standings = pandas.read_csv(cur_path + "/../datasets/epl_standings/EPLStandings.csv")
league_standings.set_index(['Team'], inplace=True)

def test_get_team_last_year_standing():
    get_team_last_year_standing = cleaning_data.get_team_last_year_standing(playing_stat, league_standings, 7)

    assert isinstance(get_team_last_year_standing, pandas.DataFrame)

def test_get_matchweek():
    get_matchweek = cleaning_data.get_matchweek(playing_stat)

    assert isinstance(get_matchweek, pandas.DataFrame)

def test_add_streak_columns():
    with pytest.raises(KeyError):
        home_add_streak_columns_W3 = cleaning_data.add_streak_columns(playing_stat, 'HTFormPtsStr', 'W', 3)
        assert isinstance(home_add_streak_columns_W3, pandas.DataFrame)
        home_add_streak_columns_W5 = cleaning_data.add_streak_columns(playing_stat, 'HTFormPtsStr', 'W', 5)
        assert isinstance(home_add_streak_columns_W5, pandas.DataFrame)
        home_add_streak_columns_L3 = cleaning_data.add_streak_columns(playing_stat, 'HTFormPtsStr', 'L', 3)
        assert isinstance(home_add_streak_columns_L3, pandas.DataFrame)
        home_add_streak_columns_L5 = cleaning_data.add_streak_columns(playing_stat, 'HTFormPtsStr', 'L', 5)
        assert isinstance(home_add_streak_columns_L5, pandas.DataFrame)
        away_add_streak_columns_W3 = cleaning_data.add_streak_columns(playing_stat, 'ATFormPtsStr', 'W', 3)
        assert isinstance(away_add_streak_columns_W3, pandas.DataFrame)
        away_add_streak_columns_W5 = cleaning_data.add_streak_columns(playing_stat, 'ATFormPtsStr', 'W', 5)
        assert isinstance(away_add_streak_columns_W5, pandas.DataFrame)
        away_add_streak_columns_L3 = cleaning_data.add_streak_columns(playing_stat, 'ATFormPtsStr', 'L', 3)
        assert isinstance(away_add_streak_columns_L3, pandas.DataFrame)
        away_add_streak_columns_L5 = cleaning_data.add_streak_columns(playing_stat, 'ATFormPtsStr', 'L', 5)
        assert isinstance(away_add_streak_columns_L5, pandas.DataFrame)