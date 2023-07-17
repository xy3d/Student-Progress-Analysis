import pandas as pd
import numpy as np
from faker import Faker

# Set the number of students in the dataset
num_students = 100000

# Initialize Faker
fake = Faker()

# Demographical features
schools = ['School_A', 'School_B', 'School_C', 'School_D', 'School_E', 'School_F', 'School_G', 'School_H', 'School_I', 'School_J']
sexes = ['Male', 'Female']
ages = np.random.randint(15, 19, num_students)
addresses = ['Urban', 'Rural']
fam_sizes = np.random.randint(2, 8, num_students)
p_statuses = ['Together', 'Apart']
medu_values = ['No', 'Primary', 'High', 'UnderGrad', 'Masters', 'phD']
fedu_values = ['No', 'Primary', 'High', 'UnderGrad', 'Masters', 'phD']
mjobs = ['Teacher', 'Doctor', 'Engineer', 'Services', 'At_home', 'Other']
fjobs = ['Teacher', 'Doctor', 'Engineer', 'Services', 'At_home', 'Other']
reasons = ['Home', 'Reputation', 'Course', 'Environment', 'Other']
guardians = ['Both', 'Mother', 'Father', 'Other']

# Social features
internet_values = ['Yes', 'No']
romantic_values = ['Yes', 'No']
famrel_values = ['Fight', 'Nofight', 'Happy', 'Sad']
free_time_values = np.random.randint(1, 9, num_students)
go_out_values = np.random.randint(1, 9, num_students)
bad_habits_values = ['Yes', 'No']
health_values = ['Good', 'Bad']

# Academic-related features
absences_values = np.random.randint(0, 51, num_students)
travel_time_values = np.random.randint(1, 5, num_students)
study_time_values = np.random.randint(1, 41, num_students)
failures_values = np.random.randint(0, 5, num_students)
school_sup_values = ['Yes', 'No']
famsup_values = ['Yes', 'No']
activities_values = ['Yes', 'No']
higher_values = ['Yes', 'No']
final_grades = ['Excellent', 'Good', 'Satisfactory', 'Poor', 'Failure']

# Subject marks
subject_marks = np.random.randint(0, 11, size=(num_students, 6))

# Calculate FinalMarks
final_marks = subject_marks.sum(axis=1)

# Encode FinalGrade based on FinalMarks
final_grade_encoding = {
    'Excellent': (45, 60),
    'Good': (36, 44),
    'Satisfactory': (24, 35),
    'Poor': (20, 23),
    'Failure': (0, 19)
}

def encode_final_grade(final_mark):
    for grade, (lower_bound, upper_bound) in final_grade_encoding.items():
        if lower_bound <= final_mark <= upper_bound:
            return grade
    return 'Unknown'

# Create the dataset
data = {
    'ID': [fake.uuid4() for _ in range(num_students)],
    'Name': [fake.name() for _ in range(num_students)],
    'School': np.random.choice(schools, num_students),
    'Sex': np.random.choice(sexes, num_students),
    'Age': ages,
    'Address': np.random.choice(addresses, num_students),
    'FamSize': fam_sizes,
    'Pstatus': np.random.choice(p_statuses, num_students),
    'Medu': np.random.choice(medu_values, num_students),
    'Fedu': np.random.choice(fedu_values, num_students),
    'Mjob': np.random.choice(mjobs, num_students),
    'Fjob': np.random.choice(fjobs, num_students),
    'Reason': np.random.choice(reasons, num_students),
    'Guardian': np.random.choice(guardians, num_students),
    'Internet': np.random.choice(internet_values, num_students),
    'Romantic': np.random.choice(romantic_values, num_students),
    'Famrel': np.random.choice(famrel_values, num_students),
    'FreeTime': free_time_values,
    'Goout': go_out_values,
    'Badhabbits': np.random.choice(bad_habits_values, num_students),
    'Health': np.random.choice(health_values, num_students),
    'Absences': absences_values,
    'TravelTime': travel_time_values,
    'StudyTime': study_time_values,
    'Failures': failures_values,
    'SchoolSup': np.random.choice(school_sup_values, num_students),
    'Famsup': np.random.choice(famsup_values, num_students),
    'Activities': np.random.choice(activities_values, num_students),
    'Higher': np.random.choice(higher_values, num_students),
    'English': subject_marks[:, 0],
    'Physics': subject_marks[:, 1],
    'Chemistry': subject_marks[:, 2],
    'Biology': subject_marks[:, 3],
    'Math': subject_marks[:, 4],
    'Statistics': subject_marks[:, 5],
    'FinalMarks': final_marks,
}

# Map FinalMarks to FinalGrade
data['FinalGrade'] = [encode_final_grade(final_mark) for final_mark in data['FinalMarks']]

# Create the DataFrame
df = pd.DataFrame(data)

# Save the dataset to a CSV file
df.to_csv('student_dataset.csv', index=False)
print(f'Dataset has been generated.')