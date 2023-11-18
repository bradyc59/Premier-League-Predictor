import numpy as np
import pandas
import operator
import os
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

cur_path = os.path.dirname(__file__)

# Function to calculate the Euclidean distance between two points
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2)**2))

# Function to normalize the data using mean normalization
def normalize(df):
    result = df.copy()
    for feature_name in df.columns:
        mean = df[feature_name].mean()
        std = df[feature_name].std()
        result[feature_name] = (df[feature_name] - mean) / std
    return result

# Function to find the k nearest neighbors of a test instance in the training data
def knn(training_data, test_instance, k):
    distances = []
    for index, row in training_data.iterrows():
        # Calculate the Euclidean distance between the test instance and the current training instance
        distance = euclidean_distance(row[:-1].to_numpy(), test_instance)
        distances.append((distance, index))
    # Sort the distances list in ascending order by distance
    distances.sort(key=operator.itemgetter(0))
    # Get the indices of the k nearest neighbors
    indices = [i[1] for i in distances[:k]]
    return indices

# Function to predict the outcome of a match for a test instance
def predict_outcome(training_data, test_instance, k):
    indices = knn(training_data, test_instance, k)
    # Get the outcomes of the k nearest neighbors
    outcomes = training_data.loc[indices, "FTR"].to_numpy()    
    # Return the most common outcome
    return max(set(outcomes), key=list(outcomes).count)

# Function to predict the outcomes of all matches in the test data
def predict_premier_league(training_data, test_data, k):
    # Extract the FTR column from the training data
    FTR_data = training_data['FTR']
    training_data = training_data.drop(['FTR'],1)
    # Normalize the training data
    normalized_training_data = normalize(training_data)
    # Add the FTR column back to the normalized training data
    normalized_training_data['FTR'] = FTR_data

    results = []
    for index, row in test_data.iterrows():
        result = predict_outcome(normalized_training_data, row[['HTP', 'ATP',
                                                     'HTGD', 'ATGD', 'HF', 'AF','HS', 'AS', 'HST', 'AST','HC', 'AC', 'HY','AY','HR','AR',
                                                     'DiffFormPts', 'DiffPts',
                                                     'DiffLP']].to_numpy(), k)
        results.append(result)
    return results

def get_accuracy(predictions, actuals):
    correct = 0
    for i in range(len(predictions)):
        if predictions[i] == actuals[i]:
            correct += 1
    return correct / len(predictions) * 100.0


# Library prediction knn
def lib_knn(attributes, target_label, test_attributes):

    classifier = KNeighborsClassifier(n_neighbors=5)  
    classifier.fit(attributes, target_label) 

    prediction = classifier.predict(test_attributes)

    return prediction

def get_accuracy_lib(test_target_label, prediction):
        count = 0
        for label, predcition_label in zip(test_target_label, prediction):
            if label == predcition_label:
                count += 1
        return count / len(prediction) * 100

def main():
    train_dataset = pandas.read_csv(cur_path + '/datasets/knn_datasets/knn_no_normalisation.csv')
    train_dataset = train_dataset.loc[:, ~train_dataset.columns.str.contains('^Unnamed')]
    test_dataset = pandas.read_csv(cur_path + '/datasets/knn_datasets/knn_test_data_no_normalisation.csv')

    home_list = test_dataset['HomeTeam'].tolist()
    away_list = test_dataset['AwayTeam'].tolist()
    k = 5

    file2 = pandas.read_csv(cur_path + '/datasets/results/predicted_reuslts.csv')

    prediction = predict_premier_league(train_dataset,test_dataset,k)
    actuals = test_dataset['FTR'].to_numpy()

    FTR_dataset = pandas.DataFrame(
        {'HomeTeam': home_list,
        'AwayTeam': away_list,
        'FTR': prediction
        })
    list12 = []
    # This was used in testing to see if brentford, a new team in the league, were given a draw or loss every game, due to not having any data on them
    for index, row in file2.iterrows():
        if row['HomeTeam'] == 'Brentford':
            home_brentford = row['HomeTeam'], row['AwayTeam'], row['FTR']
            list12.append(home_brentford)
        if row['AwayTeam'] == 'Brentford':
            away_brentford = row['HomeTeam'], row['AwayTeam'], row['FTR']
            list12.append(away_brentford)


    FTR_dataset.to_csv(cur_path + '/datasets/results/predicted_reuslts.csv')
    print("Accuracy:", get_accuracy(prediction, actuals), "%")

    # All code below is used for to use the sklearn library
    x_all = train_dataset.drop(['FTR'], 1)
    y_all = train_dataset['FTR']
    X_train, X_test, y_train, y_test = train_test_split(x_all, y_all, 
                                                    test_size = 380,
                                                    stratify = y_all)


    
    knn_library_pred = lib_knn(X_train, y_train, X_test)
    
    print("Library Accuracy:", get_accuracy_lib(y_test, knn_library_pred), "%")

    return get_accuracy(prediction, actuals)
    

if __name__ == "__main__":
    main()