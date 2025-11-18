import argparse
from time import perf_counter
import time
import random


digits = 2 

def operation_normalizer(inputOperation: str) -> str:

    inputOperation = inputOperation.lower()

    if inputOperation in ("*","x","multi","times","multiply", "multiplication"):
        operation = "*"
    elif inputOperation in ("-", "sub","subtract"):
        operation = "-"
    elif inputOperation in ("+", "add", "addition"):
        operation = "+"
    elif inputOperation in ("/","÷","div", "division", "divide"):
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
        return random.randint(0,9)

    minRange = 1
    maxRange = 9

    for i in range(0, digits - 1):
        minRange = minRange * 10
        maxRange = maxRange * 10 + 9
            
    return random.randint(minRange,maxRange)


def generate_operands(digits):
        top_operand = create_operand(digits)
        bottom_operand = create_operand(digits)

        return top_operand, bottom_operand


problem_underline = "-"
width = 3 + digits
def print_math_problem(operation, top_operand, bottom_operand):
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

def main():

    parser = argparse.ArgumentParser(description="Generate a quick math speed test")

    parser.add_argument(
        "operation",
        type=operation_normalizer,
        help="Math operation type. Examples: *, /, +, -")
    
    parser.add_argument(
        "time",
        type=int,
        help="Amount of time the math test should last")
    

    args = parser.parse_args()

    operation = (args.operation)
    test_timelimit = (args.time)


    top_operand, bottom_operand = generate_operands(digits)
    print_math_problem(operation, top_operand, bottom_operand)


    start_time = create_start_timestamp()
    print(start_time)
    timeleft = check_timeleft(start_time, test_timelimit)

    while(timeleft > 0):
        timeleft = check_timeleft(start_time, test_timelimit)
        print(timeleft)
        time.sleep(5)

if __name__ == "__main__":
    main()