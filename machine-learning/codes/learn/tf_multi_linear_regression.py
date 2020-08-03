import os
import sys

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
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

#另外，这里添加一个额外的固定输入值将权重和偏置结合起来。为此定义函数 append_bias_reshape()。该技巧有时可有效简化编程：
def append_bias_reshape(features, labels):
    m = features.shape[0]
    n = features.shape[1]
    x = np.reshape(np.c_[np.ones(m), features], [m, n + 1]) 
    y = np.reshape(labels, [m, 1])
    return x, y

def train():
    #使用 TensorFlow contrib 数据集加载波士顿房价数据集，并将其分解为 X_train 和 Y_train。可以对数据进行归一化处理：
    # default save path: ~/.keras/datasets/boston_housing.npz
    boston = tf.keras.datasets.boston_housing.load_data()
    boston_data = boston[0]
    X_train, Y_train = boston_data
    #X_train = X_train[:,:12]
    X_train = normalize(X_train)
    print(X_train.shape, Y_train.shape)
    X_train, Y_train = append_bias_reshape(X_train, Y_train)
    print(X_train.shape, Y_train.shape)

    m = len(X_train) # Number of training examples
    n = 13 + 1        # Number of features + bias
    #n = 12

    #为训练数据声明 TensorFlow 占位符：
    X = tf.placeholder(tf.float32, name = 'X', shape=[m,n])
    Y = tf.placeholder(tf.float32, name = 'Y')

    #创建 TensorFlow 的权重
    w = tf.Variable(tf.random_normal([n, 1]), name = 'weight')

    #定义用于预测的线性回归模型和损失函数
    Y_hat = tf.matmul(X, w)
    loss = tf.reduce_mean(tf.square(Y - Y_hat, name = 'loss')) + 0.6 * tf.nn.l2_loss(w)

    #选择梯度下降优化器
    optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.01, name='GradientDescentOptimizer').minimize(loss)
    #optimizer = tf.train.AdamOptimizer().minimize(loss)
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
            _, l = sess.run([optimizer, loss], feed_dict = {X:X_train, Y:Y_train})
            total.append(l)
            print('Epoch {0}: Loss {1}'.format(i, l))
        writer.close()

    #查看结果
    plt.plot(total)
    plt.show()

if __name__ == '__main__':
    train()
