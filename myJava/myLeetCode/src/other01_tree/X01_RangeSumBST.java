package other01_tree;


public class X01_RangeSumBST {
    public int result = 0;
    public int rangeSumBST(TreeNode root, int low, int high) {
        find(root,low,high);
        return this.result;
    }
    public void find(TreeNode root,int low,int high){
        if (root.val>=low && root.val<=high){this.result+=root.val;}

        if (root.left != null){
            find(root.left,low,high);
        }

        if (root.right != null){
            find(root.right,low,high);
        }

    }

}