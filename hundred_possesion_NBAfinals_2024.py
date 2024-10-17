#Author: Bhargav Ashok

import pandas as pd


# Sample data: list of dictionaries with game information
data = [
   {'game': 'Game 1', 'possessions': 94, 'scores': 89},
   {'game': 'Game 2', 'possessions': 92.7, 'scores': 98},
   {'game': 'Game 3', 'possessions': 90.3, 'scores': 99},
   {'game': 'Game 4', 'possessions': 92.6, 'scores': 122},
   {'game': 'Game 5', 'possessions': 86.8, 'scores': 88},


   ]


data_2 = [
   {'game_2': 'Game 1', 'possessions_2': 91.2, 'scores_2': 107},
   {'game_2': 'Game 2', 'possessions_2': 92.7, 'scores_2': 105},
   {'game_2': 'Game 3', 'possessions_2': 90.3, 'scores_2': 106},
   {'game_2': 'Game 4', 'possessions_2': 92.6, 'scores_2': 84},
   {'game_2': 'Game 5', 'possessions_2': 86.8, 'scores_2': 106},




   # Add more game data as needed
]


# Convert the data to a DataFrame for easier manipulation
df = pd.DataFrame(data)
df_2 = pd.DataFrame(data_2)


# Calculate the scoring rate per 100 possessions
df['scoring_rate_per_100_possessions'] = df['scores'] / df['possessions'] * 100
#celtics
df_2['scoring_rate_per_100_possessions_2'] = df_2['scores_2'] / df_2['possessions_2'] * 100


# Analyze the data for mavericks
average_scoring_rate = df['scoring_rate_per_100_possessions'].mean()
max_scoring_rate = df['scoring_rate_per_100_possessions'].max()
min_scoring_rate = df['scoring_rate_per_100_possessions'].min()


# Analyze the data for Celtics
average_scoring_rate_2 = df_2['scoring_rate_per_100_possessions_2'].mean()
max_scoring_rate_2 = df_2['scoring_rate_per_100_possessions_2'].max()
min_scoring_rate_2 = df_2['scoring_rate_per_100_possessions_2'].min()


# Display the results
print("Average Scoring Rate per 100 Possessions:", average_scoring_rate)
print("Max Scoring Rate per 100 Possessions:", max_scoring_rate)
print("Min Scoring Rate per 100 Possessions:", min_scoring_rate)


# Display the results for Celtics
print("Average Scoring Rate per 100 Possessions_2:", average_scoring_rate_2)
print("Max Scoring Rate per 100 Possessions_2:", max_scoring_rate_2)
print("Min Scoring Rate per 100 Possessions_2:", min_scoring_rate_2)


# Optional: Plot the scoring rate for each game
import matplotlib.pyplot as plt


plt.plot(df['game'], df['scoring_rate_per_100_possessions'], marker='o') #circle mark on graph
plt.plot(df_2['game_2'], df_2['scoring_rate_per_100_possessions_2'], marker='s', color ="green") #square mark on graph
plt.title('2024 NBA Finals Dallas Mavericks Scoring Rate vs Boston Celtics')
plt.xlabel('Game')
plt.ylabel('Scoring Rate per 100 Possessions')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
