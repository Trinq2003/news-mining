import keras
from keras.models import Sequential
from keras.layers import Embedding, Bidirectional, SimpleRNN, Dropout, Dense
from keras.callbacks import ModelCheckpoint

class SimpleRNNModel:
    def __init__(self):
        self.model = self.build_model()

    def build_model(self, total_words, maxlen):
        model = Sequential()
        model.add(Embedding(total_words, 70, input_length=maxlen))
        model.add(Bidirectional(SimpleRNN(64, dropout=0.1, recurrent_dropout=0.20, activation='tanh', return_sequences=True)))
        model.add(Bidirectional(SimpleRNN(64, dropout=0.1, recurrent_dropout=0.30, activation='tanh', return_sequences=True)))
        model.add(SimpleRNN(32, activation='tanh'))
        model.add(Dropout(0.2))
        model.add(Dense(41, activation='softmax'))
        return model
    
    def train(self, train_padseq, y_train):
        self.model.compile(optimizer='rmsprop',
                    loss='categorical_crossentropy',
                    metrics=['accuracy']
                    )
        # SETUP A EARLY STOPPING CALL and model check point API
        earlystopping = keras.callbacks.EarlyStopping(monitor='accuracy',
                                                    patience=5,
                                                    verbose=1,
                                                    mode='min'
                                                    )
        checkpointer = ModelCheckpoint(filepath='bestvalue',moniter='val_loss', verbose=0, save_best_only=True)
        callback_list = [checkpointer, earlystopping]

        # fit model to the data
        history = self.model.fit(train_padseq, y_train, 
                        batch_size=128, 
                            epochs=15, 
                            validation_split=0.2
                        )