__author__ = 'ahmaddorri'



def get_data(fname):
    with open(fname) as f:
        content = f.readlines()


    lables =[]
    raw_feature = []
    for line in content:
        lables.append(float(line[0]))
        raw_feature.append(line[2:])

    data = []
    qid = []
    for features in raw_feature:
        features_split = features.split(" ")
        qid_data=features_split[0]
        split_qid = qid_data.split(":")
        qid.append(int(split_qid[1]))
        features_split = features_split[1:-1]
        f_vec = []
        for feature in features_split:
            feat = feature.split(":")
            f_vec.append(float(feat[1]))
        data.append(f_vec)

    print(lables)
    print(qid)
    print(data)

    return lables, qid, data