import sys
import bl
import console_animator
import validator

input_board = list()
for row in sys.stdin.read().split('\n'):
    input_board.append(list(map(int, row.split(','))))

stream = sys.stdout

while True:
    console_animator.render(input_board, stream)
    input_board = bl.tick(input_board)
    print(validator.hash_state(input_board), file=stream)
