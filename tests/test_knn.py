
import os
import sys
import pandas as pd
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from knn import euclidean_distance, normalize, knn, predict_outcome, predict_premier_league, get_accuracy, lib_knn

def test_euclidean_distance():
    x1 = np.array([1, 2, 3])
    x2 = np.array([4, 5, 6])
    assert euclidean_distance(x1, x2) == np.sqrt(27)
    
    x1 = np.array([1, 2, 3])
    x2 = np.array([1, 2, 3])
    assert euclidean_distance(x1, x2) == 0.0
    

def test_normalize():
    data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
    df = pd.DataFrame(data)
    normalized_df = normalize(df)
    expected_result = pd.DataFrame({'A': [-1.0, 0.0, 1.0], 'B': [-1.0, 0.0, 1.0], 'C': [-1.0, 0.0, 1.0]})
    assert normalized_df.equals(expected_result)

def test_knn():
    training_data = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9], 'class': ['A', 'B', 'C']})
    test_instance = np.array([1, 5, 7])
    k = 2
    result = knn(training_data, test_instance, k)
    assert result == [0, 1]
    
    training_data = pd.DataFrame({'a': [1, 2, 3, 4, 5], 'b': [2, 4, 6, 8, 10], 'c': [3, 6, 9, 12, 15], 'class': ['A', 'B', 'A', 'B', 'A']})
    test_instance = np.array([1, 2, 3])
    k = 3
    result = knn(training_data, test_instance, k)
    assert result == [0, 1, 2]

def test_predict_outcome():
    training_data = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9], 'FTR': ['A', 'H', 'D']})

    test_instance = np.array([1, 5, 7])
    k = 3
    result = predict_outcome(training_data, test_instance, k)
    assert isinstance(result, str)

def test_get_accuracy():
    predictions = ['A', 'B', 'C', 'D', 'A']
    actuals = ['A', 'B', 'C', 'D', 'B']
    accuracy = get_accuracy(predictions, actuals)
    expected_accuracy = 80.0
    assert accuracy == expected_accuracy, f"Expected {expected_accuracy} but got {accuracy}"

def test_lib_knn():
    X, y = make_classification(n_samples=100, n_features=10, n_classes=2, random_state=42)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    predictions = lib_knn(X_train, y_train, X_test)

    assert len(predictions) == len(X_test), f"Expected {len(X_test)} predictions but got {len(predictions)}"

    assert all(prediction in set(y_train) for prediction in predictions), "Invalid prediction found"

    accuracy = sum(predictions == y_test) / len(y_test)
    assert accuracy > 0.8, f"Expected accuracy > 0.8 but got {accuracy}"