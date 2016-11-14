# for a given i, find the containing row, column, and box
def rows(i):
    position = i - i % 9
    return range(position, position + 9)


def columns(i):
    position = i % 9
    return range(position, position + 81, 9)


def boxes(i):
    position = 27 * (i // 27) + 3 * ((i % 9) // 3)
    return [i for j in range(3) for i in range(position + 9 * j, position + 9 * j + 3)]


# generate the connected indexes for all i's
connections = [(set.union(set(boxes(i)),
                          set(rows(i)),
                          set(columns(i)))
                - {i})
               for i in range(81)]


# recursively solve the board
def solve(board):
    possible = []

    # look for all empty squares and find the number of legal values for each
    for i in range(81):
        if board[i] == '0':
            # check which values are legal for an empty square
            values = set('123456789') - set(board[n] for n in connections[i])

            if len(values) == 0:  # in the words of trump: WRONG
                return

            else:  # yey
                possible.append((len(values), i, values))

    # yield board when no squares remain
    if len(possible) == 0 and '0' not in board:
        yield board

    # find the square with the least possibilities and attempt to solve using each possible value
    else:
        n, i, values = min(possible)
        for value in values:
            for attempt in solve(board[:i] + value + board[i + 1:]):
                yield attempt


puz = '950000000001000780000600020074100000005907300000008410020006000049000600000000039'


def test(solver):
    for attempt in solver(puz):
        for i in range(len(attempt) // 9 + 1):
            print(' '.join(attempt[i * 9:(i + 1) * 9]))


test(solve)
