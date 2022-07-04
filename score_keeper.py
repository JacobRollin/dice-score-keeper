scores = []
players = []
OG_winning_player = ''
winning_player = ''

def add_players():
    global scores, players
    num_of_players = int(input('Please input number of players: '))
    if num_of_players > 6 or num_of_players <= 1:
        return print('Please select a number of players between 2 and 6.'), add_players()
    else:
        i = 1
        while i <= num_of_players:
            players.append(input('Enter name of player ' + str(i) + ': '))
            scores.append(0)
            i += 1
    return print('\n'), print(players), print(scores)

def score_keeper(win_value):
    global scores, players, winning_player, OG_winning_player
    i = 0
    if scores[i] < win_value:
        while i < len(players):
            turn_score = input('Enter score for ' + players[i] + ': ')
            scores[i] = scores[i] + int(turn_score)
            print(players)
            print(scores)
            if scores[i] >= win_value:
                OG_winning_player = players[i]
                return print('\n'), print(players[i] + ' has gone out with a score of ' + str(scores[i]) + '.\n'), print(players, '\n', scores, '\n')
            i += 1
        return score_keeper(10000)

def final_roll():
    global scores, players, winning_player, OG_winning_player
    winning_player = OG_winning_player
    print(winning_player + ' has ' + str(scores[players.index(winning_player)]) + ' points.\n')
    for player in players:
        if player == OG_winning_player:
            continue
        else:
            print(player + ' needs ' + str((scores[players.index(winning_player)] - scores[players.index(player)]) + 50) + ' to take the lead!\n')
            final_roll_score = input('Enter score for ' + player + ': ')
            scores[players.index(player)] = scores[players.index(player)] + int(final_roll_score)
            if scores[players.index(player)] > scores[players.index(winning_player)]:
                winning_player = player
                print(winning_player + ' is now in the lead with a score of ' + str(scores[players.index(winning_player)]))
                print(players)
                print(scores)
                print('\n')
    return print(winning_player + ' wins with a score of ' + str(scores[players.index(winning_player)])), print(players), print(scores)

add_players()
score_keeper(10000)
final_roll()