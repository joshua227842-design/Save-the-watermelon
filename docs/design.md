# P1: Design - Save the Watermelon
Joshua Vega

## Problem Statement
The goal of this project is to create a terminal-based word-guessing game. It is designed to be a fun way for users to test their vocabulary and logic skills in a simple interactive environment.

## Game Rules & Features
- The computer selects a random word from a list.
- The player must guess the word letter by letter.
- Correct guesses reveal the letter's position.
- Incorrect guesses reduce the "watermelon slices" (lives).
- The game starts with 6 slices.
- Win Condition: All letters are guessed correctly.
- Lose Condition: The player runs out of 6 slices.

## Data Design
- **Word List:** A list of strings containing secret words.
- **Guessed Letters:** A set to keep track of letters already entered.
- **Slice Counter:** An integer starting at 6 that tracks remaining lives.

## Basic
1. Start game and select secret wor.
2. Display masked word (underscores).
3. Take user input and validate it.
4. Update display or decreas slice counter.
5. Check for win/lose status and repeat if necessary.
