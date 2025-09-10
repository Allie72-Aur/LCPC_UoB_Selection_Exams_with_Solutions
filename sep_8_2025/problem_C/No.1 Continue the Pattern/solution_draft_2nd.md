# Continue the Pattern

* **What is the next number in the series?**  
  7, 26, 63, 124, 215, ...?

1. 342
2. 343
3. 344
4. 345

## 2nd Attempt

After some amount of contemplation; you might notice something curious. to check if it's true, we can use the python script in the current folder: `./verify_pattern.py`.

Based on the analysis, the pattern is not based on the sum of digits, but rather on a cubic sequence. The pattern for the series is $n^3 −1$, starting with n=2.

The numbers in the series are:

$$2^3−1=8−1=7$$

$$3^3−1=27−1=26$$

$$4^3−1=64−1=63$$

$$5^3−1=125−1=124$$

$$6^3−1=216−1=215$$

Following this pattern, the next number would correspond to n=7:

$$7^3−1=343−1=342$$

This confirms that the next number in the series is 342, which corresponds to the first option.
