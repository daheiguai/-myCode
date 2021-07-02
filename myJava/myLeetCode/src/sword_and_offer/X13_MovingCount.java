package sword_and_offer;

public class X13_MovingCount {
    public int movingCount(int m, int n, int k) {
        int res = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if(!ifout(i,j,k)) break;
                System.out.println(m+"--"+n);
                res++;
            }
        }
        return res;
    }

    public boolean ifout(int num1,int num2,int k){
        int res = 0;
        while (num1!=0){
            res += num1%10;
            num1 /=10;
        }
        while (num2!=0){
            res += num2%10;
            num2 /= 10;
        }
        if(res>k) return false;
        return true;
    }
}
