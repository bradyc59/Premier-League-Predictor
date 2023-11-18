import pandas
from datetime import datetime
import os

cur_path = os.path.dirname(__file__)

dataset1 = pandas.read_csv(cur_path + '/datasets/train/05-06.csv')
dataset2 = pandas.read_csv(cur_path + '/datasets/train/06-07.csv')
dataset3 = pandas.read_csv(cur_path + '/datasets/train/07-08.csv')
dataset4 = pandas.read_csv(cur_path + '/datasets/train/08-09.csv')
dataset5 = pandas.read_csv(cur_path + '/datasets/train/09-10.csv')
dataset6 = pandas.read_csv(cur_path + '/datasets/train/10-11.csv')
dataset7 = pandas.read_csv(cur_path + '/datasets/train/11-12.csv')
dataset8 = pandas.read_csv(cur_path + '/datasets/train/12-13.csv')
dataset9 = pandas.read_csv(cur_path + '/datasets/train/13-14.csv')
dataset10 = pandas.read_csv(cur_path + '/datasets/train/14-15.csv')
dataset11 = pandas.read_csv(cur_path + '/datasets/train/15-16.csv')
dataset12 = pandas.read_csv(cur_path + '/datasets/train/16-17.csv')
dataset13 = pandas.read_csv(cur_path + '/datasets/train/17-18.csv')
dataset14 = pandas.read_csv(cur_path + '/datasets/train/18-19.csv')
dataset15 = pandas.read_csv(cur_path + '/datasets/train/19-20.csv')
dataset16 = pandas.read_csv(cur_path + '/datasets/train/20-21.csv')
dataset_to_test_on = pandas.read_csv(cur_path + '/datasets/test_set/21-22.csv')


test_data1 = pandas.read_csv(cur_path + '/datasets/test_dataset/02-03.csv')
test_data2 = pandas.read_csv(cur_path + '/datasets/test_dataset/01-02.csv')
test_data3 = pandas.read_csv(cur_path + '/datasets/test_dataset/00-01.csv')

dataset1.Date = pandas.to_datetime(dataset1.Date, format='%d/%m/%y')
dataset2.Date = pandas.to_datetime(dataset2.Date, format='%d/%m/%y')
dataset3.Date = pandas.to_datetime(dataset3.Date, format='%d/%m/%y')
dataset4.Date = pandas.to_datetime(dataset4.Date, format='%d/%m/%y')
dataset5.Date = pandas.to_datetime(dataset5.Date, format='%d/%m/%y')
dataset6.Date = pandas.to_datetime(dataset6.Date, format='%d/%m/%y')
dataset7.Date = pandas.to_datetime(dataset7.Date, format='%d/%m/%y')
dataset8.Date = pandas.to_datetime(dataset8.Date, format='%d/%m/%y')
dataset9.Date = pandas.to_datetime(dataset9.Date, format='%d/%m/%y')
dataset10.Date = pandas.to_datetime(dataset10.Date, format='%d/%m/%y')
dataset11.Date = pandas.to_datetime(dataset11.Date, format='%d/%m/%Y')
dataset12.Date = pandas.to_datetime(dataset12.Date, format='%d/%m/%y')
dataset13.Date = pandas.to_datetime(dataset13.Date, format='%d/%m/%Y')
dataset14.Date = pandas.to_datetime(dataset14.Date, format='%d/%m/%Y')
dataset15.Date = pandas.to_datetime(dataset15.Date, format='%d/%m/%Y')
dataset16.Date = pandas.to_datetime(dataset16.Date, format='%d/%m/%Y')
dataset_to_test_on.Date = pandas.to_datetime(dataset_to_test_on.Date, format='%d/%m/%Y')


test_data1.Date = pandas.to_datetime(test_data1.Date, format='%d/%m/%Y')
test_data2.Date = pandas.to_datetime(test_data2.Date, format='%d/%m/%y')
test_data3.Date = pandas.to_datetime(test_data3.Date, format='%d/%m/%y')


