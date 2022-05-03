
def triangle(triangle): # https://leetcode-cn.com/problems/triangle/
    n = len(triangle)
    f = [[0] * n for _ in range(n)]
    f[0][0] = triangle[0][0]
    
    for i in range(1, n):
        f[i][0] = f[i - 1][0] + triangle[i][0]  # 边界
        for j in range(1, i):
            f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]  # 状态方程 并过滤无效状态
        f[i][i] = f[i - 1][i - 1] + triangle[i][i]  # 边界
    return min(f[n - 1])

def wordBreak(s, wordDict):# https://leetcode-cn.com/problems/word-break/submissions/
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool   https://leetcode-cn.com/problems/word-break/solution/shou-hui-tu-jie-san-chong-fang-fa-dfs-bfs-dong-tai/
    """
    slen = len(s)
    dp = [False for i in range(slen + 1)] # 要加上1
    dp[0] = True

    for i in range(1, slen + 1):
        temp = range(i)
        for j in temp[::-1]:
            if (s[j:i] in wordDict and dp[j]):
                dp[i] = True
                break
    return dp[slen]


if __name__ == "__main__":
    tri = [[2],[3,4],[6,5,7],[4,1,8,3]]
    # print(triangle(tri))
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(wordBreak(s,wordDict))
    