import tensorflow as tf

# Custom Imports
from DatasetSolver.GoogleDrive import GoogleDriveDatasetSolver

if __name__ == '__main__':

    google_drive_public_links = ["https://drive.google.com/file/d/1J_3eaU1JmZN0l_mTvPYfeFfMhxy-ZCJL/view"]

    datasetSolver = GoogleDriveDatasetSolver(google_drive_public_links)
    base_dir_path = datasetSolver.resolve_dataset_dir()