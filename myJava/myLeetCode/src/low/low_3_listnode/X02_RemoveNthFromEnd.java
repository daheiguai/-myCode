package low.low_3_listnode;

public class X02_RemoveNthFromEnd {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head.next == null){return null;}
        ListNode go = head;
        if (n == 1 ){
            while (go.next.next!= null){
                go = go.next;
            }
            go.next = null;
            return head;
        }
        ListNode targit = head;


        for (int i = 0; i < n-1; i++) {
            go = go.next;
        }
        while (go.next != null){
            go = go.next;
            targit = targit.next;
        }
        targit.val = targit.next.val;
        targit.next = targit.next.next;
        return head;
    }
}
