import pandas as pd

# Load the dataset from the CSV file
dataset = pd.read_csv('grades.csv')

# Calculate the mean for each subject
mean_english = dataset['English'].mean()
mean_math = dataset['Math'].mean()
mean_science = dataset['Science'].mean()
mean_social_science = dataset['Social Science'].mean()

# Display the results
print(f"Mean marks for English: {mean_english:.2f}")
print(f"Mean marks for Math: {mean_math:.2f}")
print(f"Mean marks for Science: {mean_science:.2f}")
print(f"Mean marks for Social Science: {mean_social_science:.2f}")
