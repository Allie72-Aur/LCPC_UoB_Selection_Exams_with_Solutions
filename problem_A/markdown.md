# Solutions to Problem A (Calculating Series)

## 1. Calculate Series A

### 1.1 Problem Description

The problem is to calculate the value of the series A:
$$A = \frac{X + 1}{2!} + \frac{X + 2}{4!} + \frac{X + 3}{8!} + \dots + \frac{X + 7}{128!}$$

This can be expressed using summation notation as:
$$A = \sum_{i=1}^{7} \frac{X + i}{(2^i)!}$$

### 1.2 Pseudocode

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

## 2. Calculate Series Y

### 2.1 Problem Description

The problem is to calculate the value of the series Y:
$$Y = \frac{X_1}{2!} + \frac{X_2}{4!} + \frac{X_3}{8!} + \dots + \frac{X_n}{(2^n)!}$$

This can be expressed using summation notation as:
$$Y = \sum_{i=1}^{n} \frac{X_i}{(2^i)!}$$

### 2.2 Pseudocode

A concise solution is presented in the pseudocode below. The solution uses a loop to iterate through each term of the series, calculating the factorial and power for the denominator of each term using helper functions.

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

## 3. Calculate Product Z

### 3.1 Problem Description

The problem is to calculate the value of the series Z, which is a product of four terms:
$$Z = (3 \cdot X_1) \cdot (6 \cdot X_2) \cdot (12 \cdot X_3) \cdot (24 \cdot X_4)$$

This can be expressed using product notation as:
$$Z = \prod_{i=1}^{4} (3 \cdot 2^{i-1} \cdot X_i)$$

### 3.2 Pseudocode

A concise solution is presented in the pseudocode below. The solution uses a loop to iterate through each term of the series, calculating the coefficient for each $X_i$ and multiplying it by the corresponding value.

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
