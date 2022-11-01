import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.text import Tokenizer

# Custom Imports
from DatasetSolver.GoogleDrive import GoogleDriveDatasetSolver

if __name__ == '__main__':

    google_drive_public_links = ["https://drive.google.com/file/d/1J_3eaU1JmZN0l_mTvPYfeFfMhxy-ZCJL/view"]

    datasetSolver = GoogleDriveDatasetSolver(google_drive_public_links)
    base_dir_path = datasetSolver.resolve_dataset_dir()

    sentences = ["I love my dog", "I love my cat"]

    # num_words, will take the top most N words and only encode them
    tokenizer = Tokenizer(num_words=100)
    tokenizer.fit_on_texts(sentences)

    word_index = tokenizer.word_index
    print("Tokenizer Output")
    print(word_index)

