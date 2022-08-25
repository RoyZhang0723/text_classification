import nltk
import tensorflow_text as text
import pandas as pd
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.keras import utils
from tensorflow.keras.layers import TextVectorization, Dense, Input, Embedding
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten
from keras.models import Model


nltk.download('stopwords')
train = pd.read_csv("data.csv")
train = train.dropna(axis=0,how='any') #drop all rows that have any NaN values
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
# turn lowercase
train['cleaned_text'] = train['abstract'].apply(lambda x: " ".join(x.lower() for x in x.split()))

# remove punctuations
train['cleaned_text'] = train['cleaned_text'].str.replace('[^\w\s]','')

# remove stopwords
train['cleaned_text'] = train['cleaned_text'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))
train.head(100)

bert_preprocess = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3")
bert_encoder = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4")

def get_sentence_embeding(sentences):
    preprocessed_text = bert_preprocess(sentences)
    return bert_encoder(preprocessed_text)['pooled_output']
# get_sentence_embeding("500$ discount. hurry up")
label = train["label"][:]
all_text = np.array(train["cleaned_text"]).tolist()
vec = get_sentence_embeding(all_text[:20])

x = Conv1D(128, 5, activation='relu')(vec)
x = MaxPooling1D(5)(x)
x = Conv1D(128, 5, activation='relu')(x)
x = MaxPooling1D(5)(x)
x = Conv1D(128, 5, activation='relu')(x)
x = MaxPooling1D(35)(x)
x = Flatten()(x)
x = Dense(128, activation='relu')(x)
preds = Dense(13, activation='softmax')(x)

model = Model(vec, preds)
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['acc'])
