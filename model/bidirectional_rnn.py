from keras.models import Sequential
from keras.layers import Embedding, Bidirectional, SimpleRNN, Dropout, Dense
from keras.models import load_model
from keras.layers import GRU, LSTM, Conv1D, MaxPooling1D

class BidirectionalRNN:
    def __init__(self, config):
        self.config = config
        self.model = self.build_model()

    def build_model(self, total_words, maxlen):
        model = Sequential()
        model.add(Embedding(total_words, 100, input_length=maxlen))
        model.add(Bidirectional(LSTM(64, dropout=0.1, recurrent_dropout=0.10, activation='tanh', return_sequences=True)))
        model.add(Bidirectional(LSTM(64, dropout=0.2, recurrent_dropout=0.20, activation='tanh', return_sequences=True)))
        model.add(Bidirectional(SimpleRNN(64, dropout=0.2, recurrent_dropout=0.20, activation='tanh', return_sequences=True)))
        model.add(Conv1D(72, 3, activation='relu'))
        model.add(MaxPooling1D(2))
        model.add(SimpleRNN(64, activation='tanh', dropout=0.2, recurrent_dropout=0.20, return_sequences=True))
        model.add(GRU(64, recurrent_dropout=0.20, recurrent_regularizer='l1_l2'))
        model.add(Dropout(0.2))
        model.add(Dense(41, activation='softmax'))
        model.summary()
        return model

    def train(self, x_train, y_train, x_val, y_val):
        self.model.fit(x_train, y_train,
                       batch_size=self.config.batch_size,
                       epochs=self.config.num_epochs,
                       validation_data=(x_val, y_val))

    def evaluate(self, x_test, y_test):
        loss, accuracy = self.model.evaluate(x_test, y_test,
                                             batch_size=self.config.batch_size)
        print('loss: %f, accuracy: %f' % (loss, accuracy))

    def predict(self, x):
        y_pred = self.model.predict(x)
        return y_pred

    def save(self, path):
        self.model.save(path)

    def load(self, path):
        self.model = load_model(path)

if __name__ == '__main__':
    from config import Config
    config = Config()
    model = BidirectionalRNN(config)
    model.build_model(10000, 100)