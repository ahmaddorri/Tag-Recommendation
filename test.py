
X = [[0,3], [1,2], [2,4], [3,1.5]]
y = [0, 0, 1, 1]
from pylmnn.lmnn import LargeMarginNearestNeighbor
# lmnn = LargeMarginNearestNeighbor(n_neighbors=1)
lmnn = LargeMarginNearestNeighbor(L=None, load=None, max_constr=10000000,
              max_iter=200, n_features_out=1, n_neighbors=1,
              random_state=None, save=None, tol=1e-05, use_pca=True,
              use_sparse=True, verbose=1)
lmnn.fit(X, y) # doctest: +ELLIPSIS
print(lmnn.transform(X))

test =[[1.6,1.6]]
print(lmnn.predict(test))

print(lmnn.transform(test))