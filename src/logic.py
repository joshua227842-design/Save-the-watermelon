def check_victory(secret_word, guessed_letters):
    """Checks if all letters in the secret word have been guessed."""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True
