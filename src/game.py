from src.words import get_random_word

def start_game():
    secret_word = get_random_word()
    guessed = set()
    slices = 6
    print("--- Save the Watermelon ---")
    while slices > 0:
        display = [c if c in guessed else "_" for c in secret_word]
        print(f"\nWord: {' '.join(display)} | Slices: {slices}")
        if "_" not in display:
            print("Victory! You saved the watermelon! 🎉")
            return
        pick = input("Letter: ").upper()
        if pick.isalpha() and len(pick) == 1 and pick not in guessed:
            guessed.add(pick)
            if pick not in secret_word:
                slices -= 1
        else:
            print("Invalid or repeated letter.")
    print(f"Game Over. The word was: {secret_word}")

if __name__ == "__main__":
    start_game()
