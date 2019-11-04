pir = [
    [7, 0, 0, 0, 0],
    [3, 8, 0, 0, 0],
    [8, 1, 0, 0, 0],
    [2, 7, 4, 4, 0],
    [4, 5, 2, 6, 5]
]

n = len(pir[0]) - 1


def Dinm_mode():
    for i in range(n, 0, -1):
        for j in range(0, n):
            print(j)
            pir[i-1][j] = pir[i-1][j] + max(pir[i][j], pir[i][j + 1])


Dinm_mode()

# print(pir[0][0])
