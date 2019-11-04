class Automath:

    def __init__(self):
        self.dfa = {
            0: [1, 0, 0],
            1: [1, 2, 0],
            2: [3, 0, 0],
            3: [1, 4, 0],
            4: [5, 0, 0],
            5: [1, 4, 6],
        }
        self.str_math = "ABABAC"
        self.vals = {"A": 0, "B": 1, "C": 2}

    def change_dfa(self, np):
        self.dfa = np


def KMP(str_mat):
    auth = Automath()
    l_str = len(str_mat)
    l_aut = len(auth.dfa)
    x = 0
    for j in range(0, l_str):
        letter = str_mat[j:j + 1]

        if letter == auth.str_math[x]:
            x = auth.dfa[x][auth.vals[letter]]
        if (x != l_aut) and (j == l_str - 1):
            return -1
        elif x == l_aut:
            return j - x + 1


result = KMP('ABABABACC')
print(result)
