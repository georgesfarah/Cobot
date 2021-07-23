from data_preprocessed import X_train, X_test, y_train, y_test
from sklearn.tree import DecisionTreeClassifier

dt_model=DecisionTreeClassifier(random_state=0)
dt_model.fit(X_train,y_train)

print(dt_model.score(X_test, y_test))