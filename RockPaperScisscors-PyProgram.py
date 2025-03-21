import random

emojis = {'r': '🪨', 's': '✂️', 'p': '📃'}
choices = ('r', 's', 'p')

while True:
    user_choice = input('Rock, Paper, or Scissors? (r/p/s): ').lower()
    
    if user_choice not in choices:
        print("Invalid choice")
        continue
#ad two numbers

    computer_choice = random.choice(choices)
    
    print(f'Your choice: {emojis[user_choice]}')
    print(f'Computer choice: {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'r' and computer_choice == 's') or 
        (user_choice == 's' and computer_choice == 'p') or 
        (user_choice == 'p' and computer_choice == 'r')
    ):
        print('You win!')
    else:
        print('You lose!')

    should_continue = input('Play again? (y/n): ').lower()
    if should_continue == 'n':
        break
