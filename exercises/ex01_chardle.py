"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730557183"

count_index = 0

user_word: str = input("Enter a 5-character word: ")
if len(user_word) != 5:
    print("Error: Word must contain 5 characters")
    quit()
user_character: str = input("Enter a single character: ")

if len(user_character) != 1:
    print("Error: Character must be a single character.")
    quit()

print("Searching for " + user_character + " in " + user_word)
     
if user_character == user_word[0]:
    print(user_character + " found at index 0")
    count_index += 1
if user_character == user_word[1]:
    print(user_character + " found at index 1")
    count_index += 1
if user_character == user_word[2]:
    print(user_character + " found at index 2")
    count_index += 1
if user_character == user_word[3]:
    print(user_character + " found at index 3")
    count_index += 1
if user_character == user_word[4]:
    print(user_character + " found at index 4")
    count_index += 1

if count_index > 0:
    if count_index == 1:
        print(str(count_index) + " instance of " + user_character + " found in " + user_word)
    else:
        print(str(count_index) + " instances of " + user_character + " found in " + user_word)
else:
    print("No instances of " + user_character + " found in " + user_word)