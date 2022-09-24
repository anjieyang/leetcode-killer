class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<String> set = new HashSet<>();

        for (int i = 0; i < board.length; ++i) {
            for (int j = 0; j < board[i].length; ++j) {
                if ('.' == board[i][j]) {
                    continue;
                }

                char number = board[i][j];
                if (!set.add(number + " in row " + i)
                        || !set.add(number + " in col " + j)
                        || !set.add(number + " in block " + i / 3 + " - " + j / 3)) {
                    return false;
                }
            }
        }

        return true;
    }
}