package sword_and_offer;

import java.util.HashMap;

/**
 * 下次自己用原地置换写出来
 */
public class X03_FindRepeatNumber {
    public int findRepeatNumber(int[] nums) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) return nums[i];
            map.put(nums[i],i);
        }
        return 0;
    }
}
