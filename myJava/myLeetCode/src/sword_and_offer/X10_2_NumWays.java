package sword_and_offer;

public class X10_2_NumWays {
    public int numWays(int n) {
        if (n == 0) return 1;
        if (n == 1) return 1;
        int a = 1,b = 1,temp;
        for (int i = 2; i <= n; i++) {
            temp = b;
            b = (a+b) % 1000000007;
            a = temp;
        }
        return b;
    }
}
