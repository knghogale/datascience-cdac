#!/usr/bin/env python
# coding: utf-8

# In[21]:


print ("hello world !!")
print ("This is Kedar Ghogale, CDAC Pune.")
print ("Please find the solution of assignment number 02 below (19/08/2024) ..")


# In[50]:


import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_file.csv' with the path to your CSV file
df = pd.read_csv('cricket.csv')

# Display the first few rows of the DataFrame to verify it loaded correctly
print ("\nSolution of Q1 ...\n")
print(df.head())




print ("\nSolution of Q2 ...\n")
# Iterate over each row and print the cricketer's name and their runs
for index, row in df.iterrows():
    print(f"{row['name']}: {row['runs']} runs")
    
    
    
    
print ("\nSolution of Q3 ...\n")
# Initialize a variable to hold the total wickets
total_wickets = df['wickets'].sum()

# Print the total wickets
print(f"Total wickets taken by the cricketers: {total_wickets}")





print ("\nSolution of Q4 ...\n")
# Calculate the average number of catches
average_catches = df['catches'].mean()

# Print the average catches
print(f"The average number of catches taken by the cricketers is: {average_catches:.2f}")




print ("\nSolution of Q5 ...\n")
df['role'] = ['Batsman', 'Bowler', 'Batsman', 'wicketkeeper', 'Batsman', 'Batsman', 'Batsman', 'Batsman', 'Batsman', 'Bowler']

# Save the updated DataFrame back to the CSV file
# Use 'index=False' to avoid adding the index as a column in the CSV
df.to_csv('cricketers.csv', index=False)

# Print the updated DataFrame to verify
print(df)

# Filter the DataFrame to find the wicketkeeper
wicketkeeper = df[df['role'] == 'wicketkeeper']

# Print the name(s) of the wicketkeeper(s)
if not wicketkeeper.empty:
    print("\n")
    print("Wicketkeeper(s):")
    for name in wicketkeeper['name']:
        print(name)
        print("\n")
else:
    print("\nNo wicketkeeper found in the dataset.")
    
    
    
    
    
print ("\nSolution of Q6 ...\n")
# Filter the DataFrame to include only bowlers
bowlers = df[df['role'] == 'Bowler']

# Find the bowler with the maximum number of matches
if not bowlers.empty:
    bowler_with_most_matches = bowlers.loc[bowlers['matches'].idxmax()]
    print(f"The bowler who played the highest number of matches is: {bowler_with_most_matches['name']} with {bowler_with_most_matches['matches']} matches.")
else:
    print("No bowlers found in the dataset.")
    
    
    
    
    
print ("\nSolution of Q7 ...\n")
# Filter the DataFrame to include only bowlers
bowlers = df[df['role'] == 'Bowler']

# Calculate the average number of matches played by the bowlers
if not bowlers.empty:
    average_matches = bowlers['matches'].mean()
    print(f"The average number of matches played by bowlers is: {average_matches:.2f}")
else:
    print("No bowlers found in the dataset.")
    
# Filter the DataFrame to include only bowlers
bowlers = df[df['role'] == 'Bowler']




print ("\nSolution of Q8 ...\n")
# Calculate the bowling average (wickets per match)
# bowlers['Bowling_Average'] = bowlers['wickets'] / bowlers['matches']


# Filter the DataFrame to include only bowlers
bowlers = df.loc[df['role'] == 'Bowler']

# Calculate the bowling average (wickets per match) using .loc
bowlers.loc[:, 'Bowling_Average'] = bowlers['wickets'] / bowlers['matches']



# Find the bowler with the least bowling average
if not bowlers.empty:
    # Print the DataFrame with the new column
    print(bowlers)
    bowler_with_least_avg = bowlers.loc[bowlers['Bowling_Average'].idxmin()]
    print(f"\nThe bowler with the least bowling average is: {bowler_with_least_avg['name']} with an average of {bowler_with_least_avg['Bowling_Average']:.2f} wickets per match.")
else:
    print("No bowlers found in the dataset.")

    
    
    
print ("\nSolution of Q9 ...\n")
# Calculate the catches per match ratio
df['Catches_Per_Match'] = df['catches'] / df['matches']

# Filter the DataFrame to include only players with a catches per match ratio greater than 0.5
filtered_df = df[df['Catches_Per_Match'] > 0.5]

# Print the filtered DataFrame
print("Players with catches per match ratio greater than 0.5:")
print(filtered_df)

# Store the filtered DataFrame in a new CSV file
# Replace 'filtered_cricketers.csv' with the desired path for the new CSV file
filtered_df.to_csv('filtered_cricketers.csv', index=False)





print ("\nSolution of Q10 ...\n")
# Create a bar chart of player names against their runs
plt.figure(figsize=(10, 6))
plt.bar(df['name'], df['runs'], color='skyblue')

# Add labels and title
plt.xlabel('Player Names')
plt.ylabel('Runs')
plt.title('Runs Scored by Each Player')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability

# Display the bar chart
plt.tight_layout()
plt.show()





print ("\nSolution of Q11 ...\n")
# Sort the DataFrame by the 'Runs' column in ascending order
sorted_df = df.sort_values(by='runs', ascending=True)

# Print the sorted DataFrame
print("Players sorted by ascending order of runs:")
print(sorted_df)




print ("\nSolution of Q12 ...\n")
# Filter the DataFrame to include only players where Wickets > Matches
players_with_more_wickets = df[df['wickets'] > df['matches']]

# Print the names of these players
print("Players with wickets greater than matches:")
for name in players_with_more_wickets['name']:
    print(name)


# In[ ]:




