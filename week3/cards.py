import random

# Step I: List of card values
card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Step II: List of card suits
card_suits = ['Heart', 'Diamond', 'Club', 'Spade']

# Step III: Randomly pick one value and one suit as the answer
answer_value = random.choice(card_values)
answer_suit = random.choice(card_suits)

# Step IV: Ask the player to guess
print("Welcome to the Card Guessing Game!")
print("Try to guess the card!")
print("Possible values:", ", ".join(card_values))
print("Possible suits:", ", ".join(card_suits))

guess_value = input("Guess the card value: ").strip().capitalize()
guess_suit = input("Guess the card suit: ").strip().capitalize()

# Step V: Check the guess and give output
print(f"\nThe correct card was: {answer_value} of {answer_suit}\n")

if guess_value == answer_value and guess_suit == answer_suit:
    print("❤️ 😊 Congratulations! You guessed both correctly!")
elif guess_value == answer_value or guess_suit == answer_suit:
    print("😊 You guessed one part correctly!")
else:
    print("💔 Game Over! Better luck next time.")

