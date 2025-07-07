# 0. Prompt the players for their names
# 1. Prompt player 1 for RPS
# 2. Prompt plyaer 2 for RPS
# 3. Compare p1 and p2 choices and decide a winner

#FIXES
# 1. Check for valid responses
# 2. Hide player input
# 3. Steamline/Refactor our code


def RPS():
    print("Welcome to Rock Paper Scissors!")
    
    # Gather Player names
    player1 = input("Player 1, Please enter your name: ")
    player2 = input("Player 2, please enter your name: ")

    # Gather Player moves
    p1_Choice = input(f"{player1}, choose between Rock, Paper, & Scissors: ").lower()

    while not IsValidMove(p1_Choice):
        print("Invalid Move! Please try again")
        p1_Choice = input(f"{player1}, choose between Rock, Paper, & Scissors: ").lower()

    p2_Choice = input(f"{player2}, choose between Rock, Paper, & Scissors: ").lower()

    while not IsValidMove(p2_Choice):
        print("Invalid Move! Please try again")
        p2_Choice = input(f"{player2}, choose between Rock, Paper, & Scissors: ").lower()

    # Compare Player moves
    if p1_Choice == p2_Choice:
        print("It's a draw!")

    elif p1_Choice == "rock" and p2_Choice == "scissors":
        print(f"Rock beats scissors, {player1} wins!")

    elif p1_Choice == "paper" and p2_Choice == "rock":
        print(f"paper beats rock, {player1} wins!")

    elif p1_Choice == "scissors" and p2_Choice == "paper":
        print(f"Scissors beats paper, {player1} wins!")

    elif p2_Choice == "rock" and p1_Choice == "scissors":
        print(f"Rock beats scissors, {player2} wins!")

    elif p2_Choice == "paper" and p1_Choice == "rock":
        print(f"paper beats rock, {player2} wins!")

    elif p2_Choice == "scissors" and p1_Choice == "paper":
        print(f"Scissors beats paper, {player2} wins!")
    

def IsValidMove(playerMove):
    validMoves = ["rock", "paper", "scissors"]

    if playerMove in validMoves:
        return True
    else:
        return False

RPS()

