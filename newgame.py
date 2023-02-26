from random import *
import sys


dictionary = []

try:
    with open("files/vocab.txt", 'r') as f:
        for line in f:
            dictionary.append(line[0:-1])
except FileNotFoundError as error:
    print(error)
    sys.exit(0)

player_score = 0
computer_score = 0


def hanged_man(hangman):
    graphic = [
        """
            +-------+
            |
            |
            |
            |
            |
            == == == == == == == ==
        """,
        """
            +-------+
            |   |
            |   
            |
            |
            |
            == == == == == == == ==
        """,
        """
            +-------+
            |   |
            |   O
            |   
            |
            |
            == == == == == == == ==
        """,
        """
            +-------+
            |   |
            |   O
            |   |
            |
            |
            == == == == == == == ==

        """,
        """
            +-------+
            |   |
            |   O
            | - | 
            |
            |
            == == == == == == == ==
        """,
        """
            +-------+
            |   |
            |   O
            | - | -
            |  
            |
            == == == == == == == ==
        """,
        """
            +-------+
            |   |
            |   O
            | - | -
            |  / 
            |
            == == == == == == == ==
        """,
        """
            +-------+
            |   |
            |   O
            | - | -
            |  / \
            |
            == == == == == == == ==
        """
    ]

    print(graphic[hangman])


def start():
    print("Let’s play a game of Linux Hangman")

    while game():
        pass

    scores()


def guess_letter():
    print()

    letter = input("Take a guess at our mystery word:")

    letter.strip()
    letter.lower()

    print()

    return letter


def play_again():
    answer = input("Would you like to play again? y/n:")

    if answer in ("ÿ", "Y", "yes", "Yes", "Of Course"):
        return answer
    else:
        print("Thank you very much for playing our game. See you next time!")


def scores():
    global player_score, computer_score

    print("HIGH SCORES")
    print("Player : {}".format(player_score))
    print("Computer : {}".format(computer_score))


def game():
    word = choice(dictionary)
    word_length = len(word)

    clue = word_length * ["_"]

    tries = 7
    guesses = 0

    letters_tried = ""
    letters_right = 0
    letters_wrong = 0

    global computer_score, player_score

    while (letters_wrong != tries) and ("".join(clue) != word):
        print("".join(clue))

        letter = guess_letter()
        guesses += 1

        if len(letter) == 1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print(f'You’ve already picked, {letter}')
            else:
                letters_tried += letter
                first_index = word.find(letter)

                if first_index == -1:
                    letters_wrong += 1

                    print("Sorry letter isn’t what we’re looking for")
                else:
                    print("Congratulations letter is correct")

                    for i in range(word_length):
                        if letter == word[i]:
                            letters_right += 1
                            clue[i] = letter
        else:
            print("Choose another")

        hanged_man(letters_wrong)

        print("Guesses : {}".format("".join(letters_tried)))

        if letters_wrong == tries:
            print("Game Over")
            print(f'The word was {word}')

            computer_score += 1

            break

        if "".join(clue) == word:
            print("You Win!")
            print("The word was {}".format(word))

            player_score += 1

            break

    return play_again()


if __name__ == '__main__':
    start()
