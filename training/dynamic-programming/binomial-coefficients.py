def binomial_coefficent(n, k):
    bc = [[0] * (n+1) for _ in range(n+1)]    

    for i in range(n+1):
        bc[i][0] = 1
        bc[i][i] = 1
    
    for i in range(2, n+1):
        for j in range(1, i):
            bc[i][j] = bc[i-1][j-1] + bc[i-1][j]
    
    return bc[n][k]

print(binomial_coefficent(5, 2))
