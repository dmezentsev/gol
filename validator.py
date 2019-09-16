storage = {}


def hash_state(board):
    result = 0
    for rn, row in enumerate(board):
        for cn, cell in enumerate(row):
            pow_two = rn * len(row) + cn
            result += cell * (2 ** pow_two)
    return result
