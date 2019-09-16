import sys
import os
import time


def render(board, stream):
    os.system('clear')
    for rn, row in enumerate(board):
        stream.write('{}\n\r'.format(row))

    stream.flush()
    time.sleep(0.5)
