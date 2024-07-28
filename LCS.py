def longestCommonSubsequence(text1: str, text2: str):
    dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
    for i in range(len(text1)-1, -1, -1):
        for j in range(len(text2)-1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j+ 1] 
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i+1][j])
    lcs = []
    i, j = 0, 0
    while i < len(text1) and j < len(text2):
        if text1[i] == text2[j]:
            lcs.append(text1[i])
            i += 1
            j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            i += 1
        else:
            j += 1
    
    return dp[0][0],''.join(lcs)

print("Length of LCS is {} and it's value is {}".format(longestCommonSubsequence("ABCBDAB", "BECAB")[0],longestCommonSubsequence("ABCBDAB", "BECAB")[1]))  # Output: "BCAB"
print("Length of LCS is {} and it's value is {}".format(longestCommonSubsequence("AXYT", "AYZX")[0],longestCommonSubsequence("AXYT", "AYZX")[1]))  # Output: "AY"
print("Length of LCS is {} and it's value is {}".format(longestCommonSubsequence("AGGTAB", "GXTXAYB")[0],longestCommonSubsequence("AGGTAB", "GXTXAYB")[1]))  # Output: "GTAB"
print("Length of LCS is {} and it's value is {}".format(longestCommonSubsequence("", "")[0],longestCommonSubsequence("", "")[1]))  # Output: ""
print("Length of LCS is {} and it's value is {}".format(longestCommonSubsequence("A", "")[0],longestCommonSubsequence("A", "")[1]))  # Output: ""
print("Length of LCS is {} and it's value is {}".format(longestCommonSubsequence("", "A")[0],longestCommonSubsequence("", "A")[1]))  # Output: ""
print("Length of LCS is {} and it's value is {}".format(longestCommonSubsequence("ABC", "CBA")[0],longestCommonSubsequence("ABC", "CBA")[1]))  # Output: "C"


