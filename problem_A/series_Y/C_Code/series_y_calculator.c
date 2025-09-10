#include <stdio.h>
#include <stdlib.h>

/**
 * @brief Calculates the factorial of a non-negative integer.
 *
 * This function uses a recursive approach to compute the factorial.
 *
 * @param n The non-negative integer.
 * @return The factorial of n, or -1 if the input is negative.
 */
long long int factorial(int n) {
    if (n < 0) {
        return -1; // Error code for negative input
    }
    if (n == 0 || n == 1) {
        return 1;
    } else {
        return (long long int)n * factorial(n - 1);
    }
}

/**
 * @brief Calculates the power of a base to a non-negative integer exponent.
 *
 * This function computes base^exp using a loop.
 *
 * @param base The base number.
 * @param exp The non-negative integer exponent.
 * @return The result of base^exp, or -1 if the exponent is negative.
 */
long long int power(int base, int exp) {
    if (exp < 0) {
        return -1; // Error code for negative exponent
    }
    long long int result = 1;
    for (int i = 0; i < exp; ++i) {
        result *= base;
    }
    return result;
}

/**
 * @brief Calculates the series Y.
 *
 * The series is defined as:
 * Y = sum(X[j] / (2^j)!) for j=0 to n-1
 *
 * @param X The array of double values.
 * @param n The number of elements in the array.
 * @return The result of the series.
 */
double calculate_Y(double* X, int n) {
    double total_sum = 0.0;
    for (int j = 0; j < n; ++j) {
        long long int denominator = factorial(power(2, j));
        if (denominator == 0) {
            // Avoid division by zero, although this should not occur with this logic.
            continue;
        }
        total_sum += X[j] / (double)denominator;
    }
    return total_sum;
}

int main() {
    int n;
    printf("Enter the number of elements in the list X: ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Invalid input. Please enter a positive integer.\n");
        return 1;
    }

    // Dynamically allocate memory for the array
    double* X = (double*)malloc(n * sizeof(double));
    if (X == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    printf("Enter the elements of the list:\n");
    for (int i = 0; i < n; ++i) {
        printf("Enter element %d: ", i + 1);
        if (scanf("%lf", &X[i]) != 1) {
            printf("Invalid input. Please enter a numeric value.\n");
            free(X); // Free allocated memory before exiting
            return 1;
        }
    }

    double result = calculate_Y(X, n);
    printf("The result of the series Y is: %.10f\n", result);

    // Free the dynamically allocated memory
    free(X);

    return 0;
}
