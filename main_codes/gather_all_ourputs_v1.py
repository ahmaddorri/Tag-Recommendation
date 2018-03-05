__author__ = 'ahmaddorri'

"""
    V1: gather all outputs how the number of rel and non_rel are equal by randomly choose from non_rel list
"""
import numpy as np

file_path = "train.txt"
text_file = open(file_path, "w")

non_rel_list = []
rel_num = 0
for i in range(4,27):
    fname = "outputs/out"+str(i)+".txt"
    with open(fname) as f:
        content = f.readlines()

    for line in content:
        if line[0] == "1":
            rel_num += 1
            text_file.write(line)
        else:
            non_rel_list.append(line)

non_rel = np.random.choice(non_rel_list, rel_num, replace=False)

for line in non_rel:
    text_file.write(line)

text_file.close()
