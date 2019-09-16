def tick(board):
    next_state_board = list()
    for rn, row in enumerate(board):
        next_state_board.append([0] * len(row))
        for cn, cell in enumerate(row):
            step = []
            for n_r in (-1, 0, 1):
                for n_c in (-1, 0, 1):
                    if n_r == 0 and n_c == 0:
                        continue
                    step.append(board[rn + n_r if rn + n_r < len(board) else 0]
                                [cn + n_c if cn + n_c < len(board) else 0])
            neighbours_count = sum(step)
            if cell == 1 and neighbours_count in (2, 3):
                next_state_board[rn][cn] = 1
            elif cell == 0 and neighbours_count == 3:
                next_state_board[rn][cn] = 1
            else:
                next_state_board[rn][cn] = 0
    return next_state_board
