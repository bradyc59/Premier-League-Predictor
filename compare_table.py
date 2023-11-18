import os

cur_path = os.path.dirname(__file__)

bayes_predicted_table = open(cur_path + "/datasets/tables/bayes_position_table.txt", "r")
actual_table = open(cur_path + "/datasets/tables/actual_position.txt", "r")
knn_predicted_table = open(cur_path + "/datasets/tables/knn_position_table.txt", "r")


bayes_pred = bayes_predicted_table.readlines()
act = actual_table.readlines()
knn_pred = knn_predicted_table.readlines()


bayes_table_position = {}
actual_table_position = {}
bayes_table_position_difference = {}
knn_table_position = {}
knn_table_position_difference = {}
for team in bayes_pred:
    team = team.split(":")
    bayes_table_position[team[0]] = team[1]
pos = 1
for key, value in bayes_table_position.items(): 
    value = pos
    pos += 1
    bayes_table_position.update([(key, value)])

for team in knn_pred:
    team = team.split(":")
    knn_table_position[team[0]] = team[1]
pos = 1
for key, value in knn_table_position.items(): 
    value = pos
    pos += 1
    knn_table_position.update([(key, value)])

for team in act:
    team = team.split(":")
    actual_table_position[team[0]] = team[1]    

for team1, position1 in actual_table_position.items():
    for team2, position2 in bayes_table_position.items():
        if team1 == team2:
            difference = int(position1) - int(position2)
            position2 = difference
            bayes_table_position_difference.update([(team2, position2)])

for team1, position1 in actual_table_position.items():
    for team2, position2 in knn_table_position.items():
        if team1 == team2:
            difference = int(position1) - int(position2)
            position2 = difference
            knn_table_position_difference.update([(team2, position2)])

with open(cur_path + '/datasets/tables/position_difference_table.txt', 'w') as f:
     for key, value in bayes_table_position_difference.items(): 
        # print(key, value)
        f.write('%s:%s\n' % (key, value))

with open(cur_path + '/datasets/tables/knn_position_difference_table.txt', 'w') as f:
     for key, value in knn_table_position_difference.items(): 
        # print(key, value)
        f.write('%s:%s\n' % (key, value))
