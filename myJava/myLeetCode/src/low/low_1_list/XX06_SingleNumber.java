package low.low_1_list;
//XX意思就是  之前有一部分python写的题  现在再次刷题  补回来
public class XX06_SingleNumber {
    public int singleNumber(int[] nums) {
        int result = 0;
        for (int i:nums){
            result = result^i;
        }
        return result;
    }

}
