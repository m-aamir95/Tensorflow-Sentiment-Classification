import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.text import Tokenizer

# Custom Imports
from DatasetSolver.LocalDrive import LocalDriveDatasetSolver

if __name__ == '__main__':

    datasetSolver = LocalDriveDatasetSolver()
    base_dir_path = datasetSolver.resolve_dataset_dir()

    sentences = ["I love my dog", "i love my cat", "You LOVE my dog!"]

    # num_words, will take the top most N words and only encode them
    # Sometimes tokenization and encoding all the word might not improve the accuracy much
    # But can badly effect the training performance because of more computation needed
    # Tokenizer class will also kind of normalize the text e.g removing punctuation, lowercase handling etc.
    tokenizer = Tokenizer(num_words=100)
    tokenizer.fit_on_texts(sentences)

    word_index = tokenizer.word_index
    print("Tokenizer Output")
    print(word_index)

