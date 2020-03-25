
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences = [
    'I love my dog',
    'i love my cat',
    'You love my dog!',
    'Do you thin my dog is amazing?'
]

tokenizer = Tokenizer(num_words=100,oov_token="><OOV>")
tokenizer.fit_on_texts(sentences)

word_indexer = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequences,maxlen=5)

print(word_indexer)
print(sequences)
print(padded)

test_data = [
    'i really love my dog',
    'my dog is the best'
]

test_seq = tokenizer.texts_to_sequences(test_data)
padded = pad_sequences(test_seq,maxlen=10)


print(test_seq)
print(padded)