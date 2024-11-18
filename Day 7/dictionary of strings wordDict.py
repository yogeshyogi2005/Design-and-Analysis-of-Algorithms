s = "leetcode" 
wordDict = ["leet", "code"]  
word_set = set(wordDict)
dp = [False] * (len(s) + 1)
dp[0] = True  
for i in range(1, len(s) + 1):
    for j in range(i):
        if dp[j] and s[j:i] in word_set:
            dp[i] = True
            break

print(dp[len(s)])  
