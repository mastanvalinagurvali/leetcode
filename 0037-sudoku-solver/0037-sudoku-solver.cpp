
class Solution {
public:

    bool isvalid(vector<vector<char>>& board, int row, int col, char c) {

        for (int j = 0; j < 9; j++) {
            if (board[j][col] == c)
                return false;
        }

        for (int i = 0; i < 9; i++) {
            if (board[row][i] == c)
                return false;
        }

        int tempi = (row / 3) * 3;
        int tempj = (col / 3) * 3;

        for (int i = tempi; i < tempi + 3; i++) {
            for (int j = tempj; j < tempj + 3; j++) {
                if (board[i][j] == c)
                    return false;
            }
        }

        return true;
    }

    bool solve(vector<vector<char>>& board) {

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {

                if (board[i][j] == '.') {

                    for (char c = '1'; c <= '9'; c++) {

                        if (isvalid(board, i, j, c)) {

                            board[i][j] = c;

                            if (solve(board) == true)
                                return true;
                            else
                                board[i][j] = '.';
                        }
                    }

                    return false;
                }
            }
        }

        return true;
    }

    void solveSudoku(vector<vector<char>>& board) {
        solve(board);
    }
};