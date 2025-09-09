def Calculate_A(X: float) -> float: 
    sum = 0
    for j in range(1, 7+1):
        term = (X + j) / factorial(power(2, j))
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
    while True:
        try: 
            X = float(input("Enter a value for X: "))
            result = Calculate_A(X)
            print(f"The result of A({X}) is: {result}")
        except ValueError:
            print("Invalid input. Please enter a numeric value for X.")
        