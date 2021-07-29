from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from data_preprocessed import X_train, X_test, y_train, y_test

dt_model=DecisionTreeClassifier(random_state=0)
dt_model.fit(X_train,y_train)

print('DecisionTreeClassifier:',dt_model.score(X_test, y_test))

knn = KNeighborsClassifier(random_state=0,n_neighbors=5)
knn.fit(X_train, y_train)

print('KNeighborsClassifier:',knn.score(X_test, y_test))

clf = RandomForestClassifier(random_state=0)
clf.fit(X_train, y_train)

print('RandomForestClassifier:',clf.score(X_test, y_test))