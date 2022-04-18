
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

if __name__ == "__main__":
    tri = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print(triangle(tri))
    