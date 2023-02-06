import random

def computer_turn(computer_score, player_score):
    turn_score = 0
    while True:
        dice = random.randint(1, 6)
        if dice == 1:
            turn_score = 0
            print(f"Roll 1 Computer loss.  player turn!")
            break
        else:
            turn_score += dice
            print(f"Computer add {dice} now {turn_score}")
            if turn_score + computer_score >= 100:
                break
            elif random.choice([True, False]):
                computer_score+= turn_score
                print(f"Computer {computer_score} score")
                break
    return turn_score

def player_turn(player_score):
    turn_score = 0
    roll = "y"
    while roll == "y":
        dice = random.randint(1, 6)
        if dice == 1:
            turn_score = 0
            print("Roll1 player loss. Computer turn!")
            break
        else:
            turn_score += dice
            print(f"You add {dice}. now {turn_score}")
            if turn_score + player_score >= 100:
             break
            roll = input("Roll again? (y/n)")
    player_score += turn_score
    print(f"player  {player_score} score")
    return turn_score

def play_game():
    player_score = 0
    computer_score = 0
    while player_score < 100 and computer_score < 100:
        player_score += player_turn(player_score)
        if player_score >= 100:
            break
        computer_score += computer_turn(computer_score, player_score)
        if computer_score >= 100:
            break
        print(f"Player score: {player_score}, Computer score: {computer_score}")
    if player_score >= 100:
        print("You win!")
    else:
        print("Computer win!")

play_game()

