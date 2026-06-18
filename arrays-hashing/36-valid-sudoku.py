import numpy

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        countingSet = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] not in countingSet:
                        countingSet.add(board[i][j])
                    else:
                        return False

            countingSet.clear()

        for i in range(9):
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] not in countingSet:
                        countingSet.add(board[j][i])
                    else:
                        return False

            countingSet.clear()

        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        if board[k+i*3][l+j*3] != '.':
                            if board[k+i*3][l+j*3] not in countingSet:
                                countingSet.add(board[k+i*3][l+j*3])
                            else:
                                return False
                countingSet.clear()
        return True