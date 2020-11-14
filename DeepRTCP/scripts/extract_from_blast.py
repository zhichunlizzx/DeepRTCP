import numpy
from math import exp
from math import sqrt
import os


def extra_raw_sss(path):
    with open(path, 'r') as r_obj:
        raw_data = r_obj.readlines()
    raw_data = raw_data[2:]
    a = []
    for data in raw_data:
        data1 = data.split(' ')
        while '' in data1:
            data1.remove('')
        a.append(data1[2])
    return a

def sss_composition(sss, fold):
    l = len(sss)
    return sss.count(fold)/l


def sss_index(sss, fold):
    l = len(sss)
    sum_index = 0
    for step,fo in enumerate(sss):
        if fo == fold:
            sum_index += step
    return sum_index/(l * (l - 1))


def sss_max_index(sss, fold):
    l = len(sss)
    max_index = 0
    for step,fo in enumerate(sss):
        if fo == fold:
            max_index = step
    return max_index/l


def sss_9(path):
    fold = ['H', 'E', 'C']
    sss = []
    raw_sss = extra_raw_sss(path)
    l = len(raw_sss)
    # C
    for s in fold:
        sss.append(sss_composition(raw_sss, s))
    for s in fold:
        sss.append(sss_index(raw_sss, s))
    for s in fold:
        sss.append(sss_max_index(raw_sss, s))
    return sss, l




def extra_pssm_matrix(path):

    with open(path, mode='r') as r_obj:
        raw_data = r_obj.readlines()

    # 然后先筛选行，然后按空格切分
    raw_data = raw_data[3:-6]
    a = []
    for data in raw_data:
        b = data.split(' ')
        while '' in b:
            b.remove('')
        a.append(b[2:22])
        # print(b[2:22])
    return a


def A_i_j(x):
    return 1/(1 + exp(int(x)))


def PSSM_20(path):
    pssm_20 = []
    raw_pssm = extra_pssm_matrix(path)
    l_seq = len(raw_pssm)
    for aac in range(20):
        sum = 0
        for l in range(l_seq):
            sum += A_i_j(raw_pssm[l][aac])
        fre_occ = sum/l_seq
        pssm_20.append(fre_occ)
    # print(pssm_20)
    # print(len(pssm_20))
    return pssm_20

def F(row, raw_pssm):
    l_seq = len(raw_pssm)
    sum = 0
    for i in range(l_seq):
        value = raw_pssm[i][row]
        sum += A_i_j(value)
    sum = sum/l_seq
    return sum


def M(s, t, i, g, raw_pssm):
    l_seq = len(raw_pssm)

    F_s = F(s, raw_pssm)
    F_t = F(t, raw_pssm)
    sum_s = 0
    sum_t = 0
    for j in range(l_seq):
        sum_s += (A_i_j(raw_pssm[j][s]) - F_s)**2
        sum_t += (A_i_j(raw_pssm[j][t]) - F_t)**2
    sum_s = sum_s/l_seq
    sum_s = sqrt(sum_s)
    sum_t = sum_t/l_seq
    sum_t = sqrt(sum_t)
    try:
        M = ((A_i_j(raw_pssm[i][s]) - F_s) * (A_i_j(raw_pssm[i+g][t]) - F_t)) / (sum_s * sum_t)
    except:
        M =0
    return M


def PSSM_380(path):
    pssm_380 = []
    raw_pssm = extra_pssm_matrix(path)
    l_seq = len(raw_pssm)
    for s in range(20):
        for t in range(20):
            if s == t:
                continue
            sum = 0
            g = abs(s - t)
            for i in range(l_seq - g):
                value = M(s, t, i, g, raw_pssm)
                sum += value
            if (l_seq-g) == 0:
                pssm_380.append(0)
                continue
            pssm_value = sum / (l_seq - g)
            pssm_380.append(pssm_value)
    return pssm_380

def PSSM_400(path):
    pssm_400 = []
    raw_pssm = extra_pssm_matrix(path)
    l_seq = len(raw_pssm)
    for s in range(20):
        for t in range(20):
            # if s == t:
            #     continue
            sum = 0
            g = abs(s-t)
            for i in range(l_seq-g):
                value = M(s, t, i, g, raw_pssm)
                sum += value
            pssm_value = sum/(l_seq-g)
            pssm_400.append(pssm_value)
    return pssm_400


def SSS():
    pass



if __name__ == '__main__':
    # path = r'F:\data\PSSM\val\0\passive_pssm_val\P82414.pssm'

    # sum = 0
    # raw_pssm = extra_pssm_matrix(path)
    # for i in range(30 - 4):
    #     value = M(0, 4, i, 4, raw_pssm)
    #     print(value)
    # PSSM_380(path)
    # print(A_i_j(0))
    # p = r'F:\data\PSSM\train\0\passive_pssm\\'
    # path = os.listdir(r'F:\data\PSSM\train\0\passive_pssm\\')
    # for pa in path:
    #     pp = p + pa
        # print(pa)
        # print(PSSM_20(pp))

    path = r'F:\data\SS\train\0\A0B7F3.ss2'
    print(sss_9(path))