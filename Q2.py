"""
You are given a CSV file containing records with an ID and various parameters, including an event name, outcome, and other details. The task involves analyzing the file and performing the following operations:

Count the occurrences of each event name.
Count the number of errors.
Count the number of successful events. 
"""

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('Q2_file.csv')

# Count the occurrences of each event name
event_counts = df['event_name'].value_counts()

# Count the number of errors
error_count = df[df['outcome'] == 'error'].shape[0]

# Count the number of successful events
success_count = df[df['outcome'] == 'success'].shape[0]

# Print the results
print("Occurrences of each event name:")
print(event_counts)
print("\nNumber of errors:", error_count)
print("Number of successful events:", success_count)
