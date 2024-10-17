import pandas as pd

#Author: Bhargav Ashok


# Sample data: list of dictionaries with game information
data = [
   {'game': 'Game 1', 'possessions': 103.4, 'DRTG': 133.4},
   {'game': 'Game 2', 'possessions': 102.9, 'DRTG': 145.8},
   {'game': 'Game 3', 'possessions': 105.2, 'DRTG': 111.2},
   {'game': 'Game 4', 'possessions': 112.5, 'DRTG': 117.4},
   {'game': 'Game 5', 'possessions': 103.8, 'DRTG': 122.3},
   {'game': 'Game 6', 'possessions': 105.2, 'DRTG': 94.1},
   {'game': 'Game 7', 'possessions': 100.8, 'DRTG': 121.1},
   {'game': 'Game 8', 'possessions': 102.9, 'DRTG': 143.8},
   {'game': 'Game 9', 'possessions': 101.3, 'DRTG': 123.4},
   {'game': 'Game 10', 'possessions': 105.9, 'DRTG': 115.2},
   {'game': 'Game 11', 'possessions': 115.4, 'DRTG': 116.1},
   {'game': 'Game 12', 'possessions': 100.5, 'DRTG': 148.3},
   {'game': 'Game 13', 'possessions': 103.9, 'DRTG': 120.3},
   {'game': 'Game 14', 'possessions': 104.7, 'DRTG': 107.9},
   {'game': 'Game 15', 'possessions': 101.5, 'DRTG': 134.0},
   {'game': 'Game 16', 'possessions': 102.1, 'DRTG': 120.4},
   {'game': 'Game 17', 'possessions': 103.4, 'DRTG': 93.8},
   {'game': 'Game 18', 'possessions': 100.7, 'DRTG': 135.1},
   {'game': 'Game 19', 'possessions': 102, 'DRTG': 119.6},
   {'game': 'Game 20', 'possessions': 104.1, 'DRTG': 108.6},
   {'game': 'Game 21', 'possessions': 103.1, 'DRTG': 105.8},
   {'game': 'Game 22', 'possessions': 102.9, 'DRTG': 137.9},
   {'game': 'Game 23', 'possessions': 110.7, 'DRTG': 105.7},
   {'game': 'Game 24', 'possessions': 100, 'DRTG': 109.0},
   {'game': 'Game 25', 'possessions': 104.6, 'DRTG': 150.1},


   ]
#the lower the DRTG score the better
data_2 = [
   {'game_2': 'Game 1', 'possessions_2': 103.4, 'scores_2': 141},
   {'game_2': 'Game 2', 'possessions_2': 102.9, 'scores_2': 116},
   {'game_2': 'Game 3', 'possessions_2': 105.2, 'scores_2': 110},
   {'game_2': 'Game 4', 'possessions_2': 112.5, 'scores_2': 139},
   {'game_2': 'Game 5', 'possessions_2': 103.8, 'scores_2': 99},
   {'game_2': 'Game 6', 'possessions_2': 105.2, 'scores_2': 109},
   {'game_2': 'Game 7', 'possessions_2': 100.8, 'scores_2': 107},
   {'game_2': 'Game 8', 'possessions_2': 102.9, 'scores_2': 143},
   {'game_2': 'Game 9', 'possessions_2': 101.3, 'scores_2': 126},
   {'game_2': 'Game 10', 'possessions_2': 105.9, 'scores_2': 138},
   {'game_2': 'Game 11', 'possessions_2': 115.4, 'scores_2': 141},
   {'game_2': 'Game 12', 'possessions_2': 100.5, 'scores_2': 144},
   {'game_2': 'Game 13', 'possessions_2': 103.9, 'scores_2': 117},
   {'game_2': 'Game 14', 'possessions_2': 104.7, 'scores_2': 122},
   {'game_2': 'Game 15', 'possessions_2': 101.5, 'scores_2': 126},
   {'game_2': 'Game 16', 'possessions_2': 102.1, 'scores_2': 121},
   {'game_2': 'Game 17', 'possessions_2': 103.4, 'scores_2': 124},
   {'game_2': 'Game 18', 'possessions_2': 100.7, 'scores_2': 105},
   {'game_2': 'Game 19', 'possessions_2': 102, 'scores_2': 123},
   {'game_2': 'Game 20', 'possessions_2': 104.1, 'scores_2': 121},
   {'game_2': 'Game 21', 'possessions_2': 103.1, 'scores_2': 95},
   {'game_2': 'Game 22', 'possessions_2': 102.9, 'scores_2': 110},
   {'game_2': 'Game 23', 'possessions_2': 110.7, 'scores_2': 111},
   {'game_2': 'Game 24', 'possessions_2': 100, 'scores_2': 106},
   {'game_2': 'Game 25', 'possessions_2': 104.6, 'scores_2': 115},




   # Add more game data as needed
]


# Convert the data to a DataFrame for easier manipulation
df = pd.DataFrame(data)
df_2 = pd.DataFrame(data_2)


# Calculate the defensive rate per 100 possessions
df['DRTG_rate_per_100_possessions'] = df['DRTG'] / df['possessions'] * 100
#scoring rate
df_2['scoring_rate_per_100_possessions_2'] = df_2['scores_2'] / df_2['possessions_2'] * 100


# Analyze the data for defense
average_DRTG_rate = df['DRTG_rate_per_100_possessions'].mean()
max_DRTG_rate = df['DRTG_rate_per_100_possessions'].max()
min_DRTG_rate = df['DRTG_rate_per_100_possessions'].min()


# Analyze the data for hawks
average_scoring_rate_2 = df_2['scoring_rate_per_100_possessions_2'].mean()
max_scoring_rate_2 = df_2['scoring_rate_per_100_possessions_2'].max()
min_scoring_rate_2 = df_2['scoring_rate_per_100_possessions_2'].min()


# Display the results for defense
print("Average DRTG Rate per 100 Possessions:", average_DRTG_rate)
print("Max DRTG Rate per 100 Possessions:", max_DRTG_rate)
print("Min DRTG Rate per 100 Possessions:", min_DRTG_rate)


# Display the results for offense
print("Average Scoring Rate per 100 Possessions_2:", average_scoring_rate_2)
print("Max Scoring Rate per 100 Possessions_2:", max_scoring_rate_2)
print("Min Scoring Rate per 100 Possessions_2:", min_scoring_rate_2)


# Optional: Plot the scoring rate for each game
import matplotlib.pyplot as plt


plt.plot(df['game'], df['DRTG_rate_per_100_possessions'], marker='o', color = "orange") #circle mark on graph
plt.plot(df_2['game_2'], df_2['scoring_rate_per_100_possessions_2'], marker='o', color ="red") 
plt.title('2024 Atlanta Hawks Regular season Defense vs Scoring rating')
plt.xlabel('Hawks Regular season Defense vs Scoring Rating')
plt.ylabel('Rate per 100 Possessions')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


