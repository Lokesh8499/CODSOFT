import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'You win!'
    else:
        return 'Computer wins!'

def play():
    user_score = 0
    computer_score = 0
    
    while True:
        user_input = input("Enter rock, paper, or scissors (or type 'quit' to exit): ").lower()
        
        if user_input == 'quit':
            print("Goodbye! Thanks for playing!")
            break
        
        if user_input not in ['rock', 'paper', 'scissors']:
            print("That's not a valid choice! Try again.")
            continue
        
        computer_input = get_computer_choice()
        print(f"Computer chose: {computer_input}")
        print(f"You chose: {user_input}")
        
        result = get_result(user_input, computer_input)
        print(result)
        
        if result == 'You win!':
            user_score += 1
        elif result == 'Computer wins!':
            computer_score += 1
        
        print(f"Score - You: {user_score} | Computer: {computer_score}")
        print("")

if __name__ == "__main__":
    play()