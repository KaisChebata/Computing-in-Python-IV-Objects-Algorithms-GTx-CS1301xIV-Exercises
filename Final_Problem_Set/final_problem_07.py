#Last problem, you wrote a function that generated the all-
#time win-loss-tie record for Georgia Tech against any other
#team.
#
#That dataset had a lot of other information in it. Let's
#use it to answer some more questions. As a reminder, the
#data will be a CSV file, meaning that each line will be a
#comma-separated list of values. Each line will describe one
#game.
#
#The columns, from left-to-right, are:
#
# - Date: the date of the game, in Year-Month-Day format.
# - Opponent: the name of the opposing team
# - Location: Home, Away, or Neutral
# - Points For: Points scored by Georgia Tech
# - Points Against: Points scored by the opponent

#Here Below, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.

# ---------------------------------------------------------------------------

# from all-time football history CVS file (data set) of Georgia Tech
# you'll be asked to return statistics about a certain opponent 
# team from the data set.
# each opponent team should has the following statistics: 
# games_list with each game has the following: 
# [date, opponent, place, points for Georgia Tech, points against Georgia Tech],  
# total wins, home wins, away wins, neutral wins, 
# total losses, home losses, away losses, neutral losses, 
# total ties, home ties, away ties, neutral ties, 
# points for, points against.
# 

# Question 1: what is the total Points scored by Georgia Tech team against Auburn team.

# Questoin 2: what is the total Points scored by Auburn team against Georgia Tech team.

# Questoin 3: what is the Earliest (first) game ever Georgia Tech team played.

# Question 4: give the home record for all games.

# Question 5: give the record of the year 2009 for all games. 

# Question 6: give the record of October months for all games. 

#This line will open the file:
# record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')

from typing import Dict, List, Union
from pprint import pprint
import datetime

def get_games_info(file_name: str) -> Dict[str, Dict[str, Union[int, List[list]]]]:


    with open(file_name) as record_file:
        record = record_file.read().split('\n')[1:]
        
    statistics = {}
    for game in record:
        row = game.split(',')
        opponent_name = row[1]
        row[3], row[4] = int(row[3]), int(row[4])
        if opponent_name not in statistics.keys():
                    statistics[opponent_name] = {'games': [],
                                                 'total wins': 0,
                                                 'home wins': 0,
                                                 'away wins': 0,
                                                 'neutral wins': 0,
                                                 'total losses': 0,
                                                 'home losses': 0,
                                                 'away losses': 0,
                                                 'neutral losses': 0,
                                                 'total ties': 0,
                                                 'home ties': 0,
                                                 'away ties': 0,
                                                 'neutral ties': 0,
                                                 'points for': 0,
                                                 'points against': 0}

        opponent_info = statistics[opponent_name]
        if row[3] > row[4]:
            opponent_info['total wins'] += 1
            row.append('win')
            if row[2] == 'Home':
                opponent_info['home wins'] += 1
            elif row[2] == 'Away':
                opponent_info['away wins'] += 1
            else:
                opponent_info['neutral wins'] += 1
        elif row[3] == row[4]:
            opponent_info['total ties'] += 1
            row.append('tie')
            if row[2] == 'Home':
                opponent_info['home ties'] += 1
            elif row[2] == 'Away':
                opponent_info['away ties'] += 1
            else:
                opponent_info['neutral ties'] += 1
        else:
            opponent_info['total losses'] += 1
            row.append('loss')
            if row[2] == 'Home':
                opponent_info['home losses'] += 1
            elif row[2] == 'Away':
                opponent_info['away losses'] += 1
            else:
                opponent_info['neutral losses'] += 1
        opponent_info['points for'] += row[3]
        opponent_info['points against'] += row[4]
        statistics[opponent_name]['games'].append(row)
        # statistics[opponent_name] = opponent_info

    return statistics

history_file_path = 'Final_Problem_Set\\Raw_files\\georgia_tech_football.csv'
# season_file_path for test
# season_file_path = 'Final_Problem_Set\\Raw_files\\season_2016.csv'
# pprint(get_games_info(history_file_path))

def earliest_game(statistics: dict) -> dict:
    first_game = {'team': '', 'date': None}
    for key in statistics:
        games = sorted(statistics[key]['games'])
        game1 = games[0][0]
        game1 = datetime.datetime(int(game1[0:4]), int(game1[5:7].lstrip('0')), 
                int(game1[8:10].lstrip('0'))).strftime('%Y-%m-%d')

        if first_game['date'] is None:
            first_game['date'] = game1
            first_game['team'] = key
        elif game1 < first_game['date']:
            first_game['date'] = game1
            first_game['team'] = key
    return first_game

team_info = get_games_info(history_file_path)
# Question 1: what is the total Points scored by  Georgia Tech team against Auburn team
# Answer: Auburn points for 1327
print ('Auburn points for {0}'.format(team_info['Auburn']['points for']))

# Questoin 2: what is the total Points scored by Auburn team against Georgia team 
# :Answer: Auburn points against 1143
print ('Auburn points against {0}'.format(team_info['Auburn']['points against']))

# Questoin 3: what is the Earliest (first) game ever Georgia Tech team played
# Answer: Earliest game was 1902-10-11 against Auburn
first_game = earliest_game(team_info)
print(f'Earliest (first) game ever played was {first_game["date"]} against {first_game["team"]}')

# Question 4: give the home record for all games. 
# Answer: Home record: 513-226-27
home_wins, home_losses, home_ties = 0, 0, 0
for key in team_info.keys():
    home_wins += team_info[key]['home wins']
    home_losses += team_info[key]['home losses']
    home_ties += team_info[key]['home ties']
print(f'Home record -> Home wins: {home_wins} - Home losses: {home_losses} - Home ties: {home_ties}')

# Question 5: give the record of the year 2009 for all games. 
# Answer: 2009 record: 11-3-0

home_wins_09, home_losses_09, home_ties_09 = 0, 0 , 0

for team in team_info:
    for game in team_info[team]['games']:
        if game[0][0:4] == '2009':
            if 'win' in game:
                home_wins_09 += 1
            elif 'loss' in game:
                home_losses_09 += 1
            else:
                home_ties_09 += 1
print(f'2009 record -> Home wins: {home_wins_09} - Home losses: {home_losses_09} - Home ties: {home_ties_09}')

# Question 6: give the record of October months for all games. 
# Answer: Oct record: 302-177-10

oct_wins, oct_losses, oct_ties = 0, 0, 0

for team, info in team_info.items():
    for game in info['games']:
        game_date = game[0]
        if datetime.datetime(int(game_date[:4]), int(game_date[5:7].lstrip('0')), int(game_date[8:10])).date().month == 10:
            if 'win' in game:
                oct_wins += 1
            elif 'loss' in game:
                oct_losses += 1
            else:
                oct_ties += 1
            
print(f'October record -> Oct wins: {oct_wins} - Oct losses: {oct_losses} - Oct ties: {oct_ties}')

# Question 6: give the record of years in range(1932 + 1, 1964) for all games. 
# Answer: 
range_win, range_looses, range_ties = 0, 0, 0
for team, info in team_info.items():
    for game in team_info[team]['games']:
        game_date = game[0]
        # game_date = 
        if 1964 > datetime.datetime(int(game_date[:4]), int(game_date[5:7].lstrip('0')), int(game_date[8:10])).date().year > 1932:
            if 'win' in game:
                range_win += 1
            elif 'loss' in game:
                range_looses += 1
            else:
                range_ties += 1
print(f'years range(1933, 1964) record -> range wins: {range_win} - range losses: {range_looses} - range ties: {range_ties}')