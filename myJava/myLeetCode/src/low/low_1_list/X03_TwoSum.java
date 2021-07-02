package low.low_1_list;

import java.util.HashMap;

public class X03_TwoSum {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> m = new HashMap<Integer,Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (m.containsKey(target-nums[i])){
                return new int[]{i,m.get(target-nums[i])};
            }
            m.put(nums[i],i);
        }
        return nums;




//        解1 超出时间限制
//        List a = new ArrayList();
//        for (int i:nums){
//            if (i<target){
//                a.add(i);
//            }
//        }
//        int i = 0;
//        int[] result = new int[2];
//        while (i<a.size()){
//            for (int j=i+1;j<a.size();j++){
//                if (a.get(i)==a.get(j)){
//                    result[0] = i;
//                    result[1] = j;
//                    return result;
//                }
//            }
//        }
//        return result;
    }
}
