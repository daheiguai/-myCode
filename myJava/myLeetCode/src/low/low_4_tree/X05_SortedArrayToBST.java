package low.low_4_tree;

public class X05_SortedArrayToBST {
    public int[] nums;

    public TreeNode sortedArrayToBST(int[] nums) {
        TreeNode res = new TreeNode();
        this.nums = nums;
        sortedArrayToBSTHelper(res,0, nums.length-1);
        return res;
    }
    public void sortedArrayToBSTHelper(TreeNode root,int left,int right){
        root.left = new TreeNode();
        root.right = new TreeNode();
        root.val = nums[left+(right-left)/2];
        sortedArrayToBSTHelper(root.left,left,left+(right-left)/2-1);
        sortedArrayToBSTHelper(root.right,left+(right-left)/2+1,right);
    }
}
