import os
from extract_from_blast import PSSM_20

def pssm_one(path, out_path):
    dir_path = os.listdir(path)

    for dir in dir_path:
        di = dir
        dir = path + dir
        pssm = PSSM_20(dir)
        out = out_path + di[:-5] + '.csv'
        with open(out, 'w') as w_obj:
            for pss in pssm[:-1]:
                w_obj.write(str(pss))
                w_obj.write(',')
            w_obj.write(str(pssm[-1]))


def pssm_one_text(path, out_path):
    with open(path, 'r') as r_obj:
        dir_path = r_obj.readlines()

    for dir in dir_path:
        di = dir
        dir = r'E:\my_research\transporter_svm\data_2000\pssm\neg/' + di[:-1] + '.pssm'
        pssm = PSSM_20(dir)
        out = out_path + di[:-1] + '.csv'
        with open(out, 'w') as w_obj:
            for pss in pssm[:-1]:
                w_obj.write(str(pss))
                w_obj.write(',')
            w_obj.write(str(pssm[-1]))


def all_to_one(dir_path, label, out_path):

    list_dir = os.listdir(dir_path)
    with open(out_path, 'a') as w_obj:
        for dir in list_dir:
            dir = dir_path + dir
            with open(dir, 'r') as r_obj:
                per_csv = r_obj.readlines()
                # print(per_csv[0])

            w_obj.write(per_csv[0] + ',' + label)
            w_obj.write('\n')

def pseaac_to_one(dir_path, label, out_path):
    list_dir = os.listdir(dir_path)
    with open(out_path, 'a') as w_obj:
        for dir in list_dir:
            dir = dir_path + dir
            with open(dir, 'r') as r_obj:
                per_csv = r_obj.readlines()
                per_csv = per_csv[0]
                print(per_csv)
                per_csv = per_csv[2:-5]
            w_obj.write(per_csv + ',' + label)
            w_obj.write('\n')


def get_pseaac(path):
    with open(path, 'r') as r_obj:
        per_pseaac = r_obj.readlines()
        per_pseaac = per_pseaac[0]
        per_pseaac = per_pseaac[2:-5]
        # print(per_pseaac[2:-5])
        # print(path)
    return per_pseaac

def get_t_gram(path):
    with open(path, 'r') as r_obj:
        per_t_gram = r_obj.readlines()
        per_t_gram = per_t_gram[0]
        return per_t_gram

def get_s_gram(path):
    with  open(path, 'r') as r_obj:
        per_s_gram = r_obj.readlines()
        per_s_gram = per_s_gram[0]
        return per_s_gram
def get_pssm(path):
    with  open(path, 'r') as r_obj:
        per_pssm = r_obj.readlines()
        per_pssm = per_pssm[0]
        return per_pssm

def csv_to_one(path_1, path_2, path_3, label, out_path):
    list_dir_1 = os.listdir(path_1)
    with open(out_path, 'a') as w_obj:
        for file in list_dir_1:
            per_path_1 = get_t_gram(path_1 + file)
            per_path_2 = get_pseaac(path_2 + file)
            per_path_3 = get_s_gram(path_3 + file)


            w_obj.write(per_path_1)
            w_obj.write(',')
            w_obj.write(per_path_2)
            w_obj.write(',')
            w_obj.write(per_path_3)
            w_obj.write(',')
            w_obj.write(label)
            w_obj.write('\n')

def two_to_one(path_1, path_2, label, out_path):
    list_dir_1 = os.listdir(path_1)
    with open(out_path, 'a') as w_obj:
        for file in list_dir_1:
            per_path_1 = get_t_gram(path_1 + file)
            # print(path_2 + file)
            per_path_2 = get_pssm(path_2 + file)
            w_obj.write(per_path_1)
            w_obj.write(',')
            w_obj.write(per_path_2)
            w_obj.write(',')
            w_obj.write(label)
            w_obj.write('\n')


def main():
    # path = r'E:\my_research\transporter_svm\data\188D\neg_csv/'
    # out_path = r'E:\my_research\transporter_svm\data\p_s_gram\188D.csv'
    # all_to_one(path, '0', out_path)
    # # pseaac_to_one(path, '1', out_path)


    # rong he te zheng
    path_1 = r'E:\my_research\transporter_svm\data\zhangli_kerong\neg/'
    # path_2 = r'E:\my_research\transporter_svm\data\p_t_gram\pos/'
    path_3 = r'E:\my_research\transporter_svm\data\pssm\pssm_neg_csv/'
    out_path = r'E:\my_research\transporter_svm\data\pssm_3_gram_zhangli_kerong.csv'
    # csv_to_one(path_1,  path_2, path_3, '0', out_path)
    two_to_one(path_1, path_3, '0', out_path)

    # path1 = os.listdir(path_3)
    # for path in path1:
    #     get_pssm(path_3+path)



    # path = r'E:\my_research\transporter_svm\data_2000\neg_2000.txt'
    # out_path = r'E:\my_research\transporter_svm\data_2000\pssm\neg_csv/'
    # pssm_one_text(path, out_path)

if __name__ == '__main__':
    main()