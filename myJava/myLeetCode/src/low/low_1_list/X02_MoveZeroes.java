package low.low_1_list;

public class X02_MoveZeroes {
    public void moveZeroes(int[] nums) {
        int[] a = new int[nums.length];
        int j = 0;
        for(int i:nums){
            if(i!=0){
                a[j] = i;
                j++;
            }
        }
        for(int i=0;i< nums.length;i++){
            nums[i] = a[i];
        }
    }
}
