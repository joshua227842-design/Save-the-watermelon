import random

# Academic word list for the project
WORD_DATABASE = ["PYTHON", "ALGORITHM", "VARIABLE", "FUNCTION", "DATABASE"]

def get_random_word():
    """Returns a random word from the database."""
    return random.choice(WORD_DATABASE)
