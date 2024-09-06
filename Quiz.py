import random

from Words import *

def TheQuiz():
    random.shuffle(words)
    score = 0

    for word in words:
        print(f"What is the English word of '{word['dutch']}'?")
        inputAnswer = input("Your answer: ".strip().lower())
        correctAnswer = word['english'].lower()

        if inputAnswer == "0".strip():
            print("Exiting App...")
            return
        if inputAnswer == correctAnswer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong answer! The correct answer is {correctAnswer}.\n")

    print(f"Quiz Complete! Your score: {str(score)}/{len(words)}.")


