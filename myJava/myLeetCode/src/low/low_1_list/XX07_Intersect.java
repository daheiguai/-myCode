package low.low_1_list;


import java.util.ArrayList;
import java.util.Arrays;

public class XX07_Intersect {
//第一次不会写  第二次 自己写出了低效方法  还有个高效方法 用map
    public int[] intersect(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        ArrayList<Integer> result = new ArrayList<Integer>();
        int j = 0;
        for (int i = 0; i < nums1.length; i++) {
            if (j==nums2.length){break;}
            if (nums1[i] == nums2[j]){
                result.add(nums1[i]);
                j++;
            }else if (nums1[i] < nums2[j]){
                continue;
            }else {
                j++;
                i--;
            }
        }
        int[] a = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            a[i] = result.get(i);
        }
        return a;
    }

}
