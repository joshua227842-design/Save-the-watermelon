import random

# Lista de palabras para el juego
WORDS = ["PYTHON", "ALGORITHM", "VARIABLE", "FUNCTION", "DATABASE"]

def get_random_word():
    """Devuelve una palabra al azar de la lista."""
    return random.choice(WORDS)
