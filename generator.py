import csv
import random

# Define the subjects
subjects = ['English', 'Math', 'Science', 'Social Science']

# Generate random marks for 1000 students
student_marks = []
for student_id in range(100, 1100):
    marks = []
    for subject in subjects:
        mark = random.randint(20, 90)  # Random mark between 20 and 90
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
    student_marks.append([student_id] + marks + [total_marks, grade])

# Save the marks to a CSV file
filename = 'grades.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Rolls'] + subjects + ['Total Marks', 'Grades'])  # Write the header row
    writer.writerows(student_marks)  # Write the student marks

print(f'Saved to {filename}.')
