#!/usr/bin/env python3
import random


def generate_progression(length):
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    progression = []
    for i in range(length):
        progression.append(start + i * step)
    return progression

def hide_number(progression):
    hidden_index = random.randint(0, len(progression) - 1)
    hidden_number = progression[hidden_index]
    progression[hidden_index] = '..'
    return hidden_number


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")
    correct_answers = 0

    while correct_answers < 3:
        progression_length = random.randint(5, 10)
        progression = generate_progression(progression_length)
        hidden_number = hide_number(progression)

        print("Question: " + " ".join(map(str, progression)))
        answer = input("Your answer: ")

        if answer == str(hidden_number):
            print("Correct!")
            correct_answers += 1
        else:
            print("'" + answer + "' is wrong answer ;(. Correct answer was '" + str(hidden_number) + "'.")
            print("Let's try again, " + name + "!")
            return
    print(f"Congratulations, {name}!")

if __name__ == '__main__':
    main()
