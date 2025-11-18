import argparse
from time import perf_counter
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




def main():

    parser = argparse.ArgumentParser(description="Generate a quick math speed test")

    parser.add_argument(
        "operation",
        type=operation_normalizer,
        help="Math operation type. Examples: *, /, +, -") 
    

    args = parser.parse_args()

    operation = (args.operation)

    top_operand, bottom_operand = generate_operands(digits)
    print_math_problem(operation, top_operand, bottom_operand)

if __name__ == "__main__":
    main()