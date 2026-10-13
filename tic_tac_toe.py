# ============================================================
# TIC-TAC-TOE USING MINIMAX AND ALPHA-BETA PRUNING
# ============================================================

# X = MAX player
# O = MIN player
# _ = Empty cell

board = [
    'X', 'O', 'X',
    '_', 'O', '_',
    '_', '_', 'X'
]


# ------------------------------------------------------------
# DISPLAY BOARD
# ------------------------------------------------------------

def display_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


# ------------------------------------------------------------
# CHECK WINNER
# ------------------------------------------------------------

def check_winner(board):

    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:

        if board[a] == board[b] == board[c] and board[a] != '_':
            return board[a]

    # Draw
    if '_' not in board:
        return 'D'

    return None


# ============================================================
# PLAIN MINIMAX
# ============================================================

minimax_nodes = 0


def minimax(board, maximizing):

    global minimax_nodes

    # Count every node visited
    minimax_nodes += 1

    winner = check_winner(board)

    # Terminal states
    if winner == 'X':
        return 1

    if winner == 'O':
        return -1

    if winner == 'D':
        return 0

    # MAX player - X
    if maximizing:

        best_score = -float('inf')

        for i in range(9):

            if board[i] == '_':

                board[i] = 'X'

                score = minimax(board, False)

                board[i] = '_'

                best_score = max(best_score, score)

        return best_score

    # MIN player - O
    else:

        best_score = float('inf')

        for i in range(9):

            if board[i] == '_':

                board[i] = 'O'

                score = minimax(board, True)

                board[i] = '_'

                best_score = min(best_score, score)

        return best_score


# ============================================================
# ALPHA-BETA PRUNING
# ============================================================

alphabeta_nodes = 0
pruned_branches = 0


def alphabeta(board, maximizing, alpha, beta, depth=0):

    global alphabeta_nodes
    global pruned_branches

    # Count visited node
    alphabeta_nodes += 1

    winner = check_winner(board)

    # Terminal states
    if winner == 'X':
        return 1

    if winner == 'O':
        return -1

    if winner == 'D':
        return 0

    # MAX player - X
    if maximizing:

        best_score = -float('inf')

        for i in range(9):

            if board[i] == '_':

                board[i] = 'X'

                score = alphabeta(
                    board,
                    False,
                    alpha,
                    beta,
                    depth + 1
                )

                board[i] = '_'

                best_score = max(best_score, score)

                alpha = max(alpha, best_score)

                # PRUNING CONDITION
                if alpha >= beta:

                    pruned_branches += 1

                    print(
                        "  " * depth +
                        "PRUNED at position",
                        i + 1,
                        "(Alpha >= Beta)"
                    )

                    break

        return best_score

    # MIN player - O
    else:

        best_score = float('inf')

        for i in range(9):

            if board[i] == '_':

                board[i] = 'O'

                score = alphabeta(
                    board,
                    True,
                    alpha,
                    beta,
                    depth + 1
                )

                board[i] = '_'

                best_score = min(best_score, score)

                beta = min(beta, best_score)

                # PRUNING CONDITION
                if alpha >= beta:

                    pruned_branches += 1

                    print(
                        "  " * depth +
                        "PRUNED at position",
                        i + 1,
                        "(Alpha >= Beta)"
                    )

                    break

        return best_score


# ============================================================
# FIND BEST MOVE USING MINIMAX
# ============================================================

def find_best_move_minimax(board):

    best_score = -float('inf')
    best_move = None

    for i in range(9):

        if board[i] == '_':

            board[i] = 'X'

            score = minimax(board, False)

            board[i] = '_'

            if score > best_score:

                best_score = score
                best_move = i

    return best_move, best_score


# ============================================================
# FIND BEST MOVE USING ALPHA-BETA
# ============================================================

def find_best_move_alphabeta(board):

    best_score = -float('inf')
    best_move = None

    alpha = -float('inf')
    beta = float('inf')

    for i in range(9):

        if board[i] == '_':

            board[i] = 'X'

            score = alphabeta(
                board,
                False,
                alpha,
                beta
            )

            board[i] = '_'

            if score > best_score:

                best_score = score
                best_move = i

            alpha = max(alpha, best_score)

    return best_move, best_score


# ============================================================
# MAIN PROGRAM
# ============================================================

print("==============================================")
print("       TIC-TAC-TOE MINIMAX COMPARISON")
print("==============================================")

print("\nInitial Board:")

display_board(board)


# ============================================================
# RUN PLAIN MINIMAX
# ============================================================

minimax_nodes = 0

move1, score1 = find_best_move_minimax(board)

print("----------------------------------------------")
print("             PLAIN MINIMAX")
print("----------------------------------------------")

print("Best Move     :", move1 + 1)
print("Game Score    :", score1)
print("Nodes Explored:", minimax_nodes)


# ============================================================
# RUN ALPHA-BETA
# ============================================================

alphabeta_nodes = 0
pruned_branches = 0

print("\n----------------------------------------------")
print("          ALPHA-BETA PRUNING")
print("----------------------------------------------")

move2, score2 = find_best_move_alphabeta(board)

print("\nBest Move      :", move2 + 1)
print("Game Score     :", score2)
print("Nodes Explored :", alphabeta_nodes)
print("Pruned Branches:", pruned_branches)


# ============================================================
# COMPARISON
# ============================================================

print("\n==============================================")
print("                 COMPARISON")
print("==============================================")

print("Plain Minimax Nodes :", minimax_nodes)
print("Alpha-Beta Nodes    :", alphabeta_nodes)
print("Pruned Branches     :", pruned_branches)

if minimax_nodes > 0:

    reduction = (
        (minimax_nodes - alphabeta_nodes)
        / minimax_nodes
    ) * 100

    print("Node Reduction      : {:.2f}%".format(reduction))

# ============================================================
# CHECK WHETHER RESULT IS SAME
# ============================================================

print("\n----------------------------------------------")
print("              RESULT CHECK")
print("----------------------------------------------")

print("Minimax Best Move    :", move1 + 1)
print("Alpha-Beta Best Move :", move2 + 1)

print("Minimax Score        :", score1)
print("Alpha-Beta Score     :", score2)

if move1 == move2 and score1 == score2:

    print("\nSUCCESS!")
    print("Both algorithms produce the SAME result.")
    print("Alpha-Beta only removes unnecessary branches.")

else:

    print("\nResults are different.")