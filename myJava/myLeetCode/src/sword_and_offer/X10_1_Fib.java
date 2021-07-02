package sword_and_offer;

public class X10_1_Fib {

    public int fib(int n) {
        if (n == 0)return 0;
        if (n == 1)return 1;
        int a = 0;
        int b = 1;
        int temp = a;
        for (int i = 2; i <= n; i++) {
            temp = b;
            b = (temp+a) % 1000000007;
            a = temp;
        }
        return b;
    }
}