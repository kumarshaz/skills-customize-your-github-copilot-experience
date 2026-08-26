
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a playable Hangman game using Python strings, loops, conditionals, user input, and random selection. Practice tracking game state while giving the player clear feedback after every guess.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Create the starting state for a Hangman game. Select a secret word from a predefined list and prepare the values needed to track the player's progress and incorrect guesses.

#### Requirements
Completed program should:

- Store multiple possible words in a predefined list.
- Randomly select one word from the list for each game.
- Display the hidden word as underscores, such as `_ _ _ _`.
- Set and track a fixed number of incorrect guesses the player may make.

### 🛠️ Implement the Guessing Gameplay

#### Description
Add the game loop so the player can guess letters, reveal matching letters, and finish the game by guessing the word or using all available attempts.

#### Requirements
Completed program should:

- Accept a letter guess from the player during each turn.
- Reveal every occurrence of a correctly guessed letter in the displayed word.
- Reduce the remaining attempts when the player guesses incorrectly.
- Continue until the player guesses the complete word or has no attempts remaining.
- Display a clear win message or lose message when the game ends.
