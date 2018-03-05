__author__ = 'ahmaddorri'


def write_(fname,lables,qids,datas):
    text_file = open(fname, "w")
    for lable,qid,data in zip(lables,qids,datas):
        text_file.write(str(lable))
        text_file.write(" qid:")
        text_file.write(str(int(qid)))
        i = 0
        for v in data:
            i += 1
            text_file.write(" ")
            text_file.write(str(i))
            text_file.write(":")
            text_file.write(str(v))

        text_file.write("\n")
    text_file.close()