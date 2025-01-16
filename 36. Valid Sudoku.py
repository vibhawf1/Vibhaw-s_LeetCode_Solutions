class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                if ((num, 'row', i) in seen or
                    (num, 'col', j) in seen or
                    (num, 'box', i//3, j//3) in seen):
                    return False
                seen.add((num, 'row', i))
                seen.add((num, 'col', j))
                seen.add((num, 'box', i//3, j//3))
        return True
