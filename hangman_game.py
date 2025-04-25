import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]
LIVES = 6
words = [
    "aardvark",
    "baleia",
    "camelo",
    "doninha",
    "elefante",
    "flamingo",
    "galinha",
    "hiena",
    "iguana",
    "jararaca",
    "kiwi",
    "lince",
    "morsa",
    "narval",
    "ovelha",
    "papagaio",
    "quati",
    "rinoceronte",
    "suricate",
    "tartaruga",
    "urso",
    "vagalume",
    "wallaby",
    "ximango",
    "yak",
    "zebra",
]
rand_word = random.choice(words)
l = len(rand_word)
guess_list = []
for i in range(l):
    guess_list.append("_")
# print(guess_list)
END_GAME = False
while not END_GAME:
    letter = input("Please enter a letter: ")
    if letter not in rand_word:
        LIVES -= 1
        print("Wrong.")
        print(stages[LIVES])
        if LIVES == 0:
            END_GAME = True
            print("You Lose")
            print(f"The word was {rand_word}")
    for i in range(l):
        if rand_word[i] == letter:
            guess_list[i] = letter
    guess = " ".join(guess_list)
    print(guess)
    if "_" not in guess_list:
        END_GAME = True
        print("You win")
