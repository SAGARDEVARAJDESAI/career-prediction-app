import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

# 1️ Load Dataset
data = pd.read_csv('../dataset/career_data.csv')

# 2️ Features & Labels
X = data.drop('Recommended_Career', axis=1)
y = data['Recommended_Career']

# 3️ Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4️ Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 5️ Save model
joblib.dump(model, 'career_model.pkl')


# 6️ Test accuracy
accuracy = model.score(X_test, y_test)
print(f"Model trained with accuracy: {accuracy}")
