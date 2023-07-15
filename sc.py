import pandas as pd

# Load the df from the CSV file
df = pd.read_csv('grades.csv')

# Calculate the mean for each subject
mean_english = df['English'].mean()
mean_math = df['Math'].mean()
mean_science = df['Science'].mean()
mean_social_science = df['Social Science'].mean()

# Display the results
print(f"Mean marks for English: {mean_english:.2f}")
print(f"Mean marks for Math: {mean_math:.2f}")
print(f"Mean marks for Science: {mean_science:.2f}")
print(f"Mean marks for Social Science: {mean_social_science:.2f}")
