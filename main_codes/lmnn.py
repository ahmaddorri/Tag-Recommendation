__author__ = 'ahmaddorri'

from main_codes import get_data_splited
from main_codes import write_on_file_L2RFormat as wr

lables, qid, data = get_data_splited.get_data(fname="train.txt")

n_features_out = len(data[0])
print("n_features_out = ",n_features_out)

from pylmnn.lmnn import LargeMarginNearestNeighbor
# lmnn = LargeMarginNearestNeighbor(n_neighbors=1)
lmnn = LargeMarginNearestNeighbor(L=None, load=None, max_constr=10000000,
              max_iter=200, n_features_out=5, n_neighbors=7,
              random_state=1, save=None, tol=1e-05, use_pca=True,
              use_sparse=True, verbose=1)
lmnn.fit(data, lables) # doctest: +ELLIPSIS

data = lmnn.transform(data)
wr.write_("train_transformed.txt",lables=lables,qids=qid,datas=data)

test_lables, test_qid, test_data = get_data_splited.get_data(fname="test.txt")

test_data = lmnn.transform(test_data)

wr.write_("test_transformed.txt",lables=test_lables,qids=test_qid,datas=test_data)

# print(lmnn.score(test_data, test_lables))