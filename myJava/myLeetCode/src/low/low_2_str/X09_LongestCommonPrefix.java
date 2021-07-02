package low.low_2_str;

public class X09_LongestCommonPrefix {

//    跑分低   待改进
    public String longestCommonPrefix(String[] strs) {
        String pre = "";
        int i = 0;
        char temp = ' ';
        while (true) {
//            把第一个str 第i位取出
            if (strs.length>0 && strs[0].length() > i) {
                temp = strs[0].charAt(i);
            } else {
                return pre;
            }
//            和其他str的第 i位比较
            for (int j = 1; j < strs.length; j++) {
//                某个str长度不够  当场返回
                if (i >= strs[j].length()) {
                    return pre;
                }
//                比较  不同则返回
                if (strs[j].charAt(i) != temp) {
                    return pre;
                }
            }
            pre += temp;
            i++;
        }
    }
}
