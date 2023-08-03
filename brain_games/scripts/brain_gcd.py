#!/usr/bin/env python3
import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Find the greatest common divisor of given numbers.')
    correct_answers = 0
    while correct_answers < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        print(f"Question: {number1} {number2}")
        user_answer = input("Your answer: ").lower()
        correct_answer = gcd(number1, number2)
        if user_answer == str(correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(.")
            print(f"Correct answer is '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
