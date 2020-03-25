from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

import json
file_path = "C://Users//nle5257//projects//github//sarcasm-dataset//Sarcasm_Headlines_Dataset.json"

sentences = []
labels = []
urls = []


with open(file_path, 'r') as f:
    for line in f:
        data = json.loads(line)
        sentences.append(data['headline'])
        labels.append(data['is_sarcastic'])
        urls.append(data['article_link'])

tokenizer = Tokenizer(oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index


sequences = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequences,padding='post')

print(sentences[2])
print(padded[2])
print(padded.shape)