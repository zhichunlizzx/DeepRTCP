import tensorflow as tf
import numpy as np

def divede(path_1, path_0):
    with open(path_1, 'r') as r_obj:
        protein_1 = r_obj.readlines()
    # with open(path_0, 'r') as r_obj:
    #     protein_0 = r_obj.readlines()
    id1 = tf.range(8957)
    id1 = tf.random.shuffle(id1)
    train_1,test_1 = tf.gather(protein_1, id1[:2105]), tf.gather(protein_1, id1[2105:])
    train_1,test_1 = np.asarray(train_1), np.asarray(test_1)

    # id0 = tf.range(1940)
    # id0 = tf.random.shuffle(id0)
    # train_0, test_0 = tf.gather(protein_0, id0[:1840]), tf.gather(protein_0, id0[1840:])
    # train_0, test_0 = np.asarray(train_0), np.asarray(test_0)

    with open(r'E:\my_research\transporter_svm\data_2000\pssm_neg_875_1.txt', 'w') as w_obj:
        for pro in train_1:
            w_obj.write(str(pro)[2:-3])
            w_obj.write('\n')
    # with open(r'C:\Users\Asus\Desktop\duibi\train_0.txt', 'w') as w_obj:
    #     for pro in train_0:
    #         w_obj.write(str(pro)[2:-3])
    #         w_obj.write('\n')
    # with open(r'C:\Users\Asus\Desktop\duibi\test_1.txt', 'w') as w_obj:
    #     for pro in test_1:
    #         w_obj.write(str(pro)[2:-3])
    #         w_obj.write('\n')
    # with open(r'C:\Users\Asus\Desktop\duibi\test_0.txt', 'w') as w_obj:
    #     for pro in test_0:
    #         w_obj.write(str(pro)[2:-3])
    #         w_obj.write('\n')


if __name__ == '__main__':
    divede(r'E:\my_research\transporter_svm\data_2000\pssm_neg_id.txt', r'C:\Users\Asus\Desktop\duibi\0.txt')