import csv
import math
import random
import numpy
import pandas
import os

cur_path = os.path.dirname(__file__)

def load_CSV(filename):
    # Load the CSV file and convert the data to floats and strings
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    for i in range(1, len(dataset)):
        dataset[i] = [float(x) for x in dataset[i][1:-1]] + [dataset[i][-1]]
    # Remove the header row and return the remaining dataset
    return dataset[1:]

def split_dataset(dataset):
    # Split the dataset into training and test datasets
    return dataset[:6080], dataset[6080:]

def separate_by_class(dataset):
    # Group the dataset by class value
    separated = {}
    for vector in dataset:
        class_label = vector[-1]
        separated.setdefault(class_label, []).append(vector[:-1])
    return separated

def mean(numbers):
    # Calculate the mean value of a list of numbers
    return sum(numbers)/float(len(numbers))

def stdev(numbers):
    # Calculate the standard deviation of a list of numbers
    avg = mean(numbers)
    variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variance)

def summarize(dataset):
    # Calculate the mean and standard deviation of each attribute in the dataset
    summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
    # Remove the class label from the list of summaries
    del summaries[-1]
    return summaries

def summarize_by_class(dataset):
    # Group the dataset by class value and calculate summary statistics for each attribute
    separated = separate_by_class(dataset)
    summaries = {}
    for classValue, instances in separated.items():
        summaries[classValue] = summarize(instances)
    return summaries

def calculate_probability(x, mean, stdev):
    # Calculate the probability of a given attribute value given the mean and standard deviation
    variance = stdev ** 2
    exponent = math.exp(-((x - mean) ** 2) / (2 * variance))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent

def calculate_class_probabilities(summaries, inputVector):
    # Calculate the probabilities of each class value given the input vector
    probabilities = {}
    for class_value, class_summaries in summaries.items():
        probabilities[class_value] = 1.0
        for x, (mean, stdev) in zip(inputVector, class_summaries):
            probabilities[class_value] *= calculate_probability(x, mean, stdev)
    return probabilities

def predict(summaries, inputVector):
    # Predict the class value for a given input vector based on summary statistics
    probabilities = calculate_class_probabilities(summaries, inputVector)
    best_label, best_prob = max(probabilities.items(), key=lambda x: x[1])
    return best_label

def get_predictions(summaries, testSet):
    # Make predictions for each instance in the test set
    predictions = [predict(summaries, instance) for instance in testSet]
    return predictions


def get_accuracy(predictions, actuals):
    correct = 0
    for i in range(len(predictions)):
        if predictions[i][-1] == actuals[i]:
            correct += 1
    return correct / len(predictions) * 100.0

def main():
	full_dataset = cur_path + '/datasets/bayes_datasets/bayes_no_normalisation.csv'
	list_of_games = pandas.read_csv(cur_path + '/datasets/results/games_for_bayes.csv')
	full_dataset = load_CSV(full_dataset)
	training_set, test_set = split_dataset(full_dataset)
	summaries = summarize_by_class(training_set)
	predictions = get_predictions(summaries, test_set)
	accuracy = get_accuracy(test_set, predictions)
	results = pandas.DataFrame(predictions, columns = ['FTR'])
	list_of_games['FTR'] = results
	list_of_games.to_csv(cur_path + '/datasets/results/bayes_predicted_results.csv')
     
	print('Accuracy: {0} %'.format(accuracy))
        
	return accuracy

if __name__ == "__main__":
    main()