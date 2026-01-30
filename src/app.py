#!/usr/bin/env python3

#####################
# file name:            app.py
# author:               cloydvansecuya@gmail.com
# date of creation:     January 30, 2026
# last date modified:   January 30, 2026
#####################

import os, sys 
sys.path.append(os.path.dirname)

from collections import Counter
from collections import OrderedDict

# from src.utils.helpers import Helpers

'''
Skill Test:
League Table
The LeagueTable class tracks the score of each player in a league. After each game, the player records their score with the record_result function.

The player's rank in the league is calculated using the following logic:
1. The player with the highest score is ranked first (rank 1).
     The player with the lowest rank is ranked last.
2. If two players are tied on score, then the player who has played the fewest games is ranked higher.
3. If two players are tied on score and number of games played, then the player who was first in the list of players is ranked higher.

Implement the player_rank function that returns the player at the given rank.

For example:
table = LeagueTable(['Mike'. 'Chris', Árnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)
print(table.player_rank(1))

All players have the same score. However, Arnold and Chris have played fewer games than Mike, and Chris is before Arnold in the list of players, he is ranked first. 
Therefore, the code above should display "Chris".
'''

class LeagueTable:
    '''
    This source is responsible for recording player names and their respective scores and number of games played.
    '''

    def __init__(self, players) -> None:
        '''
        Initialize this `LeagueTable` class to denote the list of players in their respective indices and order along with 
        values for 'games_played` and 'score'        
        :param self: Description
        :param players: Description
        '''
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score) -> None:
        '''
        Assign values to the key player, where each player is element str 
        '''
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score
     
    def player_rank(self, rank) -> str:
        '''
        Query the player rank in the sorted list (winners)
        '''
        listings = self.sort()
        return listings[rank]
    
    def sort(self) -> list:
        '''
        Sort and arrange the elements by index individually.
        
        Equality and inequality operation by this logic proposition 
        compare the elements[i]...elements[(i+1)-1]
                    element nth.......tail....-1
                                  ^    ^^      ^
                                        ^
        '''
        player_ls = []
        score_ls = []
        no_of_games_played = []
        
        # Access collections
        # https://stackoverflow.com/questions/10058140/accessing-items-in-an-collections-ordereddict-by-index
        for player, records in self.standings.items():
            player_ls.append(player)                                # original list of players 
            score_ls.append(records['score'])                       # by score 
            no_of_games_played.append(records['games_played'])      # by number of games of played
            sorted_ls = list(range(len(player_ls)))                 # sorted list, arranged by indices (manipulating)

        # Check operations
        ## Compare each player by its score and number of games played
        for i in range(len(player_ls)):
            ## Check by score 
            ### if (player['score'][i] >= player['score'][ (i+1)-1 ])
            if (score_ls[i] >= score_ls[ (i+1)-1 ]):
                sorted_ls[i] = player_ls[i]
            
            ## Check when tied score 
            ### elif (player['score'][i] == player['score'][ (i+1)-1 ])
            ###     if (player['games_played'][i] < player['games_played'][ (i+1)-1 ])
            elif (score_ls[i] == score_ls[ (i+1)-1 ]):
                if (no_of_games_played[i] < no_of_games_played[ (i+1)-1 ]):
                    sorted_ls[i] = player_ls[i]

            ## Otherwise, when scores and number of games played are both tied then, consider the original indices of players
            else:
                sorted_ls = player_ls

        return sorted_ls

if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(1))