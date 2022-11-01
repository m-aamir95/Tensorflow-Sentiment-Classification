"""
Is responsible for resolving the paths for a given dataset
location could be either local or could be coming from a cloud source

"""
from DatasetSolver.DefaultSolver import DefaultSolver


class GoogleDriveDatasetSolver(DefaultSolver):
    def __init__(self):
        super().__init__()

    """
    :returns Absolute Path where the dataset resides
    """

    def resolve_dataset_dir(self):
        # Return the local mock dataset folder
        if super()._check_for_local_execution_environment_file_exist():
            return super()._resolve_base_dir()

        # Cloud platform specific download mechanism
