import tensorflow as tf
import numpy as np
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from network_cmm import CMM_NET
from sklearn.decomposition import PCA
import datetime

def get_feature(path, num):
    csv_data = pd.read_csv(path, engine='python')
    csv_data = np.array(csv_data)
    return csv_data[:,:num], csv_data[:,num]

def preprocess(x, y):
    x = tf.cast(x, dtype=tf.float32)
    y = tf.cast(y, dtype=tf.int32)
    return x, y


def main():

    path_csv = r'E:\my_research\transporter_svm\data\pssm_3_gram_zhangli_kerong.csv'

    # csv_data = pd.read_csv(path_csv)

    features, label = get_feature(path_csv, 532)
    pca = PCA(n_components=80)
    features = pca.fit_transform(features)
    train_fea, test_fea, train_label, test_label= train_test_split(features, label, test_size=.1, random_state=0)
    # print(train_fea.shape, train_label.shape, test_label.shape)
    train_fea = tf.expand_dims(train_fea, axis=2)
    # train_label = tf.expand_dims(train_label, axis=1)

    test_fea = tf.expand_dims(test_fea, axis=2)
    # print(test_label)
    # test_label = tf.expand_dims(test_label, axis=1)

    db_train = tf.data.Dataset.from_tensor_slices((train_fea, train_label))
    db_train =db_train.map(preprocess).shuffle(100000).batch(32)

    db_test = tf.data.Dataset.from_tensor_slices((test_fea, test_label))
    db_test = db_test.map(preprocess).batch(32)




    model = CMM_NET()
    # model.build(input_shape)
    learning_r =1e-4
    optimizer = tf.keras.optimizers.Adam(learning_r)


    current_time = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    log_dir = r'E:\my_research\transporter_svm\scripts\log/' + current_time + '-9+16+32+64+80'
    summary_writer = tf.summary.create_file_writer(log_dir)

    for epoch in range(1000):
        acc_num_train = 0
        num_train = 0
        loss_train = 0
        for step, (x, y) in enumerate(db_train):
            # print(x.shape, y.shape)
            with tf.GradientTape() as tape:
                # print(x)
                # print(y.shape)
                logits = model(x, True)

                y_onehot = tf.one_hot(y, depth=2)
                # print(y_onehot)
                # print(logits)
                # tf.losses.binary_crossentropy
                loss = tf.reduce_mean(tf.losses.binary_crossentropy(y_onehot, logits, from_logits=True))
            grads = tape.gradient(loss, model.trainable_variables)
            optimizer.apply_gradients(zip(grads, model.trainable_variables))

            # logits_train = model(x, training = )
            prob = tf.nn.softmax(logits)
            pred = tf.argmax(prob, axis=1)
            pred = tf.cast(pred, dtype=tf.int32)

            correct = tf.equal(y, pred)
            correct = tf.cast(correct, dtype=tf.int32)
            correct = tf.reduce_sum(correct)

            acc_num_train += correct
            num_train += x.shape[0]

            # if step % 100 == 0:
            #     print('epoch:', epoch, 'step:', step, 'loss:', float(loss))
            if step > 1:
                loss_train += loss
                loss_train = loss_train / 2
            with summary_writer.as_default():
                tf.summary.scalar("loss step" + str(epoch), loss, step=step)

        acc_num = 0
        num = 0
        num_one = 0
        acc_num_one = 0
        loss_val = 0
        numm = 0
        for x, y in db_test:
            logits = model(x, False)
            y_onehot = tf.one_hot(y, depth=2)
            loss_test = tf.reduce_mean(tf.losses.binary_crossentropy(y_onehot, logits, from_logits=True))

            if numm > 0:
                loss_val += loss_test
                loss_val = loss_val / 2
            numm += 1

            prob = tf.nn.softmax(logits, axis=1)
            pred =tf.argmax(prob, axis=1)
            pred = tf.cast(pred, dtype=tf.int32)

            correct = tf.equal(y, pred)
            correct = tf.cast(correct, dtype=tf.int32)
            correct =tf.reduce_sum(correct)

            y_one = np.array(y)
            pred_one = np.array(pred)
            # print(y_one)
            # print(pred_one)

            correct_one = 0
            # y_one = list(y_one)
            # pred_one = list(pred_one)
            for i in range(len(y_one)):
                if y_one[i] == 1:
                    num_one += 1
                    if y_one[i] == pred_one[i]:
                        correct_one += 1
            # print(correct_one)
            # print('-'*50)

            acc_num += correct
            acc_num_one += correct_one
            num += x.shape[0]

        # print(num)
        # print(num_one)
        # print(acc_num_one)
        # print(acc_num_one)
        train_acc = acc_num_train / num_train
        acc = acc_num / num
        acc_one = acc_num_one / num_one
        print('epoch', epoch, 'train_acc:', float(train_acc))
        print('epoch:', epoch, 'acc:', float(acc))
        print('epoch:', epoch, 'acc_one:', float(acc_one))

        with summary_writer.as_default():
            tf.summary.scalar('epoch_train_loss', loss_train, step=epoch)
            tf.summary.scalar('epoch_train_acc', train_acc, step=epoch)
            tf.summary.scalar('epoch_val_loss', loss_val, step=epoch)
            tf.summary.scalar('epoch_val_acc', acc, step=epoch)


if __name__ == '__main__':
    main()






# one = tf.ones([5, 5, 10])
#
# sequential = [
#     tf.keras.layers.Conv1D(2, kernel_size=1, padding='same', activation=tf.nn.relu),
#     tf.keras.layers.MaxPool1D(pool_size=2, strides=2, padding='same')
# ]
#
# layers = [
#     tf.keras.layers.Dense(15, activation=tf.nn.sigmoid)
# ]
#
# model = tf.keras.Sequential(sequential)
#
# model.build(input_shape=[None, 5, 10])
#
# # model.summary()
# print(model(one).shape)