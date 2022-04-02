import pandas as pd

students_df = pd.read_csv('student.csv')
assignments_df = pd.read_csv('assignment.csv')

def capitalize():
    # Pre-process: Initialize column to check if name is capitalized
    students_df.insert(2,'isupper',False)
    for i in range(len(students_df)):
        if students_df['name'][i].startswith('C') == True:
            students_df['name'][i] = students_df['name'][i].upper()
            # Set true if name is capitalize
            students_df['isupper'][i] = True
        else:
            students_df['name'][i] = students_df['name'][i].lower()
    return students_df

def average():
    # Join tables
    combined = pd.merge(students_df,assignments_df, left_on = "id", right_on = "student_id")
    # Calculate average based on capitalization
    combined = combined.groupby('isupper').mean()
    return combined

def main():
    capitalize()
    average()

main()