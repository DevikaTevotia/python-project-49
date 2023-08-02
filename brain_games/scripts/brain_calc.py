#!/usr/bin/env python3
import random


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('What is the result of the expression?')
    correct_answers = 0
    while correct_answers < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        number3 = random.randint(0, 2)
        if number3 == 0:
            correct_answer = number1 + number2
            question_string = (f"{number1} + {number2}")
        elif number3 == 1:
            correct_answer = number1 - number2
            question_string = (f"{number1} - {number2}")
        else:
            correct_answer = number1 * number2
            question_string = (f"{number1} * {number2}")
        print(f"Question: {question_string}")
        user_answer = input("Your answer: ").lower()
        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(.")
            print(f"Correct answer is '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        correct_answers += 1

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
