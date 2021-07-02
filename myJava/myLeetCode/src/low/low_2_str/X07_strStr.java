package low.low_2_str;

public class X07_strStr {
    public int strStr(String haystack, String needle) {
        if (needle.equals("")){ return 0;}else if (needle.length()>haystack.length()){return -1;}

        int flag;
        for (int i = 0; i < haystack.length(); i++) {
            flag = 1;
            for (int j = 0; j < needle.length(); j++) {
                if (i+j>=haystack.length()){
                    flag = 0;
                    break;
                }
                if (haystack.charAt(i+j) == needle.charAt(j)){
                    continue;
                }else {
                    flag = 0;
                    break;
                }
            }
            if (flag == 1){return i;}
        }
        return -1;
    }
}
