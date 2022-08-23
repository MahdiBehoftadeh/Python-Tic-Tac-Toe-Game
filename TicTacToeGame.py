# From https://behoftadeh.ir Written by Mahdi Behoftadeh

# This is a simple Tic Tac Toe game made by Python.
# This game takes two player names and will continue to take a movement in range of 1-9 and displays each players movements
# and when there's 3 numbers in a row the player will win the game.

# Apache License
# Version 2.0, January 2004
# http://www.apache.org/licenses/

name_player_1 = input('Enter player 1\'s name: ')
name_player_2 = input('Enter player 2\'s name: ')

arr_remaining_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr_player_1 = [];
arr_player_2 = [];

is_player_1_chosen = False
is_game_finished = False

while len(arr_remaining_moves) != 0 :
    if len(arr_remaining_moves) == 1:
        move_player_1 = input('\n' + name_player_1 + '\'s moves: ' + str(arr_player_1) + '\n' + name_player_2 + '\'s moves: ' + str(arr_player_2) + '\nremaining moves: ' + str(arr_remaining_moves) + '\n(' + name_player_1 + ') Choose your move: ')
        if move_player_1.isnumeric():
            if int(move_player_1) > 0 and int(move_player_1) < 10:
                if int(move_player_1) in arr_remaining_moves:
                    arr_player_1.append(int(move_player_1))
                    arr_remaining_moves.remove(int(move_player_1))

                    if (1 in arr_player_1 and 2 in arr_player_1 and 3 in arr_player_1) or (4 in arr_player_1 and 5 in arr_player_1 and 6 in arr_player_1) or (7 in arr_player_1 and 8 in arr_player_1 and 9 in arr_player_1) or (1 in arr_player_1 and 4 in arr_player_1 and 7 in arr_player_1) or (2 in arr_player_1 and 5 in arr_player_1 and 8 in arr_player_1) or (3 in arr_player_1 and 6 in arr_player_1 and 9 in arr_player_1) or (1 in arr_player_1 and 5 in arr_player_1 and 9 in arr_player_1) or (3 in arr_player_1 and 5 in arr_player_1 and 7) in arr_player_1:
                        print(name_player_1 + ' Won!\n' + name_player_1 + '\'s moves: ' + str(arr_player_1) + '\n' + name_player_2 + '\'s moves: ' + str(arr_player_2) + '\nremaining moves: ' + str(arr_remaining_moves))
                        is_game_finished = True
                        break

                else:
                    print('ERROR-001: This move is already taken.')
                    continue
            else:
                print('ERROR-002: Move is not in in range(1-9).')
                continue
        else:
            print('ERROR-003: Input must be numeric.')
            continue
    else:
        if not is_player_1_chosen:
            move_player_1 = input('\n' + name_player_1 + '\'s moves: ' + str(arr_player_1) + '\n' + name_player_2 + '\'s moves: ' + str(arr_player_2) + '\nremaining moves: ' + str(arr_remaining_moves) + '\n(' + name_player_1 + ') Choose your move: ')
            if move_player_1.isnumeric():
                if int(move_player_1) > 0 and int(move_player_1) < 10:
                    if int(move_player_1) in arr_remaining_moves:
                        arr_player_1.append(int(move_player_1))
                        arr_remaining_moves.remove(int(move_player_1))
                        is_player_1_chosen = True

                        if (1 in arr_player_1 and 2 in arr_player_1 and 3 in arr_player_1) or (4 in arr_player_1 and 5 in arr_player_1 and 6 in arr_player_1) or (7 in arr_player_1 and 8 in arr_player_1 and 9 in arr_player_1) or (1 in arr_player_1 and 4 in arr_player_1 and 7 in arr_player_1) or (2 in arr_player_1 and 5 in arr_player_1 and 8 in arr_player_1) or (3 in arr_player_1 and 6 in arr_player_1 and 9 in arr_player_1) or (1 in arr_player_1 and 5 in arr_player_1 and 9 in arr_player_1) or (3 in arr_player_1 and 5 in arr_player_1 and 7) in arr_player_1:
                            print(name_player_1 + ' Won!\n' + name_player_1 + '\'s moves: ' + str(arr_player_1) + '\n' + name_player_2 + '\'s moves: ' + str(arr_player_2) + '\nremaining moves: ' + str(arr_remaining_moves))
                            is_game_finished = True
                            break

                    else:
                        print('ERROR-004: This move is already taken.')
                        continue
                else:
                    print('ERROR-005: Move is not in in range(1-9).')
                    continue
            else:
                print('ERROR-006: Input must be numeric.')
                continue
    
        move_player_2 = input('\n' + name_player_1 + '\'s moves: ' + str(arr_player_1) + '\n' + name_player_2 + '\'s moves: ' + str(arr_player_2) + '\nremaining moves: ' + str(arr_remaining_moves) + '\n(' + name_player_2 + ') Choose your move: ')
        if move_player_2.isnumeric():
            if int(move_player_2) > 0 and int(move_player_2) < 10:
                if int(move_player_2) in arr_remaining_moves:
                    arr_player_2.append(int(move_player_2))
                    arr_remaining_moves.remove(int(move_player_2))
                    is_player_1_chosen = False

                    if (1 in arr_player_2 and 2 in arr_player_2 and 3 in arr_player_2) or (4 in arr_player_2 and 5 in arr_player_2 and 6 in arr_player_2) or (7 in arr_player_2 and 8 in arr_player_2 and 9 in arr_player_2) or (1 in arr_player_2 and 4 in arr_player_2 and 7 in arr_player_2) or (2 in arr_player_2 and 5 in arr_player_2 and 8 in arr_player_2) or (3 in arr_player_2 and 6 in arr_player_2 and 9 in arr_player_2) or (1 in arr_player_2 and 5 in arr_player_2 and 9 in arr_player_2) or (3 in arr_player_2 and 5 in arr_player_2 and 7) in arr_player_1:
                        print(name_player_2 + ' Won!\n' + name_player_1 + '\'s moves: ' + str(arr_player_1) + '\n' + name_player_2 + '\'s moves: ' + str(arr_player_2) + '\nremaining moves: ' + str(arr_remaining_moves))
                        is_game_finished = True
                        break

                else:
                    print('ERROR-007: This move is already taken.')
                    continue
            else:
                print('ERROR-008: Move is not in in range(1-9).')
                continue
        else:
            print('ERROR-009: Input must be numeric.')
            continue

if not is_game_finished:
    print('Draw!\n' + name_player_1 + '\'s moves: ' + str(arr_player_1) + '\n' + name_player_2 + '\'s moves: ' + str(arr_player_2) + '\nremaining moves: ' + str(arr_remaining_moves))