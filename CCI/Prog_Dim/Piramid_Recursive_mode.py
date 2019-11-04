pir = [
    [7, 0, 0, 0, 0],
    [3, 8, 0, 0, 0],
    [8, 1, 0, 0, 0],
    [2, 7, 4, 4, 0],
    [4, 5, 2, 6, 5]
]

n = len(pir[0]) - 1


def gt_pir(i, j):
    if i == n:
        return pir[i][j]
    else:
        return pir[i][j] + max(gt_pir(i + 1, j), gt_pir(i + 1, j + 1))


print(gt_pir(0, 0))
