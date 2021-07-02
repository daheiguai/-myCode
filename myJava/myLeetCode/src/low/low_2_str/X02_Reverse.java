package low.low_2_str;

public class X02_Reverse {

    public int reverse(int x) {
        int temp = 0;
        int reuslt = 0;
        while (x!=0){
            temp = x%10;
            if (reuslt+temp/10<Integer.MIN_VALUE/10 || reuslt+temp/10>Integer.MAX_VALUE/10){
                return 0;
            }
            reuslt = reuslt*10 + temp;
            x /= 10;
        }
        return reuslt;
    }

}
