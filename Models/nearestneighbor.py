from data_preprocessed import X_train, X_test, y_train, y_test
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

print(knn.score(X_test, y_test))
