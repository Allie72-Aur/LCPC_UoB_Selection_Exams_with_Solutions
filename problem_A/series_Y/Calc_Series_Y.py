from typing import List

# Function to calculate the series Y = sum(X[j] / (2^j)!)
# based on the provided list X
#
# Usage:
#   python Calc_Series_Y.py {[<number_of_elements> [<element_1> <element_2> ... <element_n>]] | [--util-mode | -u]}
#   If no command line arguments are given, the user is prompted to input the values
#   If --util-mode or -u is given, the textual prompts are not displayed, and the program runs once, the other arguments are ignored
#   and the values are taken from standard input, one per line, first the number of elements, then the elements
#   If <number_of_elements> and the elements are given, they are used directly unless utility mode flag is provided
#
# Example:
#   python Calc_Series_Y.py 3 1.0 2.0 3.0
#   This will calculate Y for X = [1.0, 2.0, 3.0]
#
# Example with utility mode:
#   echo -e "3\n1.0\n2.0\n3.0" | python Calc_Series_Y.py --util-mode
#   This will also calculate Y for X = [1.0, 2.0, 3.0] without any prompts


def Calculate_Y(X_list: List[float]) -> float:
    sum = 0
    for j in range(0, len(X_list)):
        term = X_list[j] / factorial(power(2, j))
        sum += term
    return sum


def factorial(n: int) -> int:
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


def power(base: int, exp: int) -> int:
    product = 1
    for j in range(1, exp):
        product = product * base
    return product


if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    util_mode = "--util-mode" in args or "-u" in args
    if not util_mode:
        args = [arg for arg in args if arg not in ("--util-mode", "-u")]
        if len(args) > 0:
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
                print(f"Input error: {ve}")

    while True:
        # Get the number of elements in the list from the user,
        # re-prompt if invalid input is given
        n = 0
        while True:
            prompt = "" if util_mode else "Enter the number of elements in the list X: "
            n = int(input(prompt))
            if n > 0:
                break
            else:
                print("Please enter a positive integer.")

        # Get the elements of the list from the user
        X = []
        for i in range(n):
            # Re-prompt if invalid input is given
            value = 0.0
            while True:
                try:
                    prompt = "" if util_mode else f"Enter element {i + 1}: "
                    value = float(input(prompt))
                    X.append(value)
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")

        result = Calculate_Y(X)
        output = result if util_mode else f"The result of Y({[val for val in X]}) \nis: {result}"
        print(output)
        if util_mode:
            break
