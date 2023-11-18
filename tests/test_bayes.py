import sys
import os
import pytest
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import bayes

cur_path = os.path.dirname(__file__)

data = cur_path + '/../datasets/bayes_datasets/bayes_no_normalisation.csv'

def test_load_CSV():
    dataset = bayes.load_CSV(data)
    assert isinstance(dataset, list)
    assert isinstance(dataset[2][2], float)
    with pytest.raises(IndexError):
        assert isinstance(dataset[50][10000], float)

dataset = bayes.load_CSV(data)

def test_split_dataset():
    train_set, test_set = bayes.split_dataset(dataset)
    assert isinstance(train_set, list)
    assert isinstance(test_set, list)


train_set, test_set = bayes.split_dataset(dataset)

def test_separate_by_class():
    seperate = bayes.separate_by_class(train_set)
    assert isinstance(seperate, dict)

def test_summarize_by_class():
    summary = bayes.summarize_by_class(train_set)
    assert isinstance(summary, dict)

seperate = bayes.separate_by_class(train_set)

def test_summarize():
    summaries = {}
    for classValue, instance in seperate.items():
        summaries[classValue] = bayes.summarize(instance)
    assert isinstance(summaries, dict)

def test_mean():
    numbers = [2.0, 3.0, 1.0, 4.0, 20.0]
    mean = bayes.mean(numbers)
    assert isinstance(mean, float)
    strings = ["Man United", "Liverpool"]
    with pytest.raises(TypeError):
        string_mean = bayes.mean(strings)
        assert isinstance(string_mean, float)

def test_stdev():
    numbers = [2.0, 3.0, 1.0, 4.0, 20.0]
    stdev = bayes.stdev(numbers)
    assert isinstance(stdev, float)
    strings = ["Man United", "Liverpool"]
    with pytest.raises(TypeError):
        string_stdev = bayes.stdev(strings)
        assert isinstance(string_stdev, float)

summary = bayes.summarize_by_class(train_set)

def test_calculate_probability():
    for i in range(len(test_set)):
        probabilities = {}
        for classValue, classSummaries in summary.items():
            probabilities[classValue] = 1
            for j in range(len(classSummaries)):
                mean, stdev = classSummaries[j]
                x = test_set[i][j]
                probabilities[classValue] *= bayes.calculate_probability(x, mean, stdev)
    assert isinstance(probabilities, dict)

def test_calculate_class_probabilities():
    for i in range(len(test_set)):
        calculate_class_probabilities = bayes.calculate_class_probabilities(summary, test_set[i])
        assert isinstance(calculate_class_probabilities, dict)

def test_predict():
    result = bayes.get_predictions(summary, test_set)
    assert isinstance(result, list)

result = bayes.get_predictions(summary, test_set)

def test_get_accuracy():
    accuracy = bayes.get_accuracy(test_set, result)
    assert isinstance(accuracy, float)