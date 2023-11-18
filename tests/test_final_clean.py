import sys
import os

import pytest
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import final_clean
import pandas

@pytest.fixture
def cleaned_dataset():
    # Load the cleaned dataset
    cur_path = os.path.dirname(__file__)
    data = pandas.read_csv(cur_path + '/../datasets/cleaned_datasets/final_cleaned_dataset.csv')
    # Modify the dataset by dropping irrelevant data
    cleaned_data = final_clean.drop_irrelevant_data(data)
    return cleaned_data

def test_drop_irrelevant_data(cleaned_dataset):
    assert isinstance(cleaned_dataset, pandas.DataFrame)

def test_get_dataset_stats(cleaned_dataset):
    dataset_stats = final_clean.get_dataset_stats(cleaned_dataset)
    assert isinstance(dataset_stats, tuple)