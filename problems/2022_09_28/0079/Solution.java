class Solution {
    public boolean exist(char[][] board, String word) {
        int rows = board.length, cols = board[0].length;

        // anormaly detection
        if (word.length() == 0) {
            return true;
        }

        if (rows * cols < word.length()) {
            return false;
        }

        for (int row = 0; row < rows; ++row) {
            for (int col = 0; col < cols; ++col) {
                boolean isFound = dfs(board, new boolean[rows][cols], row, col, word, 0);
                if (isFound) {
                    return true;
                }
            }
        }

        return false;
    }

    private boolean dfs(char[][] board, boolean[][] visited, int row, int col, String word, int index) {
        if ((row < 0 || row >= board.length) || (col < 0 || col >= board[0].length)
                || board[row][col] != word.charAt(index)) {
            return false;
        }

        if (visited[row][col]) {
            return false;
        }

        if (index == word.length() - 1) {
            return true;
        }

        visited[row][col] = true;

        if (dfs(board, visited, row, col + 1, word, index + 1)) {
            return true;
        }

        if (dfs(board, visited, row, col - 1, word, index + 1)) {
            return true;
        }

        if (dfs(board, visited, row + 1, col, word, index + 1)) {
            return true;
        }

        if (dfs(board, visited, row - 1, col, word, index + 1)) {
            return true;
        }

        visited[row][col] = false;
        return false;
    }
}
