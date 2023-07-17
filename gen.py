import pandas as pd
import numpy as np

# Set the number of students in the dataset
num_students = 100000

# Demographical features
schools = ['School_A', 'School_B', 'School_C']
sexes = ['Male', 'Female']
ages = np.random.randint(15, 19, num_students)
addresses = ['Urban', 'Rural']
fam_sizes = np.random.randint(2, 8, num_students)
p_statuses = ['Together', 'Apart']
medu_values = ['No','Primary', 'High', 'UnderGrad', 'Masters', 'phD']
fedu_values = ['No','Primary', 'High', 'UnderGrad', 'Masters', 'phD']
mjobs = ['Teacher', 'Doctor', 'Engineer','Services', 'At_home', 'Other']
fjobs = ['Teacher', 'Doctor', 'Engineer','Services', 'At_home', 'Other']
reasons = ['Home', 'Reputation', 'Course', 'Enviroment', 'Other']
guardians = ['Both', 'Mother', 'Father', 'Other']

# Social features
internet_values = ['Yes', 'No']
romantic_values = ['Yes', 'No']
famrel_values = ['Fight', 'Nofight', 'Happy', 'Sad' ]
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
final_grades = ['excellent', 'good', 'satisfactory', 'poor', 'failure']

# Create the dataset
data = {
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
    'Famrel': famrel_values,
    'FreeTime': free_time_values,
    'Goout': go_out_values,
    'Badhabbits': bad_habits_values,
    'Health': health_values,
    'Absences': absences_values,
    'TravelTime': travel_time_values,
    'StudyTime': study_time_values,
    'Failures': failures_values,
    'SchoolSup': np.random.choice(school_sup_values, num_students),
    'Famsup': np.random.choice(famsup_values, num_students),
    'Activities': np.random.choice(activities_values, num_students),
    'Higher': np.random.choice(higher_values, num_students),
    'FinalGrade': final_grades
}

# Create the DataFrame
df = pd.DataFrame(data)

# Save the dataset to a CSV file
df.to_csv('student_dataset.csv', index=False)
