# Longest Common Subsequence (LCS) Finder

This Python module provides a function to find the longest common subsequence (LCS) of two given strings. The function returns both the length of the LCS and the LCS itself. Additionally, it includes a visualization of the dynamic programming (DP) matrix used to compute the LCS.

## Function

### `longestCommonSubsequence(text1: str, text2: str) -> Tuple[int, str]`

**Parameters:**

- `text1` (str): The first input string.
- `text2` (str): The second input string.

**Returns:**

- A tuple containing:
  - The length of the longest common subsequence.
  - The longest common subsequence as a string.

**Description:**

This function uses dynamic programming to calculate the longest common subsequence between two strings. It constructs a 2D matrix to store lengths of longest common subsequences of substrings and then constructs the LCS from this matrix.

## Visualization

The dynamic programming matrix is used to compute the longest common subsequence. Visualizing this matrix helps in understanding the LCS computation process.

### Matrix Visualization

- **Diagonal Moves:** When characters from both strings match, the value in the matrix is incremented by 1 from the diagonal cell (i.e., `dp[i+1][j+1]`).
- **Max Value Moves:** When characters do not match, the cell value is the maximum of the cell to the right or the cell below (i.e., `max(dp[i][j+1], dp[i+1][j])`).

### Example Visualization

Here’s an example of how the matrix looks for `text1 = "ABCBDAB"` and `text2 = "BECAB"`:

```plaintext
      B  E  C  A  B
    0  0  0  0  0
  A 0  0  0  0  1
  B 0  1  1  1  2
  C 0  1  1  2  2
  B 0  1  2  2  3
  D 0  1  2  2  3
  A 0  1  2  3  3
  B 0  1  2  3  4
```
 In this matrix:

- **Diagonal Moves:** Diagonal cells with increasing values represent matches. When `text1[i]` matches `text2[j]`, the value in the matrix at `dp[i][j]` is incremented by 1 from the value at `dp[i+1][j+1]`. This indicates that the current characters contribute to the longest common subsequence.

- **Max Value Moves:** Cells with the maximum values indicate the chosen path when characters do not match. When `text1[i]` does not match `text2[j]`, the value in the matrix at `dp[i][j]` is the maximum of the value to the right (`dp[i][j+1]`) or the value below (`dp[i+1][j]`). This reflects the decision to carry forward the length of the longest common subsequence found so far.

## Complexity

- **Time Complexity:** `O(m * n)`, where `m` and `n` are the lengths of the two input strings. This complexity arises due to the double loop used to fill the 2D matrix.

- **Space Complexity:** `O(m * n)`, for storing the 2D matrix used to compute the lengths of longest common subsequences.

## Test Cases

The following test cases are included to verify the functionality of the `longestCommonSubsequence` function:

- **Both Strings are Non-empty:**
  - `text1 = "ABCBDAB"`, `text2 = "BECAB"`
  - **Expected Output:** Length of LCS is 4 and its value is BCAB

- **One String is Empty:**
  - `text1 = "A"`, `text2 = ""`
  - **Expected Output:** Length of LCS is 0 and its value is ""

- **Both Strings are Empty:**
  - `text1 = ""`, `text2 = ""`
  - **Expected Output:** Length of LCS is 0 and its value is ""

- **Common Subsequence Exists:**
  - `text1 = "AGGTAB"`, `text2 = "GXTXAYB"`
  - **Expected Output:** Length of LCS is 4 and its value is GTAB

- **Strings with No Common Characters:**
  - `text1 = "ABC"`, `text2 = "CBA"`
  - **Expected Output:** Length of LCS is 1 and its value is C

## Notes

- The function handles edge cases such as empty strings gracefully.
- Ensure to test with various cases to cover different scenarios for robustness.
- Use the visualization to understand how the LCS matrix is constructed and how the values are derived.
