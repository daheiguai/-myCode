package low.low_2_str;

import java.util.HashMap;

public class X03_FirstUniqChar {
    public int firstUniqChar(String s) {
        HashMap<Character,Integer> m = new HashMap<Character,Integer>();
//        改进：  string里面直接获取char 的方法  string.charAt(index)
        char[] c = s.toCharArray();
        for (char i:c){
            m.put(i,m.getOrDefault(i,0)+1);
        }
        for (int i=0;i<c.length;i++){
            if (m.get(c[i])==1){
                return i;
            }
        }
        return -1;
    }
}
