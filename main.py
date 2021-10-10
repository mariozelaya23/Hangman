import os, random, images, words

word = random.choice(words.hm_words)
word = word.upper()
reveal = list(len(word)*'_')
lives = 7
gameWon = False


def check_letter(letter, word):
    global reveal
    for i in range(0, len(word)):
        letter = word[i]
        if guess == letter:
            reveal[i] = guess
    if '_' not in reveal:
        return True
    else:
        return False


def status():
    os.system('cls')
    print(images.hangman[7-lives])
    print(' '.join([str(e) for e in reveal]))
    print(f"You have {lives} lives")


while not gameWon and lives > 0:
    status()
    guess = input("Guess a letter or entire word: ")
    guess = guess.upper()

    if guess == word:
        gameWon = True
        reveal = word
    elif len(guess) == 1 and guess in word:
        gameWon = check_letter(guess, word)
    else:
        lives -= 1
    status()

if gameWon:
    print("You won")
else:
    print(f"Failed, word was: {word}")




