import random

words = ["python", "java", "hangman", "coding", "computer"]

word = random.choice(words)


guessed_word = ["_"] * len(word)


attempts = 6

guessed_letters = []

print("Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")

while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Attempts left:", attempts)
    print("Guessed letters:", guessed_letters)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n❌ Game Over! The word was:", word)
