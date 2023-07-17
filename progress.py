import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the dataset into a DataFrame
data = pd.read_csv('student_dataset.csv')

# Drop any rows with missing values
data.dropna(inplace=True)

# Encode categorical variables if needed
# For simplicity, let's assume all the relevant features are already numerical

# Select relevant features and target variable
features = ['StudyTime', 'Failures', 'Absences']
target = 'FinalGrade'

X = data[features]
y = data[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Decision Tree Classifier
model = DecisionTreeClassifier()

# Train the model on the training data
model.fit(X_train, y_train)

# Predict on the test set
predictions = model.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
