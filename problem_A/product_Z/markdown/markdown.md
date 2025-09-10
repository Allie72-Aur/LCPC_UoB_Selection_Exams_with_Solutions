# Calculate Product Z

## Problem Description

The problem is to calculate the value of the series Z, which is a product of four terms:
$$Z = (3 \cdot X_1) \cdot (6 \cdot X_2) \cdot (12 \cdot X_3) \cdot (24 \cdot X_4)$$

This can be expressed using product notation as:
$$Z = \prod_{i=1}^{4} (3 \cdot 2^{i-1} \cdot X_i)$$

## Pseudocode

A concise solution is presented in the pseudocode below. The solution uses a loop to iterate through each term of the series, calculating the coefficient for each $X_i$ and multiplying it by the corresponding value.

<!-- Go is a good language for syntax highlighting pseudocode -->
```go
procedure Calculate_Z(X_list)
    product = 1
    for j from 1 through 4
        coefficient = 3 * pow(2, j-1)
        term = coefficient * X_list[j]
        product = product * term
    return product

function pow(base, exp)
    result = 1
    for j from 1 through exp
        result = result * base
    return result
```
