from Bio import SeqIO
import os

hydrophobicity = ['RKEDQN', 'GASTPHY', 'CVLIMFW']

surface_tension = ['GQDNAHR', 'KTSEC', 'ILMFPWYV']

Solventsolubility = ['ALFCGIVW', 'RKQEND', 'MPSTHY']

charged_polarity = ['LIFWCMVY', 'PATGS', 'HQRKEND']

zongshu = 0
num_1 = 0
num_2 = 0
num_3 = 0
# with open(r'D:\duibi\train\train_1.txt', 'r') as r_obj:
#     ids = r_obj.readlines()
ids = os.listdir(r'D:\duibi\seq0005524/')

A = hydrophobicity
for id in ids:
    # print(id)
    path = r'D:\duibi\seq0005524/' + id
    for data in SeqIO.parse(path, 'fasta'):
        seq = data.seq
        l = len(seq)
        zongshu += l

        for aa in A[0]:
            num_1 += seq.count(aa)
        for aa in A[1]:
            num_2 += seq.count(aa)
        for aa in A[2]:
            num_3 += seq.count(aa)

print(num_1/zongshu, num_2/zongshu, num_3/zongshu)
# print(zongshu)