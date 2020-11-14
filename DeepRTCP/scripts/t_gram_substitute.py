from Bio import SeqIO
import os

def t_gram_7_shushui_zhangli(path):

    for data in SeqIO.parse(path, 'fasta'):
        seq = data.seq
    seq = str(seq)
    seq = seq.replace('R', 'D')
    seq = seq.replace('Q', 'D')
    seq = seq.replace('N', 'D')
    seq = seq.replace('K', 'E')
    seq = seq.replace('H', 'A')
    seq = seq.replace('G', 'A')
    seq = seq.replace('T', 'S')
    seq = seq.replace('Y', 'P')
    seq = seq.replace('W', 'F')
    seq = seq.replace('I', 'F')
    seq = seq.replace('L', 'F')
    seq = seq.replace('M', 'F')
    seq = seq.replace('V', 'F')

    p_aa = ['A', 'C', 'D', 'E', 'F', 'P', 'S']
    t_gram_512 = []

    for  aa_i in p_aa:
        for aa_j in p_aa:
            for aa_k in p_aa:
                aa_t = aa_i + aa_j + aa_k
                t_gram_512.append(aa_t)
    # print(len(t_gram_512))
    t_gram = []
    for t in t_gram_512:
        num = seq.count(t)
        num = num / (len(seq) - 2)
        t_gram.append(num)
    return t_gram

def t_gram_5_shushui_kerong(path):

    for data in SeqIO.parse(path, 'fasta'):
        seq = data.seq
    seq = str(seq)
    seq = seq.replace('N', 'D')
    seq = seq.replace('E', 'D')
    seq = seq.replace('Q', 'D')
    seq = seq.replace('R', 'D')
    seq = seq.replace('K', 'D')
    seq = seq.replace('G', 'A')
    seq = seq.replace('S', 'H')
    seq = seq.replace('P', 'H')
    seq = seq.replace('Y', 'H')
    seq = seq.replace('T', 'H')
    seq = seq.replace('F', 'C')
    seq = seq.replace('I', 'C')
    seq = seq.replace('V', 'C')
    seq = seq.replace('W', 'C')
    seq = seq.replace('L', 'C')

    p_aa = ['A', 'C', 'D', 'H', 'M']
    t_gram_512 = []

    for  aa_i in p_aa:
        for aa_j in p_aa:
            for aa_k in p_aa:
                aa_t = aa_i + aa_j + aa_k
                t_gram_512.append(aa_t)
    # print(len(t_gram_512))
    t_gram = []
    for t in t_gram_512:
        num = seq.count(t)
        num = num / (len(seq) - 2)
        t_gram.append(num)
    return t_gram

def t_gram_5_shushui_dianji(path):

    for data in SeqIO.parse(path, 'fasta'):
        seq = data.seq
    seq = str(seq)
    seq = seq.replace('R', 'D')
    seq = seq.replace('K', 'D')
    seq = seq.replace('Q', 'D')
    seq = seq.replace('E', 'D')
    seq = seq.replace('N', 'D')
    seq = seq.replace('G', 'A')
    seq = seq.replace('P', 'A')
    seq = seq.replace('S', 'A')
    seq = seq.replace('T', 'A')
    seq = seq.replace('L', 'C')
    seq = seq.replace('F', 'C')
    seq = seq.replace('I', 'C')
    seq = seq.replace('V', 'C')
    seq = seq.replace('W', 'C')
    seq = seq.replace('M', 'C')

    p_aa = ['A', 'C', 'D', 'H', 'Y']
    t_gram_512 = []

    for  aa_i in p_aa:
        for aa_j in p_aa:
            for aa_k in p_aa:
                aa_t = aa_i + aa_j + aa_k
                t_gram_512.append(aa_t)
    # print(len(t_gram_512))
    t_gram = []
    for t in t_gram_512:
        num = seq.count(t)
        num = num / (len(seq) - 2)
        t_gram.append(num)
    return t_gram

def t_gram_7_zhangli_dianji(path):

    for data in SeqIO.parse(path, 'fasta'):
        seq = data.seq
    seq = str(seq)
    seq = seq.replace('G', 'A')
    seq = seq.replace('R', 'D')
    seq = seq.replace('N', 'D')
    seq = seq.replace('Q', 'D')
    seq = seq.replace('H', 'D')
    seq = seq.replace('T', 'S')
    seq = seq.replace('K', 'E')
    seq = seq.replace('M', 'F')
    seq = seq.replace('Y', 'F')
    seq = seq.replace('V', 'F')
    seq = seq.replace('L', 'F')
    seq = seq.replace('W', 'F')
    seq = seq.replace('I', 'F')

    p_aa = ['A', 'C', 'D', 'E', 'F', 'P', 'S']
    t_gram_512 = []

    for  aa_i in p_aa:
        for aa_j in p_aa:
            for aa_k in p_aa:
                aa_t = aa_i + aa_j + aa_k
                t_gram_512.append(aa_t)
    # print(len(t_gram_512))
    t_gram = []
    for t in t_gram_512:
        num = seq.count(t)
        num = num / (len(seq) - 2)
        t_gram.append(num)
    return t_gram

