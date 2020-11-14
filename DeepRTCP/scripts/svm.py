import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import roc_curve, auc
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score, train_test_split, KFold

import os
import pandas as pd
from sklearn.decomposition import PCA


def get_t_gram(path):
    csv_data = pd.read_csv(path)
    csv_data = np.array(csv_data)
    return csv_data[:, :512], csv_data[:, 512]

def get_pseaac(path):
    csv_data = pd.read_csv(path)
    csv_data = np.array(csv_data)
    return csv_data[:, :30], csv_data[:, 30]

def get_PSSM_20(path):
    csv_data = pd.read_csv(path)
    # print(csv_data)
    csv_data = np.array(csv_data)
    return csv_data[:,:20], csv_data[:,20]
    # print(csv_data[:,20])

def get_feature(path, num):
    csv_data = pd.read_csv(path, engine='python')
    csv_data = np.array(csv_data)
    return csv_data[:,:num], csv_data[:,num]


def main():

    path = r'E:\my_research\transporter_svm\data_2000\csv\pssm_3_gram_zhangli_kerong.csv'
    # fea, label = get_t_gram(path)
    # fea, label = get_PSSM_20(path)
    result = []

    for ii in range(532):
        if ii == 0:
            continue
        fea, label = get_feature(path, 532)
        pca = PCA(n_components=80)
        reduced = pca.fit_transform(fea)
        # print(label)
        # x_train, x_test, y_train, y_test = train_test_split(fea, label, test_size=.1, random_state=0)

        # print(y_train)
        # print(y_test)
        # print(fea.shape)
        # print(label.shape)
        svm = SVC(C=100000,gamma='auto', kernel='rbf')
        # svm_class = svm.fit(fea, label)
        # pre = svm_class.predict(fea)
        # num = 0
        # for i in range(len(pre)):
        #     if pre[i] == label[i]:
        #         num += 1
        # acc = num / len(pre)
        # print(acc)

        # pca = PCA(n_components=200)
        # reduced = pca.fit_transform(fea)creat_ecah_protein_file.py




        scores = cross_val_score(svm, reduced, label, cv=10, scoring='accuracy')
        # print(scores)
        result.append(scores.mean())
        print(scores.mean())
        # scores = cross_val_score(svm, reduced, label, cv=10, scoring='recall')
        # print(scores)
        # print(scores.mean())
        # scores = cross_val_score(svm,reduced, label, cv=10, scoring='precision')
        # print(scores)
        # print(scores.mean())
        # scores = cross_val_score(svm, reduced, label, cv=10, scoring='f1')
        # print(scores)
        # print(scores.mean())

    with open(r'E:\my_research\transporter_svm\PTC.txt', 'w') as w_obj:
        for re in result:
            w_obj.write(str(re))
            w_obj.write('\n')

        # kf = KFold(n_splits=3)
        # for train, test in kf.split(fea):
        #     print(label[train].shape)
        #     print(str(label[train]))
        #     print(str(label[train]).count('0'))
        #     print(label[test])

if __name__ == '__main__':
    main()