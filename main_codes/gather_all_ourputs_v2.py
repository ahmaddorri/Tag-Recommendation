__author__ = 'ahmaddorri'

"""
    V2: gather all outputs by repeat the relevant items
"""

file_path = "train.txt"
text_file = open(file_path, "w")

rel_list = []
non_rel_list = []
rel_num = 0
non_rel_num = 0

for i in range(4,27):
    fname = "outputs/out"+str(i)+".txt"
    with open(fname) as f:
        content = f.readlines()

    for line in content:
        if line[0] == "1":
            rel_num += 1
            text_file.write(line)
            rel_list.append(line)
        else:
            non_rel_num += 1
            text_file.write(line)
            non_rel_list.append(line)

number_of_repeat = int(non_rel_num/rel_num)
for i in range(1,number_of_repeat):
    for line in rel_list:
        text_file.write(line)

text_file.close()


file_path = "test.txt"
text_file = open(file_path, "w")

for i in range(0,12):
    fname = "outputsTest/out"+str(i)+".txt"
    with open(fname) as f:
        content = f.readlines()

    for line in content:
        text_file.write(line)
text_file.close()
