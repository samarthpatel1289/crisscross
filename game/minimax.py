from rest_framework.generics import *
from rest_framework import status
from rest_framework.response import Response
import sys

# class MinimaxView(RetrieveAPIView):

# def get(self,request):
player, opponent = "1", "-1"
# ismax = x = 1, ismin = o = -1
# board = ["1", "-1", "1", "-1", "-1", "1", "1", "1", "-1"]


def is_move(board):
    for i in board:
        if i == "0":
            return True
    return False


def evaluate_score(board):
    for i in range(len(board)):
        # horizontal
        if board[0] == board[1] and board[1] == board[2]:
            if board[0] == player:
                return 10
            elif board[0] == opponent:
                return -10
        if board[3] == board[4] and board[4] == board[5]:
            if board[3] == player:
                return 10
            elif board[3] == opponent:
                return -10
        if board[6] == board[7] and board[7] == board[8]:
            if board[6] == player:
                return 10
            elif board[6] == opponent:
                return -10

        # vertical
        if board[0] == board[3] and board[3] == board[6]:
            if board[0] == player:
                return 10
            elif board[0] == opponent:
                return -10
        if board[1] == board[4] and board[4] == board[7]:
            if board[1] == player:
                return 10
            elif board[1] == opponent:
                return -10
        if board[2] == board[5] and board[5] == board[8]:
            if board[2] == player:
                return 10
            elif board[2] == opponent:
                return -10

        # diagonal
        if (board[0] == board[4] and board[4] == board[8]) or (
            board[2] == board[4] and board[4] == board[6]
        ):
            if board[4] == player:
                return 10
            elif board[4] == opponent:
                return -10

    return 0


def minimax(board, depth, isMax):
    score = evaluate_score(board)

    if score == 10:
        return score

    if score == -10:
        return score

    if not is_move(board):
        return 0

    if isMax:
        best = -1000
        for i in range(len(board)):
            if board[i] == "0":
                # print(board[i])
                board[i] = player

                best = max(minimax(board, depth + 1, False), best)

                board[i] = "0"
        return best
    else:
        best = 1000
        for i in range(len(board)):
            if board[i] == "0":
                # print(board[i])
                board[i] = opponent

                best = min(minimax(board, depth + 1, True), best)

                board[i] = "0"
        return best


def bestmove(board):
    best_value = 1000
    best_move = -1

    for i in range(len(board)):
        if board[i] == "0":
            board[i] = opponent
            move_value = minimax(board, 0, True)

            board[i] = "0"
            if move_value < best_value:
                best_value = move_value
                best_move = i

    return best_move


sys.setrecursionlimit(30000)
