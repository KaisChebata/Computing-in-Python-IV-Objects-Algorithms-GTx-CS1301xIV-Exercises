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
# you'll be asked to return statistics about a certain team from the data set,
# each team should has the following statistics: 
# games, 
# total wins, home wins, away wins, neutral wins, 
# total losses, home losses, away losses, neutral losses, 
# total ties, home ties, away ties, neutral ties, 
# points for, points against.
# 

# Question 1: what is the total Points scored by Auburn team
# print ('Auburn points for {0}'.format(team_info['Auburn']['points for']))

# Questoin 2: what is the total Points scored by the Georgia team against Auburn team
# print ('Auburn points against {0}'.format(team_info['Auburn']['points against']))

#This line will open the file:
# record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
history_file_path = 'Final_Problem_Set\\Raw_files\\georgia_tech_football.csv'







def gt_csv_to_dict(filename):
    with open(filename, 'r') as record_file:
        rows = record_file.read().split('\n')
        # delete header
        del rows[0]
        # debugging graded file
        if rows[-1] == '':
            del rows[-1]
        team_info = {}

        for row in rows:
            row = row.split(',')
            # massage data
            teamname = row[1]
            row[3] = int(row[3])
            row[4] = int(row[4])
            if teamname not in team_info.keys():
                team_info[teamname] = {'games': [],
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


            team_dict = team_info[teamname]
            if row[3] > row[4]:
                team_dict['total wins'] += 1
                row.append('win')
                if row[2] == 'Home':
                    team_dict['home wins'] += 1
                elif row[2] == 'Away':
                    team_dict['away wins'] += 1
                else:
                    team_dict['neutral wins'] += 1
            elif row[3] == row[4]:
                team_dict['total ties'] += 1
                row.append('tie')
                if row[2] == 'Home':
                    team_dict['home ties'] += 1
                elif row[2] == 'Away':
                    team_dict['away ties'] += 1
                else:
                    team_dict['neutral ties'] += 1
            else:
                team_dict['total losses'] += 1
                row.append('loss')
                if row[2] == 'Home':
                    team_dict['home losses'] += 1
                elif row[2] == 'Away':
                    team_dict['away losses'] += 1
                else:
                    team_dict['neutral losses'] += 1
            team_dict['points for'] += row[3]
            team_dict['points against'] += row[4]
            team_info[teamname]['games'].append(row)
        return team_info

import datetime
from pprint import pprint
file_name_path = 'Final_Problem_Set\\Raw_files\\georgia_tech_football.csv'
pprint(gt_csv_to_dict(file_name_path))

def earliest_game(file_dict):
    first_game = {'team': '',
                  'date': None}
    for key in file_dict.keys():
        games = sorted(file_dict[key]['games'])
        game1 = games[0][0]
        game1 = datetime.datetime(int(game1[:4]), int(game1[5:7].lstrip('0')), int(game1[8:10])).date().strftime('%Y-%m-%d')
        if first_game['date'] is None:
            first_game['date'] = game1
            first_game['team'] = key
        elif game1 < first_game['date']:
            first_game['date'] = game1
            first_game['team'] = key
    return first_game

# team_info = gt_csv_to_dict(file_name_path)
# fgame = earliest_game(team_info)
# print ('Earliest game was {0} against {1}'.format(fgame['date'], fgame['team']))