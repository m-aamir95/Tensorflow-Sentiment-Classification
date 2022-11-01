"""
Is responsible for resolving the paths for a given dataset
location could be either local or could be coming from a cloud source

"""
import os

import gdown
import zipfile
import tarfile

# Custom Imports
from DatasetSolver.DefaultSolver import DefaultSolver


class GoogleDriveDatasetSolver(DefaultSolver):
    def __init__(self, google_drive_public_links=None, verbose=False):
        super().__init__()
        self.google_drive_public_links = google_drive_public_links
        self.verbose = verbose

    """
    :returns Absolute Path where the dataset resides, either local, or downloaded from remote
    """

    def resolve_dataset_dir(self):
        # Return the local mock dataset folder
        base_dir = super()._resolve__dataset_base_dir()
        # if super()._check_for_local_execution_environment_file_exist():
        # return base_dir

        # Cloud platform specific download mechanism
        for index, google_drive_public_link in enumerate(self.google_drive_public_links):
            compressed_file_abs_path = base_dir + "/zip_" + str(index)
            # TODO; Improvement; can be Multi-threaded
            gdown.download(url=google_drive_public_link,
                           output=compressed_file_abs_path,
                           quiet=self.verbose,
                           fuzzy=True)

            # TODO; Improvement; can be Multi-threaded
            with zipfile.ZipFile(compressed_file_abs_path) as zipped_file:
                zipped_file.extractall(path=base_dir)

            # TODO; feature; Provided a parameter called post-cleanup remove downloaded zip files

        return base_dir
