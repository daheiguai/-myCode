package low.low_3_listnode;

public class X04_MergeTwoLists {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
//       初始情况分类
        if (l1 == null && l2 == null) return null;
        if (l1 == null) return l2;
        if (l2 == null) return l1;
//        第一个节点处理
        ListNode res;
        if (l1.val> l2.val){
            res = l2;
            l2 = l2.next;
        }else {
            res = l1;
            l1 = l1.next;
        }
        ListNode go = res;
//        之后的情况
        while (l1 != null){
            if (l2 == null){
                go.next = l1;
                return res;
            }
            if (l1.val< l2.val){
                go.next = l1;
                l1 = l1.next;
            }else {
                go.next = l2;
                l2 = l2.next;
            }
            go = go.next;
        }
        go.next = l2;
        return res;
    }
}
