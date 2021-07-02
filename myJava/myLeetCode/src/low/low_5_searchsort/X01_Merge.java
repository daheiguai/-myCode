package low.low_5_searchsort;

public class X01_Merge {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m + n - 1;
        m--;
        n--;
        while (n>=0){
            if (m<0){
                nums1[i] = nums2[n];
                n--;
            }else if (nums1[m]<nums2[n]){
                nums1[i] = nums2[n];
                n--;
            }else {
                nums1[i] = nums1[m];
                m--;
            }
            i--;
        }
    }
}