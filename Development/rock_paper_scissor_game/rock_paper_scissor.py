import random
from rock_paper_scissor_end_user_import import end_game


def play():
    user = ""
    user_score = 0
    computer_score = 0
    # Declaring variables.

    def user_wins(user, computer):
        user_wins = {
            "rock": "scissor",
            "paper": "rock",
            "scissor": "paper",
        }

    while user not in end_game:  # While true.
        ## Scoreboard :
        # print(f"Your score: {user_score} Computer score: {computer_score}")
        # print(f"You {user_score} : {computer_score} Computer")
        print(f"You {user_score} VS Computer {computer_score}\n")

        choices = ["rock", "paper", "scissor", "r", "p", "s", "scissors"]

        # computer_input()
        def computer_choices():
            computer = random.choice(choices)

        # user_input()
        def user_choices():
            user = input(
                "What's your choice? 'r' for rock, 'p' for paper, 's' for scissor\n"
            )
            user = user.lower().strip()

        def input_validation():
            if user not in choices:
                print("Invalid input. Please try again.")
                continue

        def game_logic_processing():
            # User quits.
            if user in end_game:  # Look into it.
                print("Thanks for playing! Goodbye!")
            # Invalid input.
            if user not in choices:
                print("Invalid input. Please try again.")
                continue
            # Tie
            elif user == computer:
                print(f"I choose {computer} too. It's a tie!")
            # User wins
            elif user_wins(user, computer):
                print(f"I choose {computer}. You win!")
                user_score += 1
            # User losses
            else:
                print(f"I choose {computer}. You lose!")
                computer_score += 1

    def main():
        play()


if __name__ == "__main__":
    main()

# TODO: Input validation?
# TODO: Two players.
# TODO: Computer vs Computer.
# TODO: You Vs Computer.
# TODO: Design a GUI.
# TODO: OOP and Good Design.
# TODO: Docstrings and comments.
# TODO: Add more input perms and combs for r, p, s.
# TODO: Console Based Game Only.
# TODO: Tkinter Based GUI Game.
# TODO: Package both GUI and Console Based Game.
# TODO: Create a webapp of it using Python Programming Language.
# TODO: Create a webapp of it using Django Framework, Flask Framework, and FastAPI Framework.
# TODO: Create a webapp of it, using JavaScritp, HTML, and CSS.
