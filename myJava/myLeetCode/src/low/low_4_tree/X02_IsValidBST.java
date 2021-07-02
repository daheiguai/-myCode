package low.low_4_tree;

/**
 * 这道题范围很重要
 * 明明逻辑是对的，但是用int的最大值不行，必须用long的  马德题目也没说节点值的范围
 */
public class X02_IsValidBST {
    public boolean isValidBST(TreeNode root) {
        return isValidBST(root,Long.MAX_VALUE,Long.MIN_VALUE);
    }


    public boolean isValidBST(TreeNode root,long max ,long min){
        if (root == null) return true;
        if (root.val>=max || root.val<=min)return false;
        return isValidBST(root.left,root.val,min)&&isValidBST(root.right,max,root.val);
    }
}
