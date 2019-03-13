"""
 # @author rajchoudhary
 # @email raj.choudhary1603@gmail.com
 # @create date 2019-03-12 10:44:15
 # @modify date 2019-03-13 21:48:23
 # @desc [File for preprocessing the "Liar, Liar Pants on Fire" dataset.]
"""


# Importing the libraries
import numpy as np
import pandas as pd


# Helper functions
def read_tsv(file_path):
    """Function to read the dataset with .tsv extension.
    
    Parameters:
    -----------
    file_path: string
        Contains the path to the file to be read.

    Returns:
    --------
    dataset: pandas dataframe
        Contains the dataset read.
    """

    dataset = pd.read_csv(file_path, sep='\t', header=None)
    return dataset


def preprocess_dataset(dataset):
    """Function to select the required columns from the dataset and
    convert the multiclass labels to binary class labels.
    
    Parameters:
    -----------
    dataset: pandas dataframe
        The dataset whose contents are to be processed.
    """

    columns_to_select = [1, 2]
    dataset = dataset.iloc[:, columns_to_select]
    dataset.columns = ['label', 'news']

    # Converting the multiclass labels to binary labels
    labels_map = {
        'true': 'true',
        'mostly-true': 'true',
        'half-true': 'true',
        'false': 'false',
        'barely-true': 'false',
        'pants-fire': 'false'
    }
    dataset['label'] = dataset['label'].map(labels_map)

    return dataset


def save_to_csv(dataset, file_path, file_name):
    """Function to save the dataset in csv format.

    Parameters:
    -----------
    dataset: pandas dataframe
        The dataset to be saved in the csv format.
    file_path: String
        The path where the dataset is to be stored.
    file_name: String
        The name of the saved file.
    """
    complete_file_path_with_name = file_path + file_name
    dataset.to_csv(complete_file_path_with_name, index=False)


# File paths of the dataset to be read
train_path = './datasets/train.tsv'
valid_path = './datasets/valid.tsv'
test_path = './datasets/test.tsv'

train_data = read_tsv(train_path)
valid_data = read_tsv(valid_path)
test_data = read_tsv(test_path)

# Preprocessing the datasets
train_data = preprocess_dataset(train_data)
valid_data = preprocess_dataset(valid_data)
test_data = preprocess_dataset(test_data)

# Path for saving the files
save_path = './datasets/'

# Saving the datasets in csv format
save_to_csv(train_data, save_path, 'train.csv')
save_to_csv(valid_data, save_path, 'valid.csv')
save_to_csv(test_data, save_path, 'test.csv')
