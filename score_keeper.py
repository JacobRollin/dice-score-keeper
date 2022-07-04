from numbers import Number


players_and_scores = {}
OG_winning_player = ''
winning_player = ''

def add_players():
    global players_and_scores
    num_of_players = int(input('Please input number of players: '))
    if num_of_players > 6 or num_of_players <= 1:
        return print('Please select a number of players between 2 and 6.'), add_players()
    else:
        i = 1
        while i <= num_of_players:
            player = (input('Enter name of player ' + str(i) + ': '))
            players_and_scores[player] = 0
            i += 1
    return print('\n'), print(players_and_scores)

def score_keeper(win_value):
    global players_and_scores, winning_player, OG_winning_player
    i = 0
    for player in players_and_scores:
        turn_score = input('Enter score for {player}: '.format(player=player))
        players_and_scores[player] = players_and_scores[player] + int(turn_score)
        print(players_and_scores)
        if players_and_scores[player] >= win_value:
            OG_winning_player = player
            return print('\n'), print('{player} has gone out with a score of {score}.\n'.format(player=player, score=players_and_scores[player])), print(players_and_scores)
        i += 1
    return score_keeper(10000)

def final_roll():
    global players_and_scores, winning_player, OG_winning_player
    winning_player = OG_winning_player
    print('{player} has {score} points.\n'.format(player=winning_player, score=players_and_scores[winning_player]))
    for player in players_and_scores:
        if player == OG_winning_player:
            continue
        else:
            print('{player} needs {score} to take the lead!\n'.format(player=player, score=(players_and_scores[winning_player] - players_and_scores[player]) + 50))
            final_roll_score = input('Enter score for {player}: '.format(player=player))
            players_and_scores[player] = players_and_scores[player] + int(final_roll_score)
            if players_and_scores[player] > players_and_scores[winning_player]:
                winning_player = player
                print('{player} is now in the lead with a score of {score}'.format(player=player, score=players_and_scores[player]))
                print(players_and_scores)
    return print('{player} wins with a score of {score}'.format(player=winning_player, score=players_and_scores[winning_player])), print(players_and_scores)
    
add_players()
score_keeper(10000)
final_roll()