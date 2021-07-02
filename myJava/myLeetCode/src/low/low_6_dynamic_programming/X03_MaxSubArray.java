package low.low_6_dynamic_programming;

public class X03_MaxSubArray {
    public int maxSubArray(int[] nums) {
        int res = nums[0];
        int[][] dp = new int[nums.length][nums.length+1];
        for (int i = 0; i < nums.length; i++) {
            for (int j = 1; j < nums.length-i+1; j++) {
                dp[i][j] = dp[i][j-1]+nums[j+i-1];
                res = Math.max(res,dp[i][j]);
            }
        }
        return res;
    }
}