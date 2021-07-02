package low.low_2_str;

import java.util.HashMap;

public class X04_IsAnagram {
//第一次解 短字符串正确  长字符串错误   不应该用hashmap
    public boolean isAnagram(String s, String t) {
        HashMap<Character,Integer> m = new HashMap<Character,Integer>();
        if (s.length() != t.length()){
            return false;
        }
        for (int i = 0; i < s.length(); i++) {
            m.put(s.charAt(i),m.getOrDefault(s.charAt(i),0)+1);
        }
        for (int i = 0; i < s.length(); i++) {
            m.put(t.charAt(i),m.getOrDefault(t.charAt(i),0)-1);
        }
        for (char key: m.keySet()){
            if (m.get(key) != 0){
                return false;
            }
        }
        return true;
    }



}
