
def validity_check(choice: str) -> int:
    choice == choice.lower();
    if choice == "rock":
        return 2
    elif choice == "scissors":
        return 1
    elif choice == "paper":
        return 0
    else:
        raise ValueError("Illigal Choice!");

def check_winner(player1_choice: int, player2_choice: int) -> int:
    if player1_choice not in [0, 1, 2] or player2_choice not in [0, 1, 2]:
        raise ValueError("illegal game option");
    if player1_choice == player2_choice:
        return 0
    elif (player1_choice == 2 and player2_choice == 1) or \
         (player1_choice == 1 and player2_choice == 0) or \
         (player1_choice == 0 and player2_choice == 2):
        return 1
    else:
        return 2

def game_play():
    print("Welcome to Rock-Paper-Scissors!");
    player1_input = input("Player 1, please enter your choice (rock, paper, scissors): ");
    player2_input = input("Player 2, please enter your choice (rock, paper, scissors): ");

    try:
        player1_choice = validity_check(player1_input);
        player2_choice = validity_check(player2_input);
        result = check_winner(player1_choice, player2_choice);

        if result == 0:
            print("It's a tie!");
        elif result == 1:
            print("Player 1 is the winner!");
        else:
            print("Player 2 is the winner!");
    except ValueError as error:
        print(error);
