# Write your code here
from random import randrange

list_of_words = ['python', 'java', 'kotlin', 'javascript']
word = [char for char in list_of_words[randrange(0, 4)]]
hidden_words = ['-' for char in word]
guessed_letters = []

print("H A N G M A N")

while True:
    print("Type \"play\" to play the game, \"exit\" to quit:", end="")
    player_choice = input()

    if player_choice == "exit":
        exit()

    player_tries = 1
    while player_tries <= 8:
        print("\n" + ''.join(hidden_words))
        print('Input a letter:', end="")
        my_letter = input()

        # Letter check
        if len([char for char in my_letter]) > 1:
            print("You should input a single letter")
            continue
        elif not my_letter.islower():
            print("Please enter a lowercase English letter")
            continue
        elif type(my_letter) == int:
            print("Please enter a lowercase English letter")
            continue

        # Same letter twice Logic
        if my_letter in guessed_letters:
            print("You've already guessed this letter")
            continue

        # Checking availability logic
        if my_letter in word:
            for i in range(len(word)):
                if word[i] == my_letter:
                    hidden_words[i] = my_letter
        else:
            player_tries += 1
            print("That letter doesn't appear in the word")

        if '-' not in hidden_words:
            print("\n" + ''.join(hidden_words))
            print("You guessed the word!\nYou survived!")
            break

        guessed_letters.append(my_letter)

    if '-' in hidden_words:
        print("You lost!")
    exit()
