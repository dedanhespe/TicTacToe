from obj import *

#Main objects

plansza = Board()

##### Main functions

possible_moves = ["a1", "a2", "a3", 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

def move(player):
    global possible_moves
    while True:
      move = input("Podaj swój ruch {}: ".format(player.name))
      if move in possible_moves:
        plansza.play_to(move, player.sign)
        player.fields_occupied.append(move)
        possible_moves.remove(move)
        break
      else:
        print('Nie ma takiego ruchu!')

def player_won(player):
    if "a1" in player.fields_occupied and "a2" in player.fields_occupied and "a3" in player.fields_occupied:
        return True
    elif "b1" in player.fields_occupied and "b2" in player.fields_occupied and "b3" in player.fields_occupied:
        return True
    elif "c1" in player.fields_occupied and "c2" in player.fields_occupied and "c3" in player.fields_occupied:
        return True
    elif "a1" in player.fields_occupied and "b2" in player.fields_occupied and "c3" in player.fields_occupied:
        return True
    elif "a3" in player.fields_occupied and "b2" in player.fields_occupied and "c1" in player.fields_occupied:
        return True
    else:
        return False



### Main program ####

print("Witaj w grze w kółko i krzyżyk")
player_one_name = input("Podaj swoje imię graczu 1: ")
player_one = Player(player_one_name, "X")
player_two_name = input("Podaj swoje imię graczu 2: ")
player_two = Player(player_two_name, "O")

print("Zaczynamy grę! Oto plansza")

plansza.show()

while True:
    move(player_one)
    plansza.show()
    print(player_one.fields_occupied)
    if player_won(player_one) == True:
        print("Koniec gry")
        break
    move(player_two)
    print(player_two.fields_occupied)
    if player_won(player_two) == True:
        print("Koniec gry")
        break
    plansza.show()
