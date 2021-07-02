package sword_and_offer;

/**
 * 下次用个快点的方法
 */
public class X05_ReplaceSpace {
    public String replaceSpace(String s) {
        String res = "";
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' '){
                res+="%20";
                continue;
            }
            res+=s.charAt(i);
        }

        return res;
    }
}
