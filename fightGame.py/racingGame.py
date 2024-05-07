import random 

track_length = 20
player_position = 0
opponent_position = 0

print("Welcome to the Racing Game!")
print("Race to the finish line to beat your opponent!")

while True:
    player_move = random.randint(1, 3)
    opponent_position += player_move
    
    if player_position >= track_length:
        print("Congratulations! You won the race!")
        break
    if opponent_position >= track_length:
        print("Oh no! The opponent won the race!")
        break
    
    print("Player:","-" * player_position + "TM")
    print("Opponent:","-" * opponent_position + "O")