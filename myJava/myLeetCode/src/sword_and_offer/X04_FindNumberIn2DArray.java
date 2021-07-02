package sword_and_offer;

public class X04_FindNumberIn2DArray {
    public boolean findNumberIn2DArray(int[][] matrix, int target) {
        if (matrix.length == 0)return false;
        if (matrix[0].length == 0)return false;
        for (int i = 0; i < matrix.length; i++) {
            if (matrix[i][0]<=target && matrix[i][matrix[0].length-1]>=target){
                for (int j = 0; j < matrix[0].length; j++) {
                    if (matrix[i][j] == target) return true;
                }
            }
        }
        return false;
    }
}
