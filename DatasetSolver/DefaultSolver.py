"""
Provides the default local location of a dataset
    1) Usually the default local dataset is just mock dataset intended to the codebase
       before being deployed on Google Colab instance
"""
import os
from abc import ABC, abstractmethod


class DefaultSolver():

    def __init__(self):
        self.__dataset_directory_to_create = "Dataset"

    # Core functionality
    '''
    Will check for a directory called `Dataset` in the current working directory
    if it does not exist then it will create one
    Returns : the path of the `Dataset` directory
    '''

    def _resolve_base_dir(self):
        dataset_dir_path = f"{os.getcwd()}/{self.__dataset_directory_to_create}"
        if not os.path.exists(dataset_dir_path):
            os.mkdir(dataset_dir_path)

        return dataset_dir_path

    # Abstract Methods
    @abstractmethod
    def resolve_dataset_dir(self):
        pass

