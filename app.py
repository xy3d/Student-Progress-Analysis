import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv('student_dataset.csv')

# Select features and target variable (Math grades)
selected_features = ['Absences', 'StudyTime', 'School', 'Goout', 'FreeTime', 'Fjob', 'Mjob', 'Fedu', 'Medu', 'FamSize', 'Famrel', 'Failures']
X = df[selected_features]
y_math = df['Math']

# Encode categorical features
encoder = LabelEncoder()
categorical_features = ['School', 'Fjob', 'Mjob', 'Fedu', 'Medu', 'FamSize', 'Famrel']
for feature in categorical_features:
    X[feature] = encoder.fit_transform(X[feature])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_math, test_size=0.2, random_state=42)

# Train a RandomForestRegressor for Math grades
rf_regressor = RandomForestRegressor(random_state=42)
rf_regressor.fit(X_train, y_train)

# Predict Math grades on the test set
y_pred_math = rf_regressor.predict(X_test)

# Evaluate the model
mse_math = mean_squared_error(y_test, y_pred_math)
r2_math = r2_score(y_test, y_pred_math)

print(f"Mean Squared Error (MSE) for Math grades: {mse_math:.2f}")
print(f"R-squared (R2) for Math grades: {r2_math:.2f}")