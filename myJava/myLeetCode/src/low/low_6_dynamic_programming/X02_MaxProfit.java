package low.low_6_dynamic_programming;

public class X02_MaxProfit {
    public int maxProfit(int[] prices) {
        int maxpor = 0;
        int min = prices[0];
        for (int n :prices){
            maxpor = Math.max(maxpor,n-min);
            if (n<min) min = n;
        }
        return maxpor;

    }
}
