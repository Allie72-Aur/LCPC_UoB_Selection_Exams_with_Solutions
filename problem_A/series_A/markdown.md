# Calculate Series A

## Problem Description

The problem is to calculate the value of the series A:
$$A = \frac{X + 1}{2!} + \frac{X + 2}{4!} + \frac{X + 3}{8!} + \dots + \frac{X + 7}{128!}$$

This can be expressed using summation notation as:
$$A = \sum_{i=1}^{7} \frac{X + i}{(2^i)!}$$

## Pseudocode

A concise solution is presented in the pseudocode below, The solution uses a loop to iterate through each term of the series, calculating the factorial and power for the denominator of each term using helper functions.  

<!-- Go is a good language for syntax highlighting pseudocode -->
```go
procedure Calculate_A(X)
    sum = 0
    for j from 1 through 7
        term = (X + j) / factorial(pow(2, j))
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
