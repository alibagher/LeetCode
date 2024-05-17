class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] != ".":
                    if (board[i][j] in rows[i] or (board[i][j] in cols[j]) or (board[i][j] in boxes[(i//3, j//3)])):
                        print (board[i][j])
                        return False
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[(i//3, j//3)].add(board[i][j])
        return True