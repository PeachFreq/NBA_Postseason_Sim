import pandas as pd
import random as rnd

N = 1000 # Number of simulations to run

# Build a dataframe called `babyRaw` that stores all the regular season matchups between OKC and UTA
babyRaw = pd.read_csv('./OKC_vs_UTA.csv')
babyRaw['OKCWeightContribution'] = babyRaw['TeamPoints']*babyRaw['RecencyBias']
babyRaw['UTAWeightContribution'] = babyRaw['OpponentPoints']*babyRaw['RecencyBias']
OKCWeight = babyRaw['OKCWeightContribution'].sum()
UTAWeight = babyRaw['UTAWeightContribution'].sum()

# Simulate a game - returns True if OKC wins
def simGame():  # For the moment doing no arguments, but this is something we can change...
    x = 1 / (1 + UTAWeight / OKCWeight) # Set divider point x; prepare to roll the loaded die
    return rnd.random() < x

# Simulate a round - returns True if OKC wins
def simRound():
    teamWins = 0
    teamLosses = 0
    for i in range (7):
        if simGame() == True:
            teamWins += 1
            print(f'Game {i+1} result: OKC wins')
        else:
            teamLosses += 1
            print(f'Game {i+1} result: UTA wins')
    if teamWins >= 4:
        print('Oklahoma City Thunders on to Round 2 of the playoffs!')
    else:
        print('Utah Jazz win the series!')
    return teamWins >= 4
round1 = simRound()