import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def play_game():
    print("\n🎮 Rock-Paper-Scissors Game 🎮")
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("\nChoose rock, paper, or scissors: ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("⚠ Invalid choice. Try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"🤖 Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "user":
            user_score += 1
            print("✅ You win this round!")
        elif winner == "computer":
            computer_score += 1
            print("❌ Computer wins this round!")
        else:
            print("🤝 It's a tie!")

        print(f"📊 Score -> You: {user_score}, Computer: {computer_score}")

        play_again = input("Play another round? (y/n): ").lower()
        if play_again != 'y':
            print("👋 Thanks for playing!")
            break

play_game()
