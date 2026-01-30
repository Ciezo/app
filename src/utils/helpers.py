# import os, sys 
# sys.path.append(os.path.dirname)

#####################
# file name:            helpers.py
# author:               cloydvansecuya@gmail.com
# date of creation:     January 30, 2026
# last date modified:   January 30, 2026
#####################


class Helpers():
    '''
    Utilize helper methods 
    '''

    def __init__(self):
        pass

    def sort(self, statistics) -> list:
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
        for player, records in statistics.items():
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