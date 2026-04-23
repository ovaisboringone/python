def matrix_chain(p):
    n = len(p) - 1
    dp = [[0]*(n+1) for _ in range(n+1)]

    for length in range(2, n+1):        # chain length
        for i in range(1, n-length+2):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j]
                dp[i][j] = min(dp[i][j], cost)

    return dp[1][n]


# input
n = int(input("Number of matrices: "))
p = list(map(int, input("Enter dimensions (n+1 numbers): ").split()))

print("Minimum multiplications:", matrix_chain(p))