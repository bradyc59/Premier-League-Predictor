import pandas
import os

cur_path = os.path.dirname(__file__)

data = pandas.read_csv(cur_path + '/datasets/cleaned_datasets/cleanedDataset_full_no_normalisation.csv', index_col = 0)
data_to_test = pandas.read_csv(cur_path + '/datasets/cleaned_datasets/cleanedTestDataset_full_no_normalisation.csv', index_col = 0)
test_data = pandas.read_csv(cur_path + '/datasets/test_dataset/test_cleanedDataset_full_no_normalisation.csv', index_col=0)
games = ['HomeTeam', 'AwayTeam']
cols = ['HTP','ATP', 'HM1', 'HM2', 'HM3', 'AM1', 'AM2', 'AM3','HTGD','ATGD','HF', 'AF', 'HS', 'AS', 'HST', 'AST','HC', 'AC', 'HY','AY','HR','AR', 'DiffFormPts','DiffPts','DiffLP', 'FTR']
tester_columns = ['HomeTeam', 'AwayTeam', 'HTP','ATP', 'HM1', 'HM2', 'HM3', 'AM1', 'AM2', 'AM3','HTGD','ATGD','HF', 'AF', 'HS', 'AS', 'HST', 'AST','HC', 'AC', 'HY','AY','HR','AR','DiffFormPts','DiffPts','DiffLP', 'FTR']
data = data[cols]
games_dataframe = data_to_test[games]
# print(data_to_test)
# test_data = test_data[cols]
data_to_test = data_to_test[tester_columns]

data = data.drop(['HM1', 'HM2', 'HM3', 'AM1', 'AM2', 'AM3'], axis=1)
test_data = test_data.drop(['HM1', 'HM2', 'HM3', 'AM1', 'AM2', 'AM3', 'FTR'], axis=1)
bayes_test_data = data_to_test.drop(['HomeTeam','AwayTeam','HM1', 'HM2', 'HM3', 'AM1', 'AM2', 'AM3'], axis=1)
data_to_test = data_to_test.drop(['HM1', 'HM2', 'HM3', 'AM1', 'AM2', 'AM3'], axis=1)

# bayesFile = data + data_to_test
result = pandas.concat([data, bayes_test_data])
games_dataframe.to_csv(cur_path + '/datasets/results/games_for_bayes.csv')
data.to_csv(cur_path + '/datasets/knn_datasets/knn_no_normalisation.csv')
data_to_test.to_csv(cur_path + '/datasets/knn_datasets/knn_test_data_no_normalisation.csv')
result.to_csv(cur_path + '/datasets/bayes_datasets/bayes_no_normalisation.csv')
# data_to_test.to_csv(cur_path + '/datasets/bayes_datasets/bayes_test_no_normalisation.csv')

test_data.to_csv(cur_path + '/datasets/test_dataset/test_bayes_no_normalisation.csv')

