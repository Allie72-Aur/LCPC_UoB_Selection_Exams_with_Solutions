#include <stdio.h>

/**
 * @brief Calculates the product Z based on a list of four X values.
 *
 * The product is defined as:
 * Z = product(3 * 2^(i-1) * X_i) for i=1 to 4
 *
 * @param X An array of four double values.
 * @return The result of the product.
 */
double calculate_Z(double X[4]) {
    double total_product = 1.0;
    for (int i = 0; i < 4; ++i) {
        // The problem uses 1-based indexing for 'i',
        // we don't care for such non-sense, we're computer geeks..
        // we use 0-based indexing.
        double term_factor = 3.0;
        double power_of_2 = 1.0;
        for (int j = 0; j < i; ++j) {
            power_of_2 *= 2.0;
        }

        double term = term_factor * power_of_2 * X[i];
        total_product *= term;
    }
    return total_product;
}

int main() {
    double X[4];
    printf("Enter the four values for X (separated by spaces):\n");
    for (int i = 0; i < 4; ++i) {
        printf("X%d: ", i + 1);
        if (scanf("%lf", &X[i]) != 1) {
            printf("Invalid input. Please enter a numeric value.\n");
            // Clear the input buffer to prevent infinite loop on invalid input
            while(getchar() != '\n');
            i--; // Decrement i to re-prompt for the same value
        }
    }

    double result = calculate_Z(X);
    printf("The result of the product Z is: %.20f\n", result);

    return 0;
}
