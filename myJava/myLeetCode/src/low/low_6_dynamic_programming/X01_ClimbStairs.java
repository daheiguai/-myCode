package low.low_6_dynamic_programming;

public class X01_ClimbStairs {
    public int climbStairs(int n) {
//        初始化笔记本
        int[] textbok = new int[n+1];
        textbok[0] = 1;
        textbok[1] = 1;
        if (n>=2){
            for (int i = 2; i <= n; i++) {
                textbok[i] = textbok[i-1]+textbok[i-2];
            }
        }
        return textbok[n];
    }
}
