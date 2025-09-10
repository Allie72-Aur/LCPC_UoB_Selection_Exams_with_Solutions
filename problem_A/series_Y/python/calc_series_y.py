from typing import List
import sys
# import math

# Program to calculate the series Y = sum(X[j] / (2^j)!)
# based on the provided list X
#
# Usage:
#   python Calc_Series_Y.py {[<number_of_elements> <element_1> <element_2> ... <element_n>] | [--util-mode | -u]}
#   
#   If no command line arguments are given, the user is prompted to input the values.
#
#   If --util-mode or -u is given, the textual prompts are not displayed, and the program runs once, the other arguments are ignored
#   and the values are taken from standard input, one per line, first the number of elements, then the elements.
#   
#   If <number_of_elements> and the elements are given, they are used directly unless utility mode flag is provided
#
# Example:
#   python Calc_Series_Y.py 3 1.0 2.0 3.0
#   This will calculate Y for X = [1.0, 2.0, 3.0]
#
# Example with utility mode:
#   echo -e "3\n1.0\n2.0\n3.0" | python Calc_Series_Y.py --util-mode
#   This will also calculate Y for X = [1.0, 2.0, 3.0] without any prompts


# the custom factorial function is included for completeness, in a real-world scenario, math.factorial
# is standard and should be used instead for efficiency and reliability
def factorial(n: int) -> int:
    """Calculates the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# the custom power function is included for completeness, in a real-world scenario, the ** operator
# or math.pow should be used instead, there's probably no advantage to using your own custom implementation
# of the power function ever
def power(base: int, exp: int) -> int:
    """Calculates the power of a base to an exponent."""
    if exp < 0:
        raise ValueError("This function only supports non-negative exponents.")
    result = 1
    # loop to iterate 'exp' number of times
    for _ in range(exp):
        result *= base
    return result


def Calculate_Y(X_list: List[float]) -> float:
    """
    Calculates the series Y = sum(X_i / (2^i)!), where i starts at 1.
    The list X_list is 0-indexed, so we use j+1 to match the formula.
    """
    total_sum = 0.0
    for j in range(len(X_list)):
        # The j-th element corresponds to the i=(j+1) term in the formula
        numerator = X_list[j]
        denominator_exponent = j + 1
        denominator = factorial(power(2, denominator_exponent))
        term = numerator / denominator
        total_sum += term
    return total_sum


def run_command_line(args: List[str]):
    """Handles the command-line argument mode."""
    try:
        n = int(args[0])
        if n <= 0:
            raise ValueError("Number of elements must be a positive integer.")
        if len(args) != n + 1:
            raise ValueError(f"Expected {n} elements, but got {len(args) - 1}.")
        X = [float(arg) for arg in args[1 : n + 1]]
        result = Calculate_Y(X)
        print(result)
        sys.exit(0)
    except ValueError as ve:
        print(f"Input error: {ve}", file=sys.stderr)
        sys.exit(1)


def run_interactive_or_util(util_mode: bool):
    """Handles the interactive and utility modes."""
    try:
        while True:
            try:
                prompt = "" if util_mode else "Enter the number of elements in the list X: "
                n_str = input(prompt)
                if not n_str:
                    continue
                n = int(n_str)
                if n <= 0:
                    print("Please enter a positive integer.", file=sys.stderr)
                    continue

                X = []
                for i in range(n):
                    value_prompt = "" if util_mode else f"Enter element {i + 1}: "
                    value = float(input(value_prompt))
                    X.append(value)
                
                result = Calculate_Y(X)
                output = f"{result}" if util_mode else f"The result of Y({X}) is: {result}"
                print(output)
                if util_mode:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.", file=sys.stderr)
                if util_mode:
                    break
    except EOFError:
        pass


if __name__ == "__main__":
    args = sys.argv[1:]
    util_mode = "--util-mode" in args or "-u" in args

    # Clean the arguments list for processing
    clean_args = [arg for arg in args if arg not in ("--util-mode", "-u")]

    if not util_mode and len(clean_args) > 0:
        run_command_line(clean_args)
    else:
        run_interactive_or_util(util_mode)
