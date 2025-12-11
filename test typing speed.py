import time
import random

sentences = [
    "Python is an amazing programming language",
    "Practice makes you a better developer",
    "Typing speed is measured in words per minute",
    "Artificial intelligence is changing the world",
    "Simple projects help you learn faster"
]

def typing_test():
    print("\n--- Typing Speed Test ---")
    sentence = random.choice(sentences)
    print("\nType this sentence exactly:\n")
    print(sentence)
    print()

    input("Press Enter when you are ready...")
    print("\nStart typing below:\n")

    start_time = time.time()
    user_input = input()
    end_time = time.time()

    # Time calculation
    time_taken = end_time - start_time  # seconds
    time_in_minutes = time_taken / 60

    # WPM calculation
    words = len(user_input.split())
    wpm = words / time_in_minutes if time_in_minutes > 0 else 0

    # Accuracy calculation
    correct_chars = 0
    for i in range(min(len(sentence), len(user_input))):
        if sentence[i] == user_input[i]:
            correct_chars += 1

    accuracy = (correct_chars / len(sentence)) * 100

    # Results
    print("\n--- Results ---")
    print(f"Time Taken: {time_taken:.2f} seconds")
    print(f"Words Per Minute (WPM): {wpm:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")

typing_test()
