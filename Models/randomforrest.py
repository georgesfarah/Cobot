from data_preprocessed import X_train, X_test, y_train, y_test
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(random_state=0)
clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))