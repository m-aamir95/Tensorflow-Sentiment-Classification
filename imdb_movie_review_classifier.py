import numpy as np

import tensorflow as tf
from tensorflow import keras
import tensorflow_datasets as tfds

from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences


def extract_sentences_and_labels_into_numpy_arrays(data_iterable):
    sentences = []
    labels = []
    for text, label in data_iterable:
        sentences.append(text.numpy().decode("utf8"))
        labels.append(label.numpy())

    return np.array(sentences), np.array(labels)


def generate_padded_sequences(sentences, tokenizer, max_seq_length, trunc_type):
    # Generating sequences from provided sentence data
    seqs = tokenizer.texts_to_sequences(sentences)
    # Apply padding
    return pad_sequences(seqs, maxlen=max_seq_length, truncating=trunc_type)


if __name__ == "__main__":
    # Loading imdb movie review dataset
    imdb, info = tfds.load("imdb_reviews", with_info=True, as_supervised=True)
    train_data, test_data = imdb["train"], imdb["test"]

    # Extracting the text part and the label part from both train and test sets
    train_sentences, train_labels = extract_sentences_and_labels_into_numpy_arrays(train_data)
    test_sentences, test_labels = extract_sentences_and_labels_into_numpy_arrays(test_data)

    # Hyper parameters
    vocab_size = 10000
    embedding_dim = 16
    max_seq_length = 120
    trunc_type = "post"
    oov_tok = "<OOV>"
    num_epocs = 10

    # Fit the tokenizer TODO; optimization; Tokenizer, Sequencer, Padder can be multi-threaded, tensorflow probably
    #  already does it and we need to find the method which do it
    tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
    tokenizer.fit_on_texts(train_sentences)

    train_padded_sequences = generate_padded_sequences(train_sentences, tokenizer, max_seq_length, trunc_type)
    test_padded_sequences = generate_padded_sequences(test_sentences, tokenizer, max_seq_length, trunc_type)

    # Defining the neural network with a trainable embedding layer
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_seq_length),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(6, activation="relu"),
        tf.keras.layers.Dense(1, activation="sigmoid")
    ])

    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

    model.fit(train_padded_sequences,
              train_labels,
              epochs=num_epocs,
              validation_data=(test_padded_sequences, test_labels))