import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras import backend as K
from tensorflow.keras.layers import Layer
import matplotlib.pyplot as plt
import numpy as np



# RBF --Radial Basis Function Network
class RBFLayer(Layer):
    def __init__(self, units, gamma, **kwargs):
        super(RBFLayer, self).__init__(**kwargs)
        self.units = units
        self.gamma = K.cast_to_floatx(gamma)

    def build(self, input_shape):
        self.mu = self.add_weight(name='mu',
                                  shape=(int(input_shape[1]), self.units),
                                  initializer='uniform',
                                  trainable=True)
        super(RBFLayer, self).build(input_shape)

    def call(self, inputs):
        diff = K.expand_dims(inputs) - self.mu
        l2 = K.sum(K.pow(diff,2), axis=1)
        res = K.exp(-1 * self.gamma * l2)
        return res

    def compute_output_shape(self, input_shape):
        return (input_shape[0], self.units)




# MNIST Data 다운로드 및 데이터 확인
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 정규화
x_train, x_test = x_train / 255.0, x_test / 255.0

x_train=x_train.reshape(-1,28,28,1)
x_test=x_test.reshape(-1,28,28,1)

print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)



# Lenet-5
model = models.Sequential()
# C1
model.add(layers.Conv2D(filters=6,kernel_size=5, activation='tanh', input_shape=(28, 28, 1), padding='same', name='C1'))
# S2
model.add(layers.AvgPool2D(pool_size=(2,2), strides=(2,2),name='S2'))
# C3
model.add(layers.Conv2D(filters=16,kernel_size=5, activation='tanh',name='C3'))
# S4
model.add(layers.AveragePooling2D(pool_size=(2, 2), strides=(2,2),name='S4'))
# C5
model.add(layers.Conv2D(filters=120,kernel_size=5, activation='tanh',name='C5'))
# F6
model.add(layers.Flatten())
model.add(layers.Dense(84, activation='tanh',name='F6'))
# Output
model.add(layers.Dense(10, activation=RBFLayer(10, 0.5)))
#model.add(layers.Dense(10, activation='softmax',name='Output'))

# 모델 확인
model.summary()


model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


hist=model.fit(x=x_train, y=y_train, epochs=20, batch_size=128, validation_data=(x_test,y_test), verbose=1)
test_score=model.evaluate(x_test, y_test)
print("Test loss {:.4f}, accuracy {:.2f}%".format(test_score[0], test_score[1] * 100))

model.save("./")



# plot 그리기
f, ax = plt.subplots()
ax.plot([None] + hist.history['accuracy'], 'o-')
ax.plot([None] + hist.history['val_accuracy'], 'x-')
ax.legend(['Train acc', 'Val acc'], loc = 0)
ax.set_title('Training/Validation acc per Epoch')
ax.set_xlabel('Epoch')
ax.set_ylabel('acc')
plt.show()

import matplotlib.pyplot as plt
f, ax = plt.subplots()
ax.plot([None] + hist.history['loss'], 'o-')
ax.plot([None] + hist.history['val_loss'], 'x-')
# Plot legend and use the best location automatically: loc = 0.
ax.legend(['Train Loss', 'Val Loss'], loc = 0)
ax.set_title('Training/Validation Loss per Epoch')
ax.set_xlabel('Epoch')
ax.set_ylabel('Loss')
plt.show()



# 모델 로드
model = models.load_model('./')

# 클래스
class_names = ['0','1','2','3','4','5','6','7','8','9']

prediction_values = model.predict_classes(x_test)

# 이미지 로드해서 모델 결과값과 함께 plot 그리기
fig = plt.figure(figsize=(15, 7))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

for i in range(30):
    ax = fig.add_subplot(5, 6, i + 1, xticks=[], yticks=[])
    ax.imshow(x_test[i, :].reshape((28, 28)), cmap=plt.cm.gray_r, interpolation='nearest')
    ax.text(0, 7, class_names[prediction_values[i]], color='red')

plt.show()