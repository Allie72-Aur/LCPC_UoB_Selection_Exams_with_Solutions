#include <stdio.h>

/**
 * @brief Calculates the factorial of a non-negative integer.
 *
 * This function uses a recursive approach to compute the factorial.
 *
 * @param n The non-negative integer.
 * @return The factorial of n.
 */
long long int factorial(int n) {
    if (n < 0) {
        // Factorial is not defined for negative numbers.
        return -1; // Or handle error appropriately
    }
    if (n == 0 || n == 1) {
        return 1;
    } else {
        return (long long int)n * factorial(n - 1);
    }
}

/**
 * @brief Calculates the power of a base to an integer exponent.
 *
 * This function computes base^exp using a loop.
 *
 * @param base The base number.
 * @param exp The integer exponent.
 * @return The result of base^exp.
 */
long long int power(int base, int exp) {
    if (exp < 0) {
        // Power is not handled for negative exponents.
        return -1;
    }
    long long int result = 1;
    for (int i = 0; i < exp; ++i) {
        result *= base;
    }
    return result;
}

/**
 * @brief Calculates the series A.
 *
 * The series is defined as:
 * A(X) = sum((X + j) / (2^j)!) for j=1 to 7
 *
 * @param X The value for X.
 * @return The result of the series.
 */
double calculate_A(double X) {
    double total_sum = 0.0;
    for (int j = 1; j <= 7; ++j) {
        double term_numerator = X + j;
        double term_denominator = (double)factorial(power(2, j));
        if (term_denominator == 0) {
            // Avoid division by zero, although this should not happen with the logic.
            continue;
        }
        total_sum += term_numerator / term_denominator;
    }
    return total_sum;
}

int main() {
    double X;
    printf("Enter a value for X: ");
    if (scanf("%lf", &X) != 1) {
        printf("Invalid input. Please enter a numeric value.\n");
        return 1;
    }

    double result = calculate_A(X);
    printf("The result of A(%.2f) is: %.10f\n", X, result);

    return 0;
}
