# Make a simple Grocery App prediction in Hungary (using FastAPI)
# class_App_names = ['FoodPanda', 'Wolt', 'Spar', 'Tesco online', 'myLidl']
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

filePath = os.path.join(os.getcwd(), 'data.csv')

# 1. Get the data
data = pd.read_csv(filePath)

# 2. Check the data
# print(data.head(7))

# 3. Features & Target
X = data.drop("Apps", axis=1)
y = data['Apps']

# 4. Split the data
X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y, 
                                                    test_size=0.3,
                                                    random_state=42)

# 5. Make a model
clf = RandomForestClassifier()

# 6. Fit the model
clf.fit(X_train, y_train)

# 7. Make a prediction
y_preds = clf.predict(X_test)

# 8. Accuracy of the model
acc = accuracy_score(y_test, y_preds)
print(f"Accuracy of the model is: {round((acc*100),2)}%")

# 9. Save the model with pickle
# filename = "clf_simple.pkl"
# pickle.dump(clf, open(filename, 'wb'))

# 10. load the model and make a prediction
# in fastapi.py app