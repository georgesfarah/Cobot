import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing


le = preprocessing.LabelEncoder()

accuracy1_data=pd.read_csv("accuracy1.csv")

accuracy1_data=accuracy1_data.fillna(value=-150)

# Create feature and target arrays
y_tmp=accuracy1_data['location']
y=le.fit_transform(y_tmp)

X=accuracy1_data
X=X.drop(['location'], axis = 1)

X=(X-X.mean())/X.std()

# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10,stratify=y)


knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

print(knn.score(X_test, y_test))
