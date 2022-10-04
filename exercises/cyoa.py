"""This is like an escape room with a practice version and actual version for people to try."""

__author__ = "730557183"
 
from random import randint 
points: int = 0
round_points: int = 0
player: str = ""
game_enter: str = ""
choice: str = ""
name: str = ""
answer: str = ""


COWBOY_HAT: str = "\U0001F920"
THE_PEN: str = "\U0001F58A"
MUSCLE_ARM: str = "\U0001F4AA"
RED_WARNING: str = "\U0001F6AB"
THE_SWORD: str = "\U0001F5E1"
THE_DETECTIVE: str = "\U0001F575"
MAGNIFY_GLASS: str = "\U0001F50E"
THE_BRIEFCASE: str = "\U0001F4BC"


def main() -> None:
    """This is the main function that allows the user to choose their path and determine where they want to go."""
    greet()
    game_loop: bool = True
    while game_loop:
        game_enter = input("If you'd like to enter the game arena type 'Play', otherwise type anything else: ")
        if game_enter == "Play":
            print("You now have three choices: To play the Practice gameroom type 'Practice', To play the Real gameroom type 'Real', If you would like to Leave the game type 'Leave'.")
            choice = input("Please type your choice without quotations here: ")
            if choice == "Practice":
                global round_points
                round_points == 0
                print("Game rules: \n1. Each round you will have 5 chances for whatever task lays ahead.\n2. Each turn used will deduct 2 points from the max 10 points you can gain from a round\n3. You need 22 points to escape the room and win the game!")
                practice_game()
                practice_game_2()
                practice_game_3()
                print(f"You had {round_points} this round and needed 22 to win.")
                if round_points >= 22:
                    print("YOU ESCAPED!")
                else:
                    print("Sorry, better luck next time you were eliminated by the room.")
            elif choice == "Real":
                global points
                points = 0
                print("Game rules: \n1. Each round you will have 5 chances for whatever task lays ahead.\n2. Each turn used will deduct 2 points from the max 10 points you can gain from a round\n3. You need 22 points to escape the room and win the game!")
                real_game(12)
                real_game_2(12)
                real_game_3(12)
                print(f"You had {points} this round and needed 22 to win.")
                if points >= 22:
                    print("YOU ESCAPED!")
                else:
                    print("Sorry, better luck next time you were eliminated by the room.")
            elif choice == 'Leave':
                print(points)
                return leave()
            else:
                print("Please try again, that didn't match the optional choices.")
        else:
            print(f"Your number of points that final game: {points}")
            print(points)
    
        
def greet() -> None:
    """Allows the user to set their name that will be used throughout the game."""
    global player
    name = input("Welcome to this escape room! Please enter your name here: ")
    player = name
    print(f"Welcome to the escape room {name}!")


def practice_game() -> None:
    """The first round of the practice game."""
    global player
    print("This is a practice round that will guide you through the process of an escape room.\nWelcome to Round 1!")
    print("In this round you will be given a riddle with 5 tries to guess the correct answer. ")
    print("Here is the riddle: First think of a person who lives in disguise, who deals in secrets and tells naught but lies. Next tell me what’s the last to mend, the middle of middle and the end of end. Finally give me the sound often heard during the search for a hard to find word. Now string them together and answer me this, which creature are you unwilling to kiss?")
    print("Here's a hint: Think through this problem step at a time and connect the dots, or should I say silk.")
    turn: int = 0
    points_tracker: int = 12
    correct: bool = False
    while turn < 5 and not correct:
        turn += 1
        print(f"This is turn {turn}")
        answer = input("Enter your answer: ")
        if answer == "Spider" or "spider":
            global round_points
            global points
            points_value: int = points_tracker - turn * 2 
            print(f"Correct!!! You answered this on turn number {turn}")
            print(f"You would have received {points_value} points in the real version!")
            round_points += points_value
            points += points_value
            correct = True
        else:
            print("Sorry that is not correct, please try again.")
    if turn == 5:
        print("Sorry, you used up all your turns and gained zero points from this, you need to do better on the next two to escape!")
    print(f"Practice number of total points: {points}")
    print(f"You are now done with the first task, keep up the good work {player}!")


def practice_game_2() -> None:
    """The second round of the practice game."""
    global player
    print("Welcome to Round 2!\nIn this round you will be given two numbers and must figure out the three order of operations used to go from one number to the other.")
    print("Hint: PEMDAS doesn't always apply just to algebra in escape rooms.")
    correct: bool = False
    points_tracker: int = 12
    turn: int = 0
    start_number: int = randint(1, 10)
    target_number: int = start_number ** 2 // randint(1, 10) + 7
    print(f"The starting number is {start_number} and the target number is {target_number}. Random constants have been used.")
    while turn < 5 and not correct:
        turn += 1
        correct_answer: str = "**, //, +"
        print(f"This is turn {turn}")
        answer = input("Enter your answer: ")
        if answer == correct_answer:
            global round_points
            global points
            points_value: int = points_tracker - turn * 2 
            print(f"Correct!!! You answered this on turn number {turn}")
            print(f"You would have received {points_value} points in the real version!")
            round_points += points_value
            points += points_value
            correct = True
        else:
            print("Sorry that is not correct, please try again.")
    if turn == 5:
        print("Sorry, you used up all your turns and gained zero points from this, you need to do better on the next one to escape!")
    print(f"Practice number of total points: {points}")
    print(f"You are now done with the second task, keep up the good work {player}!")


def practice_game_3() -> None:
    """The third round of the practice game."""
    global player
    print("Welcome to Round 3 and the final round!\nIn this round you will be given a list of emojis that you must decipher into a sentence that is similar to popular statements..")
    print("Hint: Medieval soldiers would argue the opposite of this saying.")
    print(f"Here are the emojis that you will decipher: {THE_PEN} {MUSCLE_ARM} + {RED_WARNING} {THE_SWORD}, make sure to only capitalize the first word!")
    correct: bool = False
    points_tracker: int = 12
    turn: int = 0
    while turn < 5 and not correct:
        turn += 1
        print(f"This is turn {turn}")
        answer = input("Enter your answer: ")
        correct_answer: str = "It's elementary"
        if answer == correct_answer:
            global points
            global round_points
            points_value: int = points_tracker - turn * 2 
            print(f"Correct!!! You answered this on turn number {turn}")
            print(f"You would have received {points_value} points in the real version!")
            points += points_value
            round_points += points_value
            correct = True
        else:
            print("Sorry that is not correct, please try again.")
    if turn == 5:
        print("Sorry, you used up all your turns and gained zero points from this, you need to do better on the next one to escape!")
    print(f"Practice number of total points: {points}")
    print(f"Your overall number of points is {points}")
    print(f"You are now finished with all three tasks! Let's see how you stack up {player}!")
    print("Let's see if you were able to gain enough points to escape!")


def real_game(points_tracker: int) -> int:
    """The first round of the real game."""
    global player
    print("Welcome to Round 1!\nIn this round you will be given a riddle with 5 tries to guess the correct answer.")
    print("Here is the riddle: As I was going to St Ives, Upon the road I met seven wives; Every wife had seven sacks, Every sack had seven cats, Every cat had seven kits: Kits, cats, sacks, and wives, How many were going to St Ives?")
    turn: int = 0
    correct: bool = False
    while turn < 5 and not correct:
        turn += 1
        print(f"This is turn {turn}")
        answer = input("Enter your answer: ")
        if answer == "One" or "1":
            global points
            points_value: int = points_tracker - turn * 2 
            print(f"Correct!!! You answered this on turn number {turn}")
            print(f"You have received {points_value} points!")
            points += points_value
            correct = True
        else:
            print("Sorry that is not correct, please try again.")
    if turn == 5:
        print("Sorry, you used up all your turns and gained zero points from this, you need to do better on the next two to escape!")
        return points
    print(f"Number of total points: {points}")
    print(f"You are now done with the first task, keep up the good work {player}!")
    return points


def real_game_2(points_tracker: int) -> int:
    """The second round of the real game."""
    global player
    print("Welcome to Round 2!\nIn this round you will be given two numbers and must figure out the five order of operations used to go from one number to the other.")
    correct: bool = False
    turn: int = 0
    start_number: int = randint(1, 10)
    target_number: int = start_number ** 2 // randint(1, 10) % 7 + 5 - 3 
    print(f"The starting number is {start_number} and the target number is {target_number}. Random constants have been used.")
    while turn < 5 and not correct:
        turn += 1
        correct_answer = "**, //, %, +, -"
        print(f"This is turn {turn}")
        answer: str = input("Enter your answer: ")
        if answer == correct_answer:
            global points
            points_value: int = points_tracker - turn * 2 
            print(f"Correct!!! You answered this on turn number {turn}")
            print(f"You have received {points_value} points!")
            points += points_value
            correct = True
        else:
            print("Sorry that is not correct, please try again.")
    if turn == 5:
        print("Sorry, you used up all your turns and gained zero points from this, you need to do better on the next one to escape!")
    print(f"Number of total points: {points}")
    print(f"You are now done with the second task, keep up the good work {player}!")
    return points


def real_game_3(points_tracker: int) -> int:
    """The third round of the real game."""
    global player
    print("Welcome to Round 3 and the final round!\nIn this round you will be given a list of emojis that you must decipher into a sentence that is similar to popular statements..")
    print(f"Here are the emojis that you will decipher: {THE_DETECTIVE} {MAGNIFY_GLASS} {THE_BRIEFCASE}, make sure to only capitalize the first word!")
    correct: bool = False
    turn: int = 0
    while turn < 5 and not correct:
        turn += 1
        print(f"This is turn {turn}")
        answer = input("Enter your answer: ")
        correct_answer: str = "The pen is mightier than the sword"
        if answer == correct_answer:
            global points
            points_value: int = points_tracker - turn * 2 
            print(f"Correct!!! You answered this on turn number {turn}")
            print(f"You would have received {points_value} points in the real version!")
            points += points_value
            correct = True
        else:
            print("Sorry that is not correct, please try again.")
    if turn == 5:
        print("Sorry, you used up all your turns and gained zero points from this, you need to do better on the next one to escape!")
    print(f"Number of total points: {points}")
    print(f"Your overall number of points is {points}")
    print(f"You are now finished with all three tasks! Let's see how you stack up {player}!")
    print("Let's see if you were able to gain enough points to escape!")
    return points


def leave() -> None:
    """Allows you to leave the program."""
    print(f"Thanks for playing, come back soon! {COWBOY_HAT}")
    print(points)


if __name__ == "__main__":
    main()