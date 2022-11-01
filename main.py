import tensorflow as tf

# Custom Imports
from DatasetSolver.GoogleDrive import GoogleDriveDatasetSolver

if __name__ == '__main__':
    datasetSolver = GoogleDriveDatasetSolver()
    print(datasetSolver.resolve_dataset_dir())
