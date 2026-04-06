# P2: Pseudocode - Game Logic
 Joshua Vega

FUNCTION main_game_loop:
  secret_word = select_random_word()
  guessed_letters = empty set
  slices = 6
  
  WHILE slices > 0:
    DISPLAY masked_word
    PROMPT user for "letter"
    
    IF letter is valid AND not guessed:
      ADD letter TO guessed_letters
      IF letter is not in secret_word:
        slices = slices - 1
    ELSE:
      DISPLAY "Invalid or already guessed"
      
    IF all letters guessed:
      DISPLAY "You win!"
      BREAK
      
  IF slices == 0:
    DISPLAY "Game Over"
END FUNCTION
