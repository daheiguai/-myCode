package low.low_2_str;

public class X05_IsPalindrome {

    public boolean isPalindrome(String s) {
        int j =s.length()-1;
        s = s.toLowerCase();
        for (int i = 0; i < s.length(); i++) {
            if (!(Character.isLowerCase(s.charAt(i)) || Character.isDigit(s.charAt(i)))){
                continue;
            }
            if (!(Character.isLowerCase(s.charAt(j)) || Character.isDigit(s.charAt(j)))){
                j--;
                i--;
                continue;
            }
            if (s.charAt(i) != s.charAt(j)){
                return false;
            }
            if (i+1 >= j){break;}
            j--;
        }
        return true;
    }
}
