import pandas as pd
from flask import Flask, jsonify, request, render_template

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

# Route to serve the HTML chart page
@app.route('/')
def chart():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