required_columns = ['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HF', 'AF', 'HS', 'AS', 'HST', 'AST', 'HY','AY','HR','AR', 'HC', 'AC']

stat1 = dataset1[required_columns]
stat2 = dataset2[required_columns]
stat3 = dataset3[required_columns]
stat4 = dataset4[required_columns]
stat5 = dataset5[required_columns]
stat6 = dataset6[required_columns]
stat7 = dataset7[required_columns]
stat8 = dataset8[required_columns]
stat9 = dataset9[required_columns]
stat10 = dataset10[required_columns]
stat11 = dataset11[required_columns]
stat12 = dataset12[required_columns]
stat13 = dataset13[required_columns]
stat14 = dataset14[required_columns]
stat15 = dataset15[required_columns]
stat16 = dataset16[required_columns]

stat_to_test_on = dataset_to_test_on[required_columns]

test_stat1 = test_data1[required_columns]
test_stat2 = test_data2[required_columns]
test_stat3 = test_data3[required_columns]



def get_goals_scored(playing_stat):
    teams = {}
    for team in playing_stat.groupby('HomeTeam').mean().T.columns:
        teams[team] = []

    for team in range(len(playing_stat)):
        HTGS = playing_stat.iloc[team]['FTHG']
        ATGS = playing_stat.iloc[team]['FTAG']
        teams[playing_stat.iloc[team].HomeTeam].append(HTGS)
        teams[playing_stat.iloc[team].AwayTeam].append(ATGS)

    GoalsScored = pandas.DataFrame(
        data=teams, index=[i for i in range(1, 39)]).T
    GoalsScored[0] = 0

    for i in range(2, 39):
        GoalsScored[i] = GoalsScored[i] + GoalsScored[i-1]

    return GoalsScored


def get_goals_conceded(playing_stat):
    teams = {}
    for team in playing_stat.groupby('HomeTeam').mean().T.columns:
        teams[team] = []

    for team in range(len(playing_stat)):
        ATGC = playing_stat.iloc[team]['FTHG']
        HTGC = playing_stat.iloc[team]['FTAG']
        teams[playing_stat.iloc[team].HomeTeam].append(HTGC)
        teams[playing_stat.iloc[team].AwayTeam].append(ATGC)

    GoalsConceded = pandas.DataFrame(
        data=teams, index=[i for i in range(1, 39)]).T
    GoalsConceded[0] = 0

    for i in range(2, 39):
        GoalsConceded[i] = GoalsConceded[i] + GoalsConceded[i-1]

    return GoalsConceded


