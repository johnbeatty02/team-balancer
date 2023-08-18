import csv
from itertools import combinations
import random
import numpy as np


def load_csv(filename: str) -> list[list[str]]:
    with open(filename, mode='r') as file:
        csvFile = csv.reader(file)
        contents = [i for i in csvFile][1:]  # Removes header
    return contents


# Loads in stats for each game
bedwars = load_csv('bedwars.csv')
bridgeDuels = load_csv('bridgeDuels.csv')
buildBattle = load_csv('buildBattle.csv')
miniWalls = load_csv('miniWalls.csv')
parkourDuels = load_csv('parkourDuels.csv')
partyGames = load_csv('partyGames.csv')
skywars = load_csv('skywars.csv')
uhcDuels = load_csv('uhcDuels.csv')

allStats = [bedwars, bridgeDuels, buildBattle, miniWalls, parkourDuels, partyGames, skywars, uhcDuels]


def list_to_dict(game: list) -> dict:
    return {item[0]: item[1] for item in game}


# Converts the impored lists to dictionaries for each game
bedwarsDict = list_to_dict(bedwars)
bridgeDuelsDict = list_to_dict(bridgeDuels)
buildBattleDict = list_to_dict(buildBattle)
miniWallsDict = list_to_dict(miniWalls)
parkourDuelsDict = list_to_dict(parkourDuels)
partyGamesDict = list_to_dict(partyGames)
skywarsDict = list_to_dict(skywars)
uhcDuelsDict = list_to_dict(uhcDuels)

dictionaries = [bedwarsDict, bridgeDuelsDict, buildBattleDict, miniWallsDict, parkourDuelsDict, partyGamesDict,
                skywarsDict, uhcDuelsDict]

with open('players.txt') as f:
    lines = f.readlines()
    players = [i.rstrip() for i in lines]

# Generates all possible teams (1820)
possibleTeams = list(combinations(players, 4))
possibleTeams = [list(i) for i in possibleTeams]


def select_teams(possible_teams, num_teams, players_per_team):
    selected_teams = []
    used_players = []

    for _ in range(num_teams):
        available_teams = [team for team in possible_teams if all(player not in used_players for player in team)]

        if not available_teams:
            break  # No more available teams

        selected_team = random.choice(available_teams)
        selected_teams.append(selected_team)
        used_players.extend(selected_team)

    return selected_teams


generated_teams = select_teams(possibleTeams, 4, 4)
print(generated_teams)
output = False
if output:
    for idx, team in enumerate(generated_teams, start=1):
        print(f"Team {idx}: {team}")


# Calculate averages for each game
def bedwarsAverage(team_to_analyze: list) -> float:
    points = [float(bedwarsDict[player]) for player in team_to_analyze]  # Gets each player's bedwars average
    teamAverage = sum(points) / len(points)
    return teamAverage


def bridgeDuelsAverage(team_to_analyze: list) -> float:
    points = [float(bridgeDuelsDict[player]) for player in team_to_analyze]  # Gets each player's bridge average
    teamAverage = sum(points) / len(points)
    return teamAverage


def buildBattleAverage(team_to_analyze: list) -> float:
    points = [float(buildBattleDict[player]) for player in team_to_analyze]  # Gets each player's Build Battle average
    teamAverage = sum(points) / len(points)
    return teamAverage


def miniWallsAverage(team_to_analyze: list) -> float:
    points = [float(miniWallsDict[player]) for player in team_to_analyze]  # Gets each player's Mini Walls average
    teamAverage = sum(points) / len(points)
    return teamAverage


def parkourDuelsAverage(team_to_analyze: list) -> float:
    points = [float(parkourDuelsDict[player]) for player in team_to_analyze]  # Gets each player's Parkour Duels average
    teamAverage = sum(points) / len(points)
    return teamAverage


def partyGamesAverage(team_to_analyze: list) -> float:
    points = [float(partyGamesDict[player]) for player in team_to_analyze]  # Gets each player's Parkour Duels average
    teamAverage = sum(points) / len(points)
    return teamAverage


def skywarsAverage(team_to_analyze: list) -> float:
    points = [float(skywarsDict[player]) for player in team_to_analyze]  # Gets each player's skywars average
    teamAverage = sum(points) / len(points)
    return teamAverage


def uhcDuelsAverage(team_to_analyze: list) -> float:
    points = [float(uhcDuelsDict[player]) for player in team_to_analyze]  # Gets each player's skywars average
    teamAverage = sum(points) / len(points)
    return teamAverage


# Figure out how "good" this set of teams is
# Currently uses standard deviation of all point values. Could probably figure out something better later.
# For now, the LOWER the closeness index, the better the teams are.
def closenessIndex(set_of_teams: list) -> float:
    bedwars_averages = [bedwarsAverage(i) for i in set_of_teams]
    bridgeDuels_averages = [bridgeDuelsAverage(i) for i in set_of_teams]
    buildBattle_averages = [buildBattleAverage(i) for i in set_of_teams]
    miniWalls_averages = [miniWallsAverage(i) for i in set_of_teams]
    parkourDuels_averages = [parkourDuelsAverage(i) for i in set_of_teams]
    partyGames_averages = [partyGamesAverage(i) for i in set_of_teams]
    skywars_averages = [skywarsAverage(i) for i in set_of_teams]
    uhcDuels_averages = [uhcDuelsAverage(i) for i in set_of_teams]

    all_averages = [bedwars_averages, bridgeDuels_averages, buildBattle_averages, miniWalls_averages,
                    parkourDuels_averages, partyGames_averages, skywars_averages, uhcDuels_averages]

    stdev = round(float(np.std(all_averages)), 3)  # This can be changed to the desired "closeness metric"

    return stdev


# Outputs results
with open('output.txt', 'w') as f:
    # Generates a set number of teams and calculates a closeness index for each set
    for i in range(1000):
        f.write(f'Set {str(i+1)}: ')
        generated_teams = select_teams(possibleTeams, 4, 4)
        print(generated_teams)

        closeness_index = closenessIndex(generated_teams)
        print(closeness_index)
        f.write(f'{str(closeness_index)} ')
        f.write(f'{str(generated_teams)}\n')
