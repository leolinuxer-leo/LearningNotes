# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np

print(tf.__version__)

# 加载数据、区分出测试数据和训练数据
# 注意：如果已经下过，重复下载的话，可能会出现EOFError: Compressed file ended before the end-of-stream marker was reached错误

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# 分类的列表
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# 查看数据的值
print(train_images.shape)  # 样本的shape(可以看出有多少条样本、维度)
print(len(train_labels))  # label的个数，有多少个样本，就应该有多少个label
print(train_labels)  # label的值，对应上面分类列表(从0到9)


# 对测试数据和训练数据进行预处理(实际上就是归一化)
train_images = train_images / 255.0
test_images = test_images / 255.0

# 设置层  (初始处理)--- 建立神经层
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])


# 损失函数、优化器、指标
model.compile(
              #optimizer=tf.train.AdamOptimizer(),
              #optimizer=tf.optimizers.Adam(),
              #optimizer=tf.compat.v1.train.MomentumOptimizer(learning_rate=0.05, momentum=0.9),
              optimizer=tf.compat.v1.train.MomentumOptimizer(learning_rate=0.05, momentum=0.9, use_nesterov=True)
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 将训练集丢进去，训练出模型(Model)
model.fit(train_images, train_labels, epochs=5)

# 将测试数据丢到模型中，评估一下得分(准确率)
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)

# 评估完准确率以后，我们可以对测试数据进行预测
predictions = model.predict(test_images)

# 选第一个样本预测后的得出最有可能结果
print(np.argmax(predictions[0]))

# 对比结果
print(test_labels[0])
