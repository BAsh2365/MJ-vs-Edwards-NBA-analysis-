import pandas as pd
import matplotlib.pyplot as plt
#Author: Bhargav Ashok


# Load the data from the Excel files from basketball-reference
edwards_data = pd.read_excel('Anthony_Edwards_PLayoff_Stats.xlsx')
jordan_data = pd.read_excel('Michael_Jordan_Playoff_Stats.xlsx')


# Ensure the data contains stats up to age 22
edwards_data = edwards_data[edwards_data['Age'] <= 22] #first four NBA seasons
jordan_data = jordan_data[jordan_data['Age'] <= 24]


# Select relevant columns (for example: Points, Assists, Rebounds, etc.)
columns_of_interest = ['Season', 'AST']


edwards_stats = edwards_data[columns_of_interest]
jordan_stats = jordan_data[columns_of_interest]


# Plotting the stats comparison
plt.figure(figsize=(14, 8))


for column in columns_of_interest[1:]:
   plt.plot(edwards_stats['Season'], edwards_stats[column], marker='x', color = "blue", label=f'Edwards {column}')
   plt.plot(jordan_stats['Season'], jordan_stats[column], marker='x', color = "red", label=f'Jordan {column}')


plt.xlabel('Seasons')
plt.ylabel('Average assists per game (in playoffs)')
plt.title('Anthony Edwards vs Michael Jordan Assists Comparison over first 4 playoff seasons')
plt.legend()
plt.grid(True)
plt.show()



