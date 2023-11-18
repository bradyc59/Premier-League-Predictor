import pandas
import os

# location = 'C:/FYP_Gitlab_Conor/src/datasets/'
# test_location = 'C:/FYP_Gitlab_Conor/src/datasets/test_dataset/'

cur_path = os.path.dirname(__file__)

data = pandas.read_csv(cur_path + '/datasets/cleaned_datasets/final_cleaned_dataset.csv')
data_to_test = pandas.read_csv(cur_path + '/datasets/cleaned_datasets/final_cleaned_test_dataset.csv')
test_data = pandas.read_csv(cur_path + '/datasets/test_dataset/test_final_cleaned_dataset.csv')

def drop_irrelevant_data(data): 

	data.drop(['Unnamed: 0','HomeTeam', 'AwayTeam', 'Date', 'MW', 'HTFormPtsStr', 'ATFormPtsStr', 'FTHG', 'FTAG',
	           'HTGS', 'ATGS', 'HTGC', 'ATGC','HomeTeamLP', 'AwayTeamLP','HTFormPts','ATFormPts',
	           'HM4','HM5','AM4','AM5','HTWStreak3','HTLStreak3','HTWStreak5','HTLStreak5',
	           'ATWStreak3','ATLStreak3','ATLStreak5','ATWStreak5'],1, inplace=True)
	return data

def drop_testing_data(data_to_test):
	data_to_test.drop(['Unnamed: 0', 'Date', 'MW', 'HTFormPtsStr', 'ATFormPtsStr', 'FTHG', 'FTAG',
	           'HTGS', 'ATGS', 'HTGC', 'ATGC','HomeTeamLP', 'AwayTeamLP','HTFormPts','ATFormPts',
	           'HM4','HM5','AM4','AM5','HTWStreak3','HTLStreak3','HTWStreak5','HTLStreak5',
	           'ATWStreak3','ATLStreak3','ATLStreak5','ATWStreak5'],1, inplace=True)
	return data_to_test

test_cleaned_data = drop_testing_data(data_to_test)
cleaned_data = drop_irrelevant_data(data)

def get_dataset_stats(data):
    total_matches = data.shape[0]
    number_of_features = data.shape[1] - 1
    number_homewins = data['FTR'].value_counts()['H']
    win_rate = (number_homewins / total_matches) * 100
    return total_matches, number_of_features, number_homewins, win_rate

total_matches, number_of_features, number_homewins, win_rate = get_dataset_stats(cleaned_data)
total_matches, number_of_features, number_homewins, win_rate = get_dataset_stats(test_cleaned_data)

cleaned_data.to_csv(cur_path + '/datasets/cleaned_datasets/cleanedDataset_full_no_normalisation.csv')
test_cleaned_data.to_csv(cur_path + '/datasets/cleaned_datasets/cleanedTestDataset_full_no_normalisation.csv')
# cleaned_data.to_csv(cur_path + '/datasets/test_dataset/test_cleanedDataset_full_no_normalisation.csv')

print ("Total number of matches: {}".format(total_matches))
print ("Number of features: {}".format(number_of_features))
print ("Number of matches won by home team: {}".format(number_homewins))
print ("Win rate of home team: {:.2f}%".format(win_rate))
