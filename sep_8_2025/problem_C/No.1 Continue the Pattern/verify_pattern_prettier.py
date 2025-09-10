# Define the ANSI escape codes for colors and formatting
# This allows for a more readable and visually appealing output in the terminal.
RESET = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_CYAN = '\033[96m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_MAGENTA = '\033[95m'

# The given series of numbers to analyze
series = [7, 26, 63, 124, 215]

# Print a formatted title for the program's output
print(f"{BOLD}{BRIGHT_BLUE}--- Analyzing the Series Pattern ---{RESET}\n")

# Verify the pattern n³ - 1 for each number in the series
print(f"{BRIGHT_YELLOW}Verifying the pattern {UNDERLINE}$n^3 - 1${RESET}{BRIGHT_YELLOW}:{RESET}")
for i, num in enumerate(series, start=2):
    calculated_num = i**3 - 1
    # Check if the calculated number matches the number in the series
    match = calculated_num == num
    
    # Use f-strings to include the variables and the color codes
    # The green color is used for numbers and the boolean result to highlight success
    print(f"  For n={i}: {i}³ - 1 = {BRIGHT_GREEN}{calculated_num}{RESET}. Match: {BRIGHT_GREEN}{match}{RESET}")

# Print a new, formatted header for the next part of the calculation
print(f"\n{BOLD}{BRIGHT_CYAN}--- Calculating the Next Number ---{RESET}")

# Determine the value of n for the next number in the series
next_n = len(series) + 2

# Calculate the next number based on the pattern
next_number = next_n**3 - 1

# Print the final result, highlighting the answer in a different color
print(f"  The next number in the series is for n={next_n}.")
print(f"  Calculation: {BOLD}7³ - 1{RESET} = {BRIGHT_MAGENTA}{next_number}{RESET}")
