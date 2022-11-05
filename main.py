import tensorflow as tf
from tensorflow import keras
from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
# Custom Imports
from DatasetSolver.LocalDrive import LocalDriveDatasetSolver

if __name__ == '__main__':

    datasetSolver = LocalDriveDatasetSolver()
    base_dir_path = datasetSolver.resolve_dataset_dir()

    sentences = ["I love my dog",
                 "i love my cat",
                 "You LOVE my dog!",
                 "Do you think my dog is amazing?"]


    # num_words, will take the top most N words and only encode them
    # Sometimes tokenization and encoding all the word might not improve the accuracy much
    # But can badly effect the training performance because of more computation needed
    # Tokenizer class will also kind of normalize the text e.g removing punctuation, lowercase handling etc.
    tokenizer = Tokenizer(num_words=100, oov_token="<OOV>")
    tokenizer.fit_on_texts(sentences)

    # Generating text to sequence on the fit tokenizer
    # Can only provide token indices for the words which it had seen during fitting the call fit_on_texts
    sequences = tokenizer.texts_to_sequences(sentences)

    #Apply padding
    # Padding pre -> applies padding before the original seq
    # Padding post -> applies padding after the original seq
    # Max-length restricts the length of the sequence, else it maps all the seqs according to the longest original present in the corpus
    # Truncating -> specifies incasse of truncation where should the truncation start
    padded_seqs = pad_sequences(sequences, padding="post", maxlen=5, truncating="post")
    print(padded_seqs)
