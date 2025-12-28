# Hangman Game - Beginner Version

word = "python"          # secret word
guessed_letters = []     # letters guessed by the user
lives = 6                # number of chances

print("Welcome to Hangman!")

while lives > 0:
    display_word = ""
    
    # Show the word with guessed letters
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    
    print("\nWord:", display_word)
    print("Lives left:", lives)

    # Check if user has guessed the word
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word.")
        break

    guess = input("Guess a letter: ").lower()

    # Check if letter already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess not in word:
        print("❌ Wrong guess!")
        lives -= 1
    else:
        print("✅ Correct guess!")

# If lives are over
if lives == 0:
    print("\n😢 You lost! The word was:", word)
