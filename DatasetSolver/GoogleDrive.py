"""
Is responsible for resolving the paths for a given dataset
location could be either local or could be coming from a cloud source

"""
from DatasetSolver.DefaultSolver import DefaultSolver


class GoogleDriveSolver(DefaultSolver):
    """
        use_local_mock_dataset, will resolve for local dataset folder is True, default True
    """

    def __init__(self, use_local_mock_dataset=True):
        super().__init__()
        print("Google Drive Solver Initialized")

    def resolve_dataset_dir(self):
        return super()._resolve_base_dir()

