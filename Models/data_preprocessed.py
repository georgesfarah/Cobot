import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler


accuracy1_data=pd.read_csv("Datasets/accuracy1.csv") #chdir is /
accuracy1_data=accuracy1_data.dropna(subset=['location'])

# Create feature and target arrays
y_tmp=accuracy1_data['location']
le = LabelEncoder()
y=le.fit_transform(y_tmp)

X=accuracy1_data.drop(['location','C2:2B:F9:8D:63:ED'], axis = 1)
X=X.fillna(value=-150)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1,stratify=y)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)