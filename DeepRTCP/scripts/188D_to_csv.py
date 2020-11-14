import os


path = r'E:\my_research\transporter_svm\data\188D\neg/'

files = os.listdir(path)

for file in files:
    with open(path+file, 'r') as r_obj:
        features = r_obj.readlines()
    features = features[-1]
    features = features[:-10]
    out_path = r'E:\my_research\transporter_svm\data\188D\neg_csv/' + file[:-4] + '.csv'
    with open(out_path, 'w') as w_obj:
        w_obj.write(features)