#!/usr/bin/env python3
import random

def is_even(number):
    return number % 2 == 0

def play_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print("Hello, " + name + "!")

    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 20)
        print("Question:", number)
        answer = input("Your answer: ")

        if (is_even(number) and answer.lower() == "yes") or (not is_even(number) and answer.lower() == "no"):
            print("Correct!")
            correct_answers += 1
        else:
            correct_answer = "no" if is_even(number) else "yes"
            print("'" + answer + "' is wrong answer ;(. Correct answer was '" + correct_answer + "'.")
            print("Let's try again, " + name + "!")
            return

    print("Congratulations, " + name + "!")


play_game()
