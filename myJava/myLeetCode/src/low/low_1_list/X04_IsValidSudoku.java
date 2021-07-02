package low.low_1_list;

import java.util.HashMap;
//第一遍不会  第二遍记住思路  但是盒子的边界没记住  (row/3)*3+(line/3)
public class X04_IsValidSudoku {
    public boolean isValidSudoku(char[][] board) {
        HashMap<Integer,HashMap<Character,Integer>> row = new HashMap<Integer,HashMap<Character,Integer>>();
        HashMap<Integer,HashMap<Character,Integer>> cow = new HashMap<Integer,HashMap<Character,Integer>>();
        HashMap<Integer,HashMap<Character,Integer>> box = new HashMap<Integer,HashMap<Character,Integer>>();

        for (int i = 0; i < 9; i++) {
            row.put(i,new HashMap<Character,Integer>());
            cow.put(i,new HashMap<Character,Integer>());
            box.put(i,new HashMap<Character,Integer>());
        }

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == '.'){continue;}
                row.get(i).put(board[i][j],row.get(i).getOrDefault(board[i][j],0)+1);
                if (row.get(i).get(board[i][j])>1){return false;}
                cow.get(j).put(board[i][j],cow.get(j).getOrDefault(board[i][j],0)+1);
                if (cow.get(j).get(board[i][j])>1){return false;}
                box.get((i/3)*3+j/3).put(board[i][j],box.get((i/3)*3+j/3).getOrDefault(board[i][j],0)+1);
                if (box.get((i/3)*3+j/3).get(board[i][j])>1){return false;}
            }
        }
        return true;
    }
}
