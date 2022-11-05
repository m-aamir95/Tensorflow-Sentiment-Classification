import tensorflow as tf
from tensorflow import keras
import tensorflow_datasets as tfds
from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences

# Custom Imports
from DatasetSolver.LocalDrive import LocalDriveDatasetSolver
from DatasetLoader.DatasetLoader import load_dataset

if __name__ == '__main__':
    datasetSolver = LocalDriveDatasetSolver()
    base_dir_path = datasetSolver.resolve_dataset_dir()

    (article_links, article_headlines, article_ground_truths) = load_dataset(base_dir_path,
                                                                             "Sarcasm_Headlines_Dataset.json")

    # num_words, will take the top most N words and only encode them
    # Sometimes tokenization and encoding all the word might not improve the accuracy much
    # But can badly effect the training performance because of more computation needed
    # Tokenizer class will also kind of normalize the text e.g removing punctuation, lowercase handling etc.
    tokenizer = Tokenizer(oov_token="<OOV>")
    tokenizer.fit_on_texts(article_headlines)

    # Generating text to sequence on the fit tokenizer
    # Can only provide token indices for the words which it had seen during fitting the call fit_on_texts
    sequences = tokenizer.texts_to_sequences(article_headlines)

    # Padding pre -> applies padding before the original seq Padding post -> applies padding after the original seq
    # Max-length restricts the length of the sequence, else it maps all the seqs according to the longest original
    # present in the corpus Truncating -> specifies in case of truncation where should the truncation start
    padded_seqs = pad_sequences(sequences, padding="post")
    print(padded_seqs.shape)
