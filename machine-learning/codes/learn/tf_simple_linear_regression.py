import os
import sys

#import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
import matplotlib.pyplot as plt

#定义一个函数来归一化输入数据
def normalize(X):
    mean = np.mean(X)
    std = np.std(X)
    X = (X - mean) / std
    return X

def train():
    #使用 TensorFlow contrib 数据集加载波士顿房价数据集，并将其分解为 X_train 和 Y_train。可以对数据进行归一化处理：
    # default save path: ~/.keras/datasets/boston_housing.npz
    boston = tf.keras.datasets.boston_housing.load_data()
    boston_data = boston[0]
    X_train, Y_train = boston_data
    #选择第6维特征：RM (average number of rooms per dwelling)
    X_train = X_train[:, 5]
    X_train = normalize(X_train)
    n_samples = X_train.shape[0]

    #为训练数据声明 TensorFlow 占位符：
    X = tf.placeholder(tf.float32, name = 'X')
    Y = tf.placeholder(tf.float32, name = 'Y')

    #创建 TensorFlow 的权重和偏置变量且初始值为零    
    w = tf.Variable(0.0, name = 'weight')
    b = tf.Variable(0.0, name = 'bias')

    #定义用于预测的线性回归模型和损失函数
    Y_hat = X * w + b
    #Y_hat = tf.tensordot(X, w, axes=1) + b
    loss = tf.square(Y - Y_hat, name = 'loss')

    #选择梯度下降优化器
    #optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.1, name='GradientDescentOptimizer').minimize(loss)
    optimizer = tf.train.AdamOptimizer().minimize(loss)
    #optimizer = tf.train.MomentumOptimizer(learning_rate=0.05, momentum=0.9, use_nesterov=True).minimize(loss)

    #声明初始化操作符
    init_op = tf.global_variables_initializer()
    total = []

    #现在，开始计算图，训练 100 次：
    with tf.Session() as sess:
        # Initialize variables
        sess.run(init_op)

        writer = tf.summary.FileWriter('graphs', sess.graph)

        #Train the model for 100 times
        for i in range(100):
            total_loss = 0
            for x, y in zip(X_train, Y_train):
                _, l = sess.run([optimizer, loss], feed_dict = {X:x, Y:y})
                total_loss += l 
            total.append(total_loss / n_samples)
            print('Epoch {0}: Loss {1}'.format(i, total_loss/n_samples))
        writer.close()
        b_value, w_value = sess.run([b, w])

    #查看结果
    Y_pred = X_train * w_value + b_value
    print('Done')
    
    plt.plot(X_train, Y_train, 'bo', label = 'Real Data')
    plt.plot(X_train, Y_pred, 'r', label = 'Predicted Data')
    plt.legend()
    plt.show()
    plt.plot(total)
    plt.show()

if __name__ == '__main__':
    train()