def t_gram_8_zhangli_kerong(path):
    for data in SeqIO.parse(path, 'fasta'):
        seq = data.seq
    seq = str(seq)
    seq = seq.replace('G', 'A')
    seq = seq.replace('N', 'D')
    seq = seq.replace('Q', 'D')
    seq = seq.replace('R', 'D')
    seq = seq.replace('K', 'E')
    seq = seq.replace('T', 'S')
    seq = seq.replace('L', 'F')
    seq = seq.replace('W', 'F')
    seq = seq.replace('I', 'F')
    seq = seq.replace('V', 'F')
    seq = seq.replace('Y', 'M')
    seq = seq.replace('P', 'M')

    p_aa = ['A', 'C', 'D', 'E', 'F', 'H', 'S', 'M']
    t_gram_512 = []

    for aa_i in p_aa:
        for aa_j in p_aa:
            for aa_k in p_aa:
                aa_t = aa_i + aa_j + aa_k
                t_gram_512.append(aa_t)
    # print(len(t_gram_512))
    t_gram = []
    for t in t_gram_512:
        num = seq.count(t)
        num = num / (len(seq) - 2)
        t_gram.append(num)
    return t_gram

def t_gram_7_kerong_dianji(path):

    for data in SeqIO.parse(path, 'fasta'):
        seq = data.seq
    seq = str(seq)
    seq = seq.replace('I', 'C')
    seq = seq.replace('W', 'C')
    seq = seq.replace('F', 'C')
    seq = seq.replace('L', 'C')
    seq = seq.replace('V', 'C')
    seq = seq.replace('G', 'A')
    seq = seq.replace('R', 'D')
    seq = seq.replace('E', 'D')
    seq = seq.replace('N', 'D')
    seq = seq.replace('Q', 'D')
    seq = seq.replace('K', 'D')
    seq = seq.replace('Y', 'M')
    seq = seq.replace('S', 'P')
    seq = seq.replace('T', 'P')

    p_aa = ['A', 'C', 'D', 'M', 'P', 'H']
    t_gram_512 = []

    for  aa_i in p_aa:
        for aa_j in p_aa:
            for aa_k in p_aa:
                aa_t = aa_i + aa_j + aa_k
                t_gram_512.append(aa_t)
    # print(len(t_gram_512))
    t_gram = []
    for t in t_gram_512:
        num = seq.count(t)
        num = num / (len(seq) - 2)
        t_gram.append(num)
    return t_gram



def s_gram_8(path):
    for data in SeqIO.parse(path, 'fasta'):
        seq = data.seq
    seq = str(seq)
    seq = seq.replace('I', 'V')
    seq = seq.replace('Y', 'F')
    seq = seq.replace('W', 'F')
    seq = seq.replace('L', 'A')
    seq = seq.replace('M', 'A')
    seq = seq.replace('Q', 'E')
    seq = seq.replace('R', 'E')
    seq = seq.replace('K', 'E')
    seq = seq.replace('N', 'D')
    seq = seq.replace('H', 'C')
    seq = seq.replace('S', 'C')
    seq = seq.replace('T', 'C')

    p_aa = ['A', 'C', 'D', 'E', 'F', 'G', 'P', 'V']
    s_gram_400 = []

    for aa_i in p_aa:
        for aa_j in p_aa:
            aa_s = aa_i+aa_j
            s_gram_400.append(aa_s)
    s_gram = []
    for t in s_gram_400:
        num = seq.count(t)
        num = num / (len(seq) - 2)
        s_gram.append(num)
    return s_gram



def t_gram_8(path):

    for data in SeqIO.parse(path, 'fasta'):
        seq = data.seq
    seq = str(seq)
    seq = seq.replace('I', 'V')
    seq = seq.replace('Y', 'F')
    seq = seq.replace('W', 'F')
    seq = seq.replace('L', 'A')
    seq = seq.replace('M', 'A')
    seq = seq.replace('Q', 'E')
    seq = seq.replace('R', 'E')
    seq = seq.replace('K', 'E')
    seq = seq.replace('N', 'D')
    seq = seq.replace('H', 'C')
    seq = seq.replace('S', 'C')
    seq = seq.replace('T', 'C')

    p_aa = ['A', 'C', 'D', 'E', 'F', 'G', 'P', 'V']
    t_gram_512 = []

    for  aa_i in p_aa:
        for aa_j in p_aa:
            for aa_k in p_aa:
                aa_t = aa_i + aa_j + aa_k
                t_gram_512.append(aa_t)
    # print(len(t_gram_512))
    t_gram = []
    for t in t_gram_512:
        num = seq.count(t)
        num = num / (len(seq) - 2)
        t_gram.append(num)
    return t_gram
    # out_file = out_path +

