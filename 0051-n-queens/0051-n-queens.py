class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []              # to store all valid boards
        board = [["."] * n for _ in range(n)]   # empty board

        cols = set()             # used columns
        diag1 = set()            # (row - col)
        diag2 = set()            # (row + col)

        def backtrack(row):
            # Step 1: If all queens placed
            if row == n:
                # convert board into required format
                result.append(["".join(r) for r in board])
                return

            # Step 2: Try placing queen in every column
            for col in range(n):

                # Step 3: Check if safe
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue   # skip unsafe position

                # Step 4: Place the queen
                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Step 5: Move to next row
                backtrack(row + 1)

                # Step 6: Backtrack (undo)
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        # Start from row 0
        backtrack(0)

        return result