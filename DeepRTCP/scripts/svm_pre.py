import numpy as np
import matplotlib.pyplot as plt
# from sklearn import svm
from sklearn.metrics import roc_curve, auc
from sklearn.svm import SVC
from extract_from_blast import PSSM_20,PSSM_380,sss_9
import os
import pandas as pd
pathh = r'F:\data\SS\val\val_750.csv'
import roc


def get_csv_PSSM_20(path_1, path_0):
    path_list_1 = os.listdir(path_1)
    path_list_0 = os.listdir(path_0)
    l_1, l_0 = len(path_list_1), len(path_list_0)

    # x = np.zeros(l_1+l_0, 20)
    x = []
    y_1 = np.ones(l_1)
    y_0 = np.ones(l_0)
    y = np.append(y_1, y_0)

    for p in path_list_1:
        pth = path_1 + p
        pssm, l_ss= PSSM_20(pth)
        # print(pssm)
        if l_ss > 750:
            continue
        with open(pathh, 'a') as w_obj:
            # for d in range(21):
            #     w_obj.write(str(d))
            # w_obj.write('\n')
            for pss in pssm:
                w_obj.write(str(pss))
                w_obj.write(',')
            w_obj.write('1')
            w_obj.write('\n')
        x.append(pssm)
    for p in path_list_0:
        pth = path_0 + p
        pssm, l_se = PSSM_20(pth)
        if l_se > 750:
            continue
        with open(pathh, 'a') as w_obj:
            for pss in pssm:
                w_obj.write(str(pss))
                w_obj.write(',')
            w_obj.write('0')
            w_obj.write('\n')
        x.append(pssm)
    x = np.array(x)
    print(x)
    # return x, y

def get_csv_PSSM_380(path_1, path_0):
    path_list_1 = os.listdir(path_1)
    path_list_0 = os.listdir(path_0)
    l_1, l_0 = len(path_list_1), len(path_list_0)

    # x = np.zeros(l_1+l_0, 20)
    # x = []
    y_1 = np.ones(l_1)
    y_0 = np.ones(l_0)
    y = np.append(y_1, y_0)

    for p in path_list_1:
        pth = path_1 + p
        pssm = PSSM_380(pth)
        # print(pssm)
        with open(pathh, 'a') as w_obj:
            # for d in range(381):
            #     w_obj.write(str(d))
            # w_obj.write('\n')
            for pss in pssm:
                w_obj.write(str(pss))
                w_obj.write(',')
            w_obj.write('1')
            w_obj.write('\n')
        # x.append(pssm)
    for p in path_list_0:
        pth = path_0 + p
        pssm = PSSM_380(pth)
        with open(pathh, 'a') as w_obj:
            for pss in pssm:
                w_obj.write(str(pss))
                w_obj.write(',')
            w_obj.write('0')
            w_obj.write('\n')
        # x.append(pssm)
    # x = np.array(x)
    # print(x)

def get_csv_sss9(path_1, path_0):
    path_list_1 = os.listdir(path_1)
    path_list_0 = os.listdir(path_0)
    l_1, l_0 = len(path_list_1), len(path_list_0)

    # x = np.zeros(l_1+l_0, 20)
    # x = []
    y_1 = np.ones(l_1)
    y_0 = np.ones(l_0)
    y = np.append(y_1, y_0)
    for p in path_list_1:
        pth = path_1 + p
        pssm, l_ss = sss_9(pth)
        if l_ss > 750:
            continue
        # print(pssm)
        with open(pathh, 'a') as w_obj:
            # for d in range(10):
            #     w_obj.write(str(d))
            # w_obj.write('\n')
            for pss in pssm:
                w_obj.write(str(pss))
                w_obj.write(',')
            w_obj.write('1')
            w_obj.write('\n')
        # x.append(pssm)
    for p in path_list_0:
        pth = path_0 + p
        pssm, l_ss = sss_9(pth)
        if l_ss > 750:
            continue
        with open(pathh, 'a') as w_obj:
            for pss in pssm:
                w_obj.write(str(pss))
                w_obj.write(',')
            w_obj.write('0')
            w_obj.write('\n')



def get_PSSM_20(path):
    csv_data = pd.read_csv(path)
    # print(csv_data)
    csv_data = np.array(csv_data)
    return csv_data[:,:20], csv_data[:,20]
    # print(csv_data[:,20])

def get_PSSM_380(path):
    csv_data = pd.read_csv(path)
    csv_data = np.array(csv_data)
    return csv_data[:, :380], csv_data[:, 380]


def get_sss_9(path):
    csv_data = pd.read_csv(path)
    csv_data = np.array(csv_data)
    return csv_data[:, :9], csv_data[:, 9]

def main():
    svm_class = SVC(C=10000, gamma=0.00001, kernel='rbf')
    train_path_1 = r'F:\data\PSSM\train\train.csv'
    train_path_0 = r'F:\data\PSSM\val\val_750.csv'
    # train_path_111 = r'F:\data\PSSM\val\val_1.csv'
    train_fea,train_label = get_PSSM_20(train_path_1)
    val_fea, val_label =  get_PSSM_20(train_path_0)
    # val_1_fea, val_1_label = get_PSSM_20(train_path_111)
    # print(train_fea)
    # print(train_label.shape)
    a = svm_class.fit(train_fea, train_label)
    y_score = a.decision_function(val_fea)
    fpr, tpr, threshold = roc_curve(val_label, y_score)
    roc_auc = auc(fpr, tpr)
    pre = a.predict(val_fea)
    num = 0
    pos =0
    for i in range(len(pre)):
        if pre[i] == val_label[i]:
            num += 1
            if pre[i] == 1:
                pos += 1
    with open(r'H:\script\pssm\y_score.txt','w') as w_obj:
        for score in y_score:
            w_obj.write(str(score))
            w_obj.write('\n')
    print(num)
    print(num/len(pre))
    print(pos)
    # print(y_score)
    '''
    svm_class = SVC(C=10000, gamma=0.00001, kernel='rbf')
    train_path_1 = r'F:\data\PSSM\train\train_380.csv'
    train_path_0 = r'F:\data\PSSM\val\val_750_380.csv'
    # train_path_111 = r'F:\data\PSSM\val\val_1.csv'
    train_fea, train_label = get_PSSM_380(train_path_1)
    val_fea, val_label = get_PSSM_380(train_path_0)
    # val_1_fea, val_1_label = get_PSSM_20(train_path_111)
    # print(train_fea)
    # print(train_label.shape)
    a = svm_class.fit(train_fea, train_label)
    y_score_80 = a.decision_function(val_fea)
    fpr_80, tpr_80, threshold = roc_curve(val_label, y_score_80)
    roc_auc_80 = auc(fpr_80, tpr_80)
    pre = a.predict(val_fea)
    num = 0
    pos = 0
    for i in range(len(pre)):
        if pre[i] == val_label[i]:
            num += 1
            if pre[i] == 1:
                pos += 1
    with open(r'H:\script\pssm\y_score.txt', 'w') as w_obj:
        for score in y_score:
            w_obj.write(str(score))
            w_obj.write('\n')
    print(num)
    print(num / len(pre))
    print(pos)

    svm_class = SVC(C=100000, gamma=0.01, kernel='rbf')
    train_path_1 = r'F:\data\SS\train\train.csv'
    train_path_0 = r'F:\data\SS\val\val_750.csv'
    # train_path_111 = r'F:\data\PSSM\val\val_1.csv'
    train_fea, train_label = get_sss_9(train_path_1)
    val_fea, val_label = get_sss_9(train_path_0)
    # val_1_fea, val_1_label = get_PSSM_20(train_path_111)
    # print(train_fea)
    # print(train_label.shape)
    a = svm_class.fit(train_fea, train_label)
    y_score = a.decision_function(val_fea)
    fpr_ss, tpr_ss, threshold = roc_curve(val_label, y_score)
    roc_auc_ss = auc(fpr_ss, tpr_ss)
    pre = a.predict(val_fea)
    num = 0
    pos = 0
    for i in range(len(pre)):
        if pre[i] == val_label[i]:
            num += 1
            if pre[i] == 1:
                pos += 1
    with open(r'H:\script\pssm\y_score.txt', 'w') as w_obj:
        for score in y_score:
            w_obj.write(str(score))
            w_obj.write('\n')
    print(num)
    print(num / len(pre))
    print(pos)

    y_score_1 = roc.y_score(22)
    y_label_1 = roc.y_label(475, 481)
    fpr_1, tpr_1, threshold = roc_curve(y_label_1, y_score_1)
    roc_auc_1 = auc(fpr, tpr)
    '''





    '''
    plt.figure()
    lw = 1
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='Pssm_380 (area = %0.2f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
    plt.plot(fpr_80, tpr_80, color='darkblue',
             lw=lw, label='Pssm_20 (area = %0.2f)' % roc_auc_80)
    plt.plot(fpr_ss, tpr_ss, color='darkviolet',
             lw=lw, label='SS (area = %0.2f)' % roc_auc_ss)
    plt.plot(fpr_1, tpr_1, color='black',
             lw=lw, label='DeepCM (area = %0.2f)' % roc_auc_1)

    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
    plt.show()
    '''


    # pre = a.predict(val_1_fea)
    # num = 0
    # for i in range(len(pre)):
    #     if pre[i] == val_1_label[i]:
    #         num += 1
    # print(num)
    # print(num / len(pre))

if __name__ == '__main__':
    # main()
    train_path_1 = r'F:\data\SS\val\1/'
    train_path_0 = r'F:\data\SS\val\0/'
    get_csv_PSSM_20(train_path_1, train_path_0)
    # get_csv_PSSM_380(train_path_1, train_path_0)
    # get_csv_sss9(train_path_1, train_path_0)