def possible_paths(n):
    gr = [[0] * (n + 1) for _ in range(n+1)]

    for i in range(n+1):
        gr[i][0] = 1
        gr[0][i] = 1
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            gr[i][j]  = gr[i-1][j] + gr[i][j-1]

    return gr[n][n]

print(possible_paths(20))