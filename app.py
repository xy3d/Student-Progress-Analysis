import pandas as pd
from flask import Flask, render_template, jsonify

# Load the dataset from the CSV file
dataset = pd.read_csv('grades.csv')

# Create the Flask app
app = Flask(__name__)

# Function to identify weaknesses for each subject
def identify_weaknesses(subject):
    pass_marks = 40
    weaknesses = dataset[dataset[subject] < pass_marks]
    return weaknesses

# API endpoint to get weaknesses by subject
@app.route('/api/weaknesses/<subject>', methods=['GET'])
def get_weaknesses_by_subject(subject):
    if subject not in dataset.columns:
        return jsonify({'error': 'Subject not found'}), 404

    weaknesses = identify_weaknesses(subject)
    return weaknesses.to_json(orient='records')

# API endpoint to get weaknesses count for each subject
@app.route('/api/weakness_count', methods=['GET'])
def get_weakness_count():
    weaknesses_count = {}
    subjects = ['English', 'Math', 'Science', 'Social Science']
    for subject in subjects:
        weaknesses_count[subject] = identify_weaknesses(subject).shape[0]
    return jsonify(weaknesses_count)

# Route to serve the HTML dashboard page
@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
