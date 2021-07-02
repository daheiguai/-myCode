package low.low_3_listnode;

public class X03_ReverseList {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode res = null;
        while (head!= null){
            ListNode temp = head.next;
            head.next = res;
            res = head;
            head = temp;
        }
        return res;
    }
}
