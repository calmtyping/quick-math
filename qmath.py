import argparse
from random import randint
from time import perf_counter
import sys


def operation_normalizer(inputOperation: str) -> str:

    inputOperation = inputOperation.lower()

    if inputOperation in ("*", "x", "multi", "times", "multiply", "multiplication"):
        operation = "*"
    elif inputOperation in ("-", "sub", "subtract"):
        operation = "-"
    elif inputOperation in ("+", "add", "addition"):
        operation = "+"
    elif inputOperation in ("/", "÷", "div", "division", "divide"):
        operation = "/"
    else:
        raise argparse.ArgumentTypeError(
            f"Unknown operation: {inputOperation}. Use one of: +, -, *, / (or x, add, sub, div...)."
        )

    return operation


def create_operand(digits):

    if digits <= 0:
        raise ValueError("digits must be a positive integer")

    if digits == 1:
        return randint(0, 9)

    minRange = 1
    maxRange = 9

    for i in range(0, digits - 1):
        minRange = minRange * 10
        maxRange = maxRange * 10 + 9

    return randint(minRange, maxRange)


def create_math_problem(digits, operation):
    top_operand = create_operand(digits)
    bottom_operand = create_operand(digits)

    return top_operand, bottom_operand, operation, digits


def print_math_problem(math_problem):
    top_operand, bottom_operand, operation, digits = math_problem

    width = 3 + digits
    problem_underline = "-"

    print(f"{top_operand:>{width}}")
    print(f" {operation}{bottom_operand:>{width-2}}")
    print(f" {problem_underline * (width-1)}")


def create_start_timestamp():
    start_time = round(perf_counter(), 2)
    return start_time


def check_timeleft(start_time, test_timelimit):
    current_time = round(perf_counter(), 2)
    time_elapsed = current_time - start_time
    timeleft = test_timelimit - time_elapsed
    return timeleft


def check_answer_correctness(user_answer, math_problem):
    top_operand, bottom_operand, operation, _digits = math_problem

    assert operation in {"+", "-", "*", "/"}, \
        f"Unexpected operation: {operation}. Check operation_normalizer"

    if operation == "+":
        correct = top_operand + bottom_operand
    elif operation == "-":
        correct = top_operand - bottom_operand
    elif operation == "*":
        correct = top_operand * bottom_operand

    if user_answer == correct:
        return "Correct"
    else:
        return "Incorrect"


def user_answer_validator(user_answer):
    user_answer = user_answer.strip().lower()

    try:
        return int(user_answer)
    except ValueError:
        print("Answers can only be an integer! (Type 'q' or 'quit' to end test.)")
        return "INVALID"

def quit_if_user_wants_to(user_input):
    user_input = user_input.strip().lower()
    if user_input in ("q", "quit"):
        print("Goodbye!")
        sys.exit(0)

def run_math_test(operation, test_timelimit, digits):
    start_time = create_start_timestamp()
    timeleft = check_timeleft(start_time, test_timelimit)

    while timeleft > 0:
        math_problem = create_math_problem(digits, operation)
        print_math_problem(math_problem)
        user_input = input()

        quit_if_user_wants_to(user_input)

        user_answer = user_answer_validator(user_input)

        while user_answer == "INVALID":
            user_input = input()

            quit_if_user_wants_to(user_input)

            user_answer = user_answer_validator(user_input)
            timeleft = check_timeleft(start_time, test_timelimit)
            if timeleft <= 0:
                print("Sorry, times up! That still wasn't an integer!")
                return
        timeleft = check_timeleft(start_time, test_timelimit)
        correctness = check_answer_correctness(user_answer, math_problem)
        if timeleft <= 0:
            print("Sorry but time is up!")
            print(f"Your answer was {correctness} though!")
            return
        else:
            print(correctness)

    print("times up!")


def main():

    parser = argparse.ArgumentParser(description="Generate a quick math speed test")

    parser.add_argument(
        "operation",
        type=operation_normalizer,
        help="Math operation type. Examples: *, /, +, -",
    )

    parser.add_argument(
        "time", type=int, help="Amount of time the math test should last"
    )

    parser.add_argument(
        "digits", type=int, help="Amount of digits generated math problems should have"
    )

    args = parser.parse_args()

    operation = args.operation
    test_timelimit = args.time
    digits = args.digits

    run_math_test(operation, test_timelimit, digits)


if __name__ == "__main__":
    main()
