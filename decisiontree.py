import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

le = preprocessing.LabelEncoder()

accuracy1_data=pd.read_csv("accuracy1.csv")

accuracy1_data=accuracy1_data.fillna(value=-150)

# Create feature and target arrays
y_tmp=accuracy1_data['location']
y=le.fit_transform(y_tmp)

X=accuracy1_data
X=X.drop(['location'], axis = 1)

# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=5, random_state=10,stratify=y)

dt_model=DecisionTreeClassifier(random_state=0)
dt_model.fit(X_train,y_train)

print(dt_model.score(X_test, y_test))