import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.text import Tokenizer

# Custom Imports
from DatasetSolver.LocalDrive import LocalDriveDatasetSolver

if __name__ == '__main__':

    datasetSolver = LocalDriveDatasetSolver()
    base_dir_path = datasetSolver.resolve_dataset_dir()

    sentences = ["I love my dog", "I love my cat"]

    # num_words, will take the top most N words and only encode them
    tokenizer = Tokenizer(num_words=100)
    tokenizer.fit_on_texts(sentences)

    word_index = tokenizer.word_index
    print("Tokenizer Output")
    print(word_index)

