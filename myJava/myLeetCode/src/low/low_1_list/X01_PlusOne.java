package low.low_1_list;

public class X01_PlusOne {
    public int[] plusOne(int[] digits) {
        int i = digits.length-1;
        while (digits[i]+1==10){
            if(i!=0){
                digits[i] = 0;
                i--;
            }else {
                int[] a = new int[digits.length+1];
                a[0] = 1;
                return a;
            }
        }
        digits[i]++;
        return digits;
    }
}
