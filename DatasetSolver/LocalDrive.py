"""
Is responsible for resolving the paths for a given dataset
location could be either local or could be coming from a cloud source

"""
import os

# Custom Imports
from DatasetSolver.DefaultSolver import DefaultSolver


# Can be used to directly load the actual dataset from local storage
class LocalDriveDatasetSolver(DefaultSolver):
    def __init__(self):
        super().__init__()

    """
    :returns Absolute Path where the dataset resides, either local, or downloaded from remote
    """

    def resolve_dataset_dir(self):
        # Return the local dataset folder
        return super()._resolve__dataset_base_dir()
