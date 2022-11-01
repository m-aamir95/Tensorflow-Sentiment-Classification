import tensorflow as tf

# Custom Imports
from DatasetSolver.GoogleDrive import GoogleDriveSolver
if __name__ == '__main__':


    datasetSolver = GoogleDriveSolver()
    print(datasetSolver.resolve_dataset_dir())