def t_gram_9(path):

    for data in SeqIO.parse(path, 'fasta'):
        seq = data.seq
    seq = str(seq)
    seq = seq.replace('I', 'V')
    seq = seq.replace('Y', 'F')
    seq = seq.replace('W', 'F')
    seq = seq.replace('L', 'A')
    seq = seq.replace('M', 'A')
    seq = seq.replace('Q', 'E')
    seq = seq.replace('R', 'E')
    seq = seq.replace('K', 'E')
    seq = seq.replace('N', 'D')
    seq = seq.replace('H', 'C')
    seq = seq.replace('S', 'C')
    seq = seq.replace('T', 'C')

    p_aa = ['A', 'C', 'D', 'E', 'F', 'G', 'P', 'V']
    t_gram_512 = []

    for  aa_i in p_aa:
        for aa_j in p_aa:
            for aa_k in p_aa:
                aa_t = aa_i + aa_j + aa_k
                t_gram_512.append(aa_t)
    # print(len(t_gram_512))
    t_gram = []
    for t in t_gram_512:
        num = seq.count(t)
        num = num / (len(seq) - 2)
        t_gram.append(num)
    return t_gram

def s_gram(path):
    for data in SeqIO.parse(path, 'fasta'):
        seq = data.seq
    seq = str(seq)

    p_aa = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K',
              'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
              'V', 'W', 'Y']
    s_gram_400 = []

    for aa_i in p_aa:
        for aa_j in p_aa:
            aa_s = aa_i+aa_j
            s_gram_400.append(aa_s)
    s_gram = []
    for t in s_gram_400:
        num = seq.count(t)
        num = num / (len(seq) - 2)
        s_gram.append(num)
    return s_gram

def one_gram(path):
    for data in SeqIO.parse(path, 'fasta'):
        seq = data.seq
    seq = str(seq)

    p_aa = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K',
              'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
              'V', 'W', 'Y']
    one_gra = []
    for aa in p_aa:
        num = seq.count(aa)
        num = num / (len(seq) - 2)
        one_gra.append(num)
    return one_gra

def t_gram_normal(path):

    for data in SeqIO.parse(path, 'fasta'):
        seq = data.seq
    seq = str(seq)

    p_aa = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K',
            'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
            'V', 'W', 'Y']
    t_gram_512 = []

    for  aa_i in p_aa:
        for aa_j in p_aa:
            for aa_k in p_aa:
                aa_t = aa_i + aa_j + aa_k
                t_gram_512.append(aa_t)
    # print(len(t_gram_512))
    t_gram = []
    for t in t_gram_512:
        num = seq.count(t)
        num = num / (len(seq) - 2)
        t_gram.append(num)
    return t_gram

def main():

    # files = os.listdir(path)
    # for file in files:
    #     protein_name = file[:-6]
    #     file = path + file
    #     t_gram = t_gram_8(file)
    #     print(protein_name)
    #     print(t_gram)
    #     out_file = out_path + protein_name + '.csv'
    #     with open(out_file, 'w') as w_obj:
    #         for i in range(len(t_gram) - 1):
    #             w_obj.write(str(t_gram[i]))
    #             w_obj.write(',')
    #         w_obj.write(str(t_gram[-1]))
    path = r'E:\my_research\transporter_svm\data\trans_neg/'
    # path = r'E:\my_research\transporter_svm\data_2000\pos/'
    out_path = r'E:\my_research\transporter_svm\data\zhangli_kerong\neg/'

    with open(r'E:\my_research\transporter_svm\data\neg_875.txt', 'r') as r_obj:
        proteins = r_obj.readlines()
    for protein in proteins:
        protein = protein[:-1]
        file = path + protein + '.fasta'
        t_gram = t_gram_8_zhangli_kerong(file)
        # print(protein)
        # print(t_gram)
        out_file = out_path + protein + '.csv'
        with open(out_file, 'w') as w_obj:
            for i in range(len(t_gram) - 1):
                w_obj.write(str(t_gram[i]))
                w_obj.write(',')
            w_obj.write(str(t_gram[-1]))


if __name__ == '__main__':
    main()