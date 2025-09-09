# Calculate Series Y

## Problem Description

The problem is to calculate the value of the series Y:
$$Y = \frac{X_1}{2!} + \frac{X_2}{4!} + \frac{X_3}{8!} + \dots + \frac{X_n}{(2^n)!}$$

This can be expressed using summation notation as:
$$Y = \sum_{i=1}^{n} \frac{X_i}{(2^i)!}$$

## Pseudocode

A concise solution is presented in the pseudocode below. The solution uses a loop to iterate through each term of the series, calculating the factorial and power for the denominator of each term using helper functions.

<!-- Go is a good language for syntax highlighting pseudocode -->
```go
procedure Calculate_Y(X_list, n)
    sum = 0
    for j from 1 through n
        term = X_list[j] / factorial(pow(2, j))
        sum = sum + term
    return sum

function factorial(n)
    if n is 0 or 1
        return 1
    else
        return n * factorial(n - 1)

function pow(base, exp)
    product = 1
    for j from 1 through exp
        product = product * base
    return product
```
