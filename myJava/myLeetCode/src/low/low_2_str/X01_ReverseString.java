package low.low_2_str;

public class X01_ReverseString {
    public void reverseString(char[] s) {
        int i = 0;
        int j = s.length-1;
        char temp = ' ';
        while (j>i){
            temp = s[i];
            s[i] = s[j];
            s[j] = temp;
            i++;
            j--;
        }
    }
}