def get_goal_stats(playing_stat):
    GC = get_goals_conceded(playing_stat)
    GS = get_goals_scored(playing_stat)

    HTGS = []
    ATGS = []
    HTGC = []
    ATGC = []

    for i in range(380):
        # Get the home team and away team for the current match
        ht = playing_stat.iloc[i].HomeTeam
        at = playing_stat.iloc[i].AwayTeam

        # Append the home team goals scored, away team goals scored, home team goals conceded, and away team goals conceded to their respective lists
        HTGS.append(GS.loc[ht][i // 10])
        ATGS.append(GS.loc[at][i // 10])
        HTGC.append(GC.loc[ht][i // 10])
        ATGC.append(GC.loc[at][i // 10])

    # Add columns to the playing_stat dataframe for home team goals scored, away team goals scored, home team goals conceded, and away team goals conceded
    playing_stat['HTGS'] = HTGS
    playing_stat['ATGS'] = ATGS
    playing_stat['HTGC'] = HTGC
    playing_stat['ATGC'] = ATGC

    return playing_stat


stat10 = stat10.drop(stat10.index[len(stat10)-1])

stat1 = get_goal_stats(stat1)
stat2 = get_goal_stats(stat2)
stat3 = get_goal_stats(stat3)
stat4 = get_goal_stats(stat4)
stat5 = get_goal_stats(stat5)
stat6 = get_goal_stats(stat6)
stat7 = get_goal_stats(stat7)
stat8 = get_goal_stats(stat8)
stat9 = get_goal_stats(stat9)
stat10 = get_goal_stats(stat10)
stat11 = get_goal_stats(stat11)
stat12 = get_goal_stats(stat12)
stat13 = get_goal_stats(stat13)
stat14 = get_goal_stats(stat14)
stat15 = get_goal_stats(stat15)
stat16 = get_goal_stats(stat16)

stat_to_test_on = get_goal_stats(stat_to_test_on)

test_stat1 = get_goal_stats(test_stat1)
test_stat2 = get_goal_stats(test_stat2)
test_stat3 = get_goal_stats(test_stat3)


def get_match_points(result):
    if result == 'W':
        return 3
    elif result == 'D':
        return 1
    else:
        return 0


def sum_points_by_match(match_result):
    # Apply the get_points function to each element in the DataFrame
    match_result_points = match_result.applymap(get_match_points)
    # Compute the cumulative sum along the columns (axis=1)
    match_result_points = match_result_points.cumsum(axis=1)
    # Insert a column of zeros at the beginning of the DataFrame
    match_result_points.insert(column=0, loc=0, value=[0*i for i in range(20)])
    return match_result_points


def get_all_matches(playing_stat):
    teams = {}
    for team in playing_stat.groupby('HomeTeam').mean().T.columns:
        teams[team] = []

    for game in range(len(playing_stat)):
        if playing_stat.iloc[game].FTR == 'H':
            teams[playing_stat.iloc[game].HomeTeam].append('W')
            teams[playing_stat.iloc[game].AwayTeam].append('L')
        elif playing_stat.iloc[game].FTR == 'A':
            teams[playing_stat.iloc[game].HomeTeam].append('L')
            teams[playing_stat.iloc[game].AwayTeam].append('W')
        elif playing_stat.iloc[game].FTR == 'D':
            teams[playing_stat.iloc[game].HomeTeam].append('D')
            teams[playing_stat.iloc[game].AwayTeam].append('D')

    return pandas.DataFrame(data=teams, index=[i for i in range(1, 39)]).T


def aggregate_match_points(playing_stat):
    match_results = get_all_matches(playing_stat)
    # Compute the cumulative points for all teams in the league
    cumulative_pts = sum_points_by_match(match_results)
    home_team_points = []
    away_team_points = []

    for i, row in playing_stat.iterrows():
        # Get the home team and away team for the current match
        home_team, away_team = row['HomeTeam'], row['AwayTeam']
        # Compute the points for the home and away teams at the current match
        home_team_points.append(cumulative_pts.loc[home_team][i // 10])
        away_team_points.append(cumulative_pts.loc[away_team][i // 10])

    # Add columns to the playing_stat dataframe for home team points and away team points
    playing_stat['HTP'] = home_team_points
    playing_stat['ATP'] = away_team_points

    return playing_stat



stat1 = aggregate_match_points(stat1)
stat2 = aggregate_match_points(stat2)
stat3 = aggregate_match_points(stat3)
stat4 = aggregate_match_points(stat4)
stat5 = aggregate_match_points(stat5)
stat6 = aggregate_match_points(stat6)
stat7 = aggregate_match_points(stat7)
stat8 = aggregate_match_points(stat8)
stat9 = aggregate_match_points(stat9)
stat10 = aggregate_match_points(stat10)
stat11 = aggregate_match_points(stat11)
stat12 = aggregate_match_points(stat12)
stat13 = aggregate_match_points(stat13)
stat14 = aggregate_match_points(stat14)
stat15 = aggregate_match_points(stat15)
stat16 = aggregate_match_points(stat16)

stat_to_test_on = aggregate_match_points(stat_to_test_on)


test_stat1 = aggregate_match_points(test_stat1)
test_stat2 = aggregate_match_points(test_stat2)
test_stat3 = aggregate_match_points(test_stat3)



def get_team_form(playing_stat, num):
    form = get_all_matches(playing_stat)
    form_final = form.copy()
    for i in range(num, 39):
        form_final[i] = ''
        j = 0
        while j < num:
            form_final[i] += form[i-j]
            j += 1
    return form_final


def add_form(playing_stat, num):
    form = get_team_form(playing_stat, num)

    # Create lists of 'M' values for the home and away teams
    home = ['M' for i in range(num * 10)]
    away = ['M' for i in range(num * 10)]

    # Initialize the counter for the form data
    j = num

    # Iterate over the rows of the playing_stat DataFrame
    for i in range((num*10), 380):
        # Get the home and away teams for the current match
        home_team = playing_stat.iloc[i].HomeTeam
        away_team = playing_stat.iloc[i].AwayTeam

        # Get the form data for the home and away teams
        home_form = form.loc[home_team][j]
        away_form = form.loc[away_team][j]

        # Append the last element of the form data to the appropriate lists
        home.append(home_form[num-1])
        away.append(away_form[num-1])

        # Increment the counter for the form data if necessary
        if ((i + 1) % 10) == 0:
            j = j + 1

    # Add the form data to the playing_stat DataFrame
    playing_stat['HM' + str(num)] = home
    playing_stat['AM' + str(num)] = away

    return playing_stat


def add_form_difference(playing_stat):
    playing_stat = add_form(playing_stat, 1)
    playing_stat = add_form(playing_stat, 2)
    playing_stat = add_form(playing_stat, 3)
    playing_stat = add_form(playing_stat, 4)
    playing_stat = add_form(playing_stat, 5)

    return playing_stat


stat1 = add_form_difference(stat1)
stat2 = add_form_difference(stat2)
stat3 = add_form_difference(stat3)
stat4 = add_form_difference(stat4)
stat5 = add_form_difference(stat5)
stat6 = add_form_difference(stat6)
stat7 = add_form_difference(stat7)
stat8 = add_form_difference(stat8)
stat9 = add_form_difference(stat9)
stat10 = add_form_difference(stat10)
stat11 = add_form_difference(stat11)
stat12 = add_form_difference(stat12)
stat13 = add_form_difference(stat13)
stat14 = add_form_difference(stat14)
stat15 = add_form_difference(stat15)
stat16 = add_form_difference(stat16)

stat_to_test_on = add_form_difference(stat_to_test_on)


test_stat1 = add_form_difference(test_stat1)
test_stat2 = add_form_difference(test_stat2)
test_stat3 = add_form_difference(test_stat3)


cols = ['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTGS', 'ATGS', 'HTGC', 'ATGC', 'HTP', 'ATP', 'HM1', 'HM2', 'HM3',
        'HM4', 'HM5', 'AM1', 'AM2', 'AM3', 'AM4', 'AM5', 'HF', 'AF', 'HS', 'AS', 'HST', 'AST' , 'HC', 'AC', 'HY','AY','HR','AR']

stat1 = stat1[cols]
stat2 = stat2[cols]
stat3 = stat3[cols]
stat4 = stat4[cols]
stat5 = stat5[cols]
stat6 = stat6[cols]
stat7 = stat7[cols]
stat8 = stat8[cols]
stat9 = stat9[cols]
stat10 = stat10[cols]
stat11 = stat11[cols]
stat12 = stat12[cols]
stat13 = stat13[cols]
stat14 = stat14[cols]
stat15 = stat15[cols]
stat16 = stat16[cols]

stat_to_test_on = stat_to_test_on[cols]

test_stat1 = test_stat1[cols]
test_stat2 = test_stat2[cols]
test_stat3 = test_stat3[cols]


league_standings = pandas.read_csv(cur_path + "/datasets/epl_standings/EPLStandings.csv")
test_league_standings = pandas.read_csv(cur_path + "/datasets/test_dataset/TestEPLStandings.csv")

league_standings.set_index(['Team'], inplace=True)
# league_standings = league_standings.fillna(20)

test_league_standings.set_index(['Team'], inplace=True)
# test_league_standings = test_league_standings.fillna(20)



def get_team_last_year_standing(playing_stat, Standings, year):
    HomeTeamLP = []
    AwayTeamLP = []
    i = 0
    while i < 380:
        # Get the home and away teams for the current match
        home_team = playing_stat.iloc[i].HomeTeam
        away_team = playing_stat.iloc[i].AwayTeam
        # Get the last year standing data for the home and away teams
        HomeTeamLP.append(Standings.loc[home_team][year])
        AwayTeamLP.append(Standings.loc[away_team][year])
        i += 1
    # Add the 'HomeTeamLP' and 'AwayTeamLP' lists as new columns to the playing_stat DataFrame
    playing_stat['HomeTeamLP'] = HomeTeamLP
    playing_stat['AwayTeamLP'] = AwayTeamLP
    return playing_stat


get_team_last_year_standing(stat1, league_standings, 0)
get_team_last_year_standing(stat2, league_standings, 1)
get_team_last_year_standing(stat3, league_standings, 2)
get_team_last_year_standing(stat4, league_standings, 3)
get_team_last_year_standing(stat5, league_standings, 4)
get_team_last_year_standing(stat6, league_standings, 5)
get_team_last_year_standing(stat7, league_standings, 6)
get_team_last_year_standing(stat8, league_standings, 7)
get_team_last_year_standing(stat9, league_standings, 8)
get_team_last_year_standing(stat10, league_standings, 9)
get_team_last_year_standing(stat11, league_standings, 10)
get_team_last_year_standing(stat12, league_standings, 11)
get_team_last_year_standing(stat13, league_standings, 12)
get_team_last_year_standing(stat14, league_standings, 13)
get_team_last_year_standing(stat15, league_standings, 14)
get_team_last_year_standing(stat16, league_standings, 15)

get_team_last_year_standing(stat_to_test_on, league_standings, 15)


get_team_last_year_standing(test_stat1, test_league_standings, 0)
get_team_last_year_standing(test_stat2, test_league_standings, 1)
get_team_last_year_standing(test_stat3, test_league_standings, 2)


def get_matchweek(playing_stat):
    current_matchweek = 0
    matchweek = []
    for i in range(380):
        if i % 10 == 0:
            current_matchweek += 1
        matchweek.append(current_matchweek)
        
    playing_stat['MW'] = matchweek
    return playing_stat

stat1 = get_matchweek(stat1)
stat2 = get_matchweek(stat2)
stat3 = get_matchweek(stat3)
stat4 = get_matchweek(stat4)
stat5 = get_matchweek(stat5)
stat6 = get_matchweek(stat6)
stat7 = get_matchweek(stat7)
stat8 = get_matchweek(stat8)
stat9 = get_matchweek(stat9)
stat10 = get_matchweek(stat10)
stat11 = get_matchweek(stat11)
stat12 = get_matchweek(stat12)
stat13 = get_matchweek(stat13)
stat14 = get_matchweek(stat14)
stat15 = get_matchweek(stat15)
stat16 = get_matchweek(stat16)

stat_to_test_on = get_matchweek(stat_to_test_on)


test_stat1 = get_matchweek(test_stat1)
test_stat2 = get_matchweek(test_stat2)
test_stat3 = get_matchweek(test_stat3)


playing_stat_joined = pandas.concat([stat1,stat2,stat3,stat4,stat5,stat6,stat7,stat8,stat9,stat10,stat11,stat12,stat13,stat14,stat15,stat16], ignore_index=True)

test_stat_joined = pandas.concat([test_stat1,test_stat2,test_stat3], ignore_index=True)


def get_form_points(string):
    sum = 0
    for letter in string:
        sum += get_match_points(letter)   
    return sum


playing_stat_joined['HTFormPtsStr'] = playing_stat_joined['HM1'] + playing_stat_joined['HM2'] + playing_stat_joined['HM3'] + playing_stat_joined['HM4'] + playing_stat_joined['HM5']
playing_stat_joined['ATFormPtsStr'] = playing_stat_joined['AM1'] + playing_stat_joined['AM2'] + playing_stat_joined['AM3'] + playing_stat_joined['AM4'] + playing_stat_joined['AM5']

playing_stat_joined['HTFormPts'] = playing_stat_joined['HTFormPtsStr'].apply(get_form_points)
playing_stat_joined['ATFormPts'] = playing_stat_joined['ATFormPtsStr'].apply(get_form_points)

stat_to_test_on['HTFormPtsStr'] = stat_to_test_on['HM1'] + stat_to_test_on['HM2'] + stat_to_test_on['HM3'] + stat_to_test_on['HM4'] + stat_to_test_on['HM5']
stat_to_test_on['ATFormPtsStr'] = stat_to_test_on['AM1'] + stat_to_test_on['AM2'] + stat_to_test_on['AM3'] + stat_to_test_on['AM4'] + stat_to_test_on['AM5']

stat_to_test_on['HTFormPts'] = stat_to_test_on['HTFormPtsStr'].apply(get_form_points)
stat_to_test_on['ATFormPts'] = stat_to_test_on['ATFormPtsStr'].apply(get_form_points)


test_stat_joined['HTFormPtsStr'] = test_stat_joined['HM1'] + test_stat_joined['HM2'] + test_stat_joined['HM3'] + test_stat_joined['HM4'] + test_stat_joined['HM5']
test_stat_joined['ATFormPtsStr'] = test_stat_joined['AM1'] + test_stat_joined['AM2'] + test_stat_joined['AM3'] + test_stat_joined['AM4'] + test_stat_joined['AM5']

test_stat_joined['HTFormPts'] = test_stat_joined['HTFormPtsStr'].apply(get_form_points)
test_stat_joined['ATFormPts'] = test_stat_joined['ATFormPtsStr'].apply(get_form_points)



def add_streak_columns(playing_stat, form_column, streak_type, streak_len):
    """
    Adds new columns to the playing_stat DataFrame for a streak of the given type (W or L) and length.
    :param playing_stat: DataFrame containing the data.
    :param form_column: Name of the column containing the form data.
    :param streak_type: Type of streak to look for, either 'W' or 'L'
    :param streak_len: Length of streak to look for
    """
    check_string = streak_type * streak_len
    new_column_name = f"{form_column[:2]}{streak_type}Streak{streak_len}"
    playing_stat[new_column_name] = playing_stat[form_column].apply(lambda x: 1 if x[-streak_len:] == check_string else 0)
    
add_streak_columns(playing_stat_joined, 'HTFormPtsStr', 'W', 3)
add_streak_columns(playing_stat_joined, 'HTFormPtsStr', 'W', 5)
add_streak_columns(playing_stat_joined, 'HTFormPtsStr', 'L', 3)
add_streak_columns(playing_stat_joined, 'HTFormPtsStr', 'L', 5)
add_streak_columns(playing_stat_joined, 'ATFormPtsStr', 'W', 3)
add_streak_columns(playing_stat_joined, 'ATFormPtsStr', 'W', 5)
add_streak_columns(playing_stat_joined, 'ATFormPtsStr', 'L', 3)
add_streak_columns(playing_stat_joined, 'ATFormPtsStr', 'L', 5)

playing_stat_joined['DiffPts'] = playing_stat_joined['HTP'] - playing_stat_joined['ATP']
playing_stat_joined['DiffFormPts'] = playing_stat_joined['HTFormPts'] - playing_stat_joined['ATFormPts']

playing_stat_joined['DiffLP'] = playing_stat_joined['HomeTeamLP'] - playing_stat_joined['AwayTeamLP']

add_streak_columns(stat_to_test_on, 'HTFormPtsStr', 'W', 3)
add_streak_columns(stat_to_test_on, 'HTFormPtsStr', 'W', 5)
add_streak_columns(stat_to_test_on, 'HTFormPtsStr', 'L', 3)
add_streak_columns(stat_to_test_on, 'HTFormPtsStr', 'L', 5)
add_streak_columns(stat_to_test_on, 'ATFormPtsStr', 'W', 3)
add_streak_columns(stat_to_test_on, 'ATFormPtsStr', 'W', 5)
add_streak_columns(stat_to_test_on, 'ATFormPtsStr', 'L', 3)
add_streak_columns(stat_to_test_on, 'ATFormPtsStr', 'L', 5)

stat_to_test_on['DiffPts'] = stat_to_test_on['HTP'] - stat_to_test_on['ATP']
stat_to_test_on['DiffFormPts'] = stat_to_test_on['HTFormPts'] - stat_to_test_on['ATFormPts']

stat_to_test_on['DiffLP'] = stat_to_test_on['HomeTeamLP'] - stat_to_test_on['AwayTeamLP']

stat_to_test_on['HTGD'] = stat_to_test_on['HTGS'] - stat_to_test_on['HTGC']
stat_to_test_on['ATGD'] = stat_to_test_on['ATGS'] - stat_to_test_on['ATGC']

add_streak_columns(test_stat_joined, 'HTFormPtsStr', 'W', 3)
add_streak_columns(test_stat_joined, 'HTFormPtsStr', 'W', 5)
add_streak_columns(test_stat_joined, 'HTFormPtsStr', 'L', 3)
add_streak_columns(test_stat_joined, 'HTFormPtsStr', 'L', 5)
add_streak_columns(test_stat_joined, 'ATFormPtsStr', 'W', 3)
add_streak_columns(test_stat_joined, 'ATFormPtsStr', 'W', 5)
add_streak_columns(test_stat_joined, 'ATFormPtsStr', 'L', 3)
add_streak_columns(test_stat_joined, 'ATFormPtsStr', 'L', 5)

playing_stat_joined['HTGD'] = playing_stat_joined['HTGS'] - playing_stat_joined['HTGC']
playing_stat_joined['ATGD'] = playing_stat_joined['ATGS'] - playing_stat_joined['ATGC']

test_stat_joined['DiffPts'] = test_stat_joined['HTP'] - test_stat_joined['ATP']
test_stat_joined['DiffFormPts'] = test_stat_joined['HTFormPts'] - test_stat_joined['ATFormPts']

test_stat_joined['DiffLP'] = test_stat_joined['HomeTeamLP'] - test_stat_joined['AwayTeamLP']

test_stat_joined['HTGD'] = test_stat_joined['HTGS'] - test_stat_joined['HTGC']
test_stat_joined['ATGD'] = test_stat_joined['ATGS'] - test_stat_joined['ATGC']


cols = ['HTGD','ATGD','DiffPts','HTP','ATP']
playing_stat_joined.MW = playing_stat_joined.MW.astype(float)

stat_to_test_on.MW = stat_to_test_on.MW.astype(float)

test_stat_joined.MW = test_stat_joined.MW.astype(float)


playing_stat_joined.to_csv(cur_path + "/datasets/cleaned_datasets/final_cleaned_dataset.csv")

stat_to_test_on.to_csv(cur_path + "/datasets/cleaned_datasets/final_cleaned_test_dataset.csv")

test_stat_joined.to_csv(cur_path + "/datasets/test_dataset/test_final_cleaned_dataset.csv")

