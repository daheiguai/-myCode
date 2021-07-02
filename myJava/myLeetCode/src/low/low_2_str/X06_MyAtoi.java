package low.low_2_str;

public class X06_MyAtoi {
    public int myAtoi(String s) {
        int result = 0;
        char flag = ' ';
//        遍历字符串
        for (int i = 0; i < s.length(); i++) {
//            空白跳过
            if (s.charAt(i) == ' '){continue;}
//            第一次出现符好保存 符合第二次出现直接不合法退出
            if (s.charAt(i) == '+' || s.charAt(i) == '-'){
                if (flag == ' '){
                    flag = s.charAt(i);
                }else {break;}
            }
//            如果是非数字不合法退出
            if (Character.isDigit(s.charAt(i))){
//                第一次出现数字如果之前没有符合 当场给符合定值
                if (flag == ' '){flag = '+';}

                result = result*10 + Integer.valueOf(s.charAt(i));
            }else {break;}
        }
        return 0;
    }

}
