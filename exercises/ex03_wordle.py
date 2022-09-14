"""This program will run like the Wordle Game and give users 6 tries to complete."""


__author__ = "730557183"


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn: int = 1
    print(f"=== Turn {turn}/6 === ")
    inputg = input_guess(5)
    emojified(inputg, secret)
    while inputg != secret and turn < 6:
        print(emojified(inputg, secret))
        turn += 1
        print(f"=== Turn {turn}/6 === ")
        inputg = input_guess(5)
    if inputg == secret and turn <= 6:
        print(f"You won in {turn}/6 turns!")
        print(emojified(secret, secret))
    elif inputg != secret and turn == 6:
        print("X/6 - Sorry. try again tomorrow!")
    
 
def contains_char(searched: str, searcher: str) -> bool:
    """This function will searched a word for a certain character and return boolean values based on the result."""
    assert len(searcher) == 1
    c: int = 0
    track: bool = False
    while not track and c < len(searched):
        if (searched[c] == searcher[0]):
            track = True
        else:
            c += 1
    if track:
        return True
    else:           
        return False 


def emojified(user_word: str, secret_word: str) -> str:
    """This function will compare the word the user inputs to the secret word and return colored boxes based on the matching values and indices."""
    assert len(user_word) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    s: str = ""
    j: int = 0
    while j < (len(user_word)):
        if (user_word[j] == secret_word[j]):
            s += GREEN_BOX
        elif contains_char(secret_word, user_word[j]):
            s += YELLOW_BOX
        else:
            s += WHITE_BOX
        j += 1   
    return s   


def input_guess(expected: int) -> str:
    """This function will compare an expected number to the length of the user's input and continue to prompt until they are equal."""
    guess: str = input(f"Enter a {expected} character word: ")
    while len(guess) != expected:
        guess: str = input(f"That wasn't {expected} chars! Try again: ")
    return guess


if __name__ == "__main__":
    main()