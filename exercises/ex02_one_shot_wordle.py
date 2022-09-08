"""Wordle game that gives you one try."""

__author__ = "730557183"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
 
secret_word: str = "python" 
user_word: str = input("What is your 6-letter guess? ")
j: int = 0
s: str = ""
# If the input word of the user doesn't match the length 
# of the secret word we tell them to try again.
while len(user_word) != len(secret_word):
    user_word: str = input("That was not 6 letters! Try again: ")

# While the integer j is less than what the user inputed 
# we will run this code to determine what color each box will be
while j <= (len(user_word) - 1):
    if (user_word[j] == secret_word[j]):
        s = s + GREEN_BOX
    else:
        c: int = 0
        track: bool = False
        while not track and c <= (len(user_word) - 1):
            if (user_word[j] == secret_word[c]):
                track = True
            else:
                c = c + 1  
        if track:
            s = s + YELLOW_BOX
        else:           
            s = s + WHITE_BOX
    j = j + 1    
# This looop above, if the box isn't green, will determine whether it's 
# yellow or white. We use another while loop to compare the current index
# of the user_word with each index of the secret_word until either we find a match 
# or we don't find any match and then it will be a white box as the bool value will still be false
if secret_word != user_word:
    print(s)
    print("Not quite. Play again soon!")
        
else:
    print(s)
    print("Woo! You got it!") 