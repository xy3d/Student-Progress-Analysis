import csv
import random
from faker import Faker

# Initialize Faker to generate fake data
fake = Faker()

# Define the subjects
subjects = ['English', 'Math', 'Science', 'Social_Science']

# Probability distributions for each subject (mean, standard deviation)
subject_distributions = {
    'English': (80, 10),
    'Math': (70, 15),
    'Science': (65, 20),
    'Social_Science': (75, 12)
}

# Generate random data for 1000 students with fake names
student_data = []
for student_id in range(100, 1100):
    student_name = fake.name()
    marks = []
    for subject in subjects:
        mean, std_dev = subject_distributions[subject]
        mark = round(random.gauss(mean, std_dev))  # Random mark with Gaussian distribution
        mark = max(5, min(95, mark))  # Limit the marks between 5 and 95
        marks.append(mark)
    total_marks = sum(marks)
    grade = ''
    if total_marks >= 320:
        grade = 'A'
    elif total_marks >= 240:
        grade = 'B'
    elif total_marks >= 160:
        grade = 'C'
    else:
        grade = 'D'

    # Additional features
    attendance = random.randint(70, 100)  # Percentage of classes attended (70% to 100%)
    study_hours = random.randint(1, 5)  # Number of hours spent studying (1 to 5 hours)
    extracurricular = random.choice([0, 1])  # Binary: 0 (not involved) or 1 (involved)
    parent_education = random.choice(['High School', 'Bachelor', 'Master', 'Doctorate'])
    socioeconomic_status = random.choice(['Low', 'Middle', 'High'])
    previous_exam_scores = [random.randint(30, 95) for _ in subjects]
    learning_style = random.choice(['Visual', 'Auditory', 'Kinesthetic'])
    study_resources = random.choice([0, 1])  # Binary: 0 (no access) or 1 (has access)

    student_data.append([student_id, student_name] + marks + [total_marks, grade, attendance, study_hours,
                                                             extracurricular, parent_education,
                                                             socioeconomic_status, previous_exam_scores,
                                                             learning_style, study_resources])

# Save the student data to a CSV file
filename = 'grades.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    header = ['Rolls', 'Student_Name'] + subjects + ['Total_Marks', 'Grades', 'Attendance', 'Study_Hours',
                                                    'Extracurricular', 'Parent_Education', 'Socioeconomic_Status',
                                                    'Previous_Exam_Scores', 'Learning_Style', 'Study_Resources']
    writer.writerow(header)  # Write the header row
    writer.writerows(student_data)  # Write the student data

print(f'Saved to {filename}.')
