series = [7, 26, 63, 124, 215]

print("Verifying the pattern $n^3 - 1$:")
for i, num in enumerate(series, start=2):
    calculated_num = i**3 - 1
    print(f"For n={i}: {i}^3 - 1 = {calculated_num}. Matches series number: {num == calculated_num}")

next_n = len(series) + 2
next_number = next_n**3 - 1

print(f"\nThe next number in the series is for n={next_n}.")
print(f"Calculation: {next_n}^3 - 1 = {next_number}")