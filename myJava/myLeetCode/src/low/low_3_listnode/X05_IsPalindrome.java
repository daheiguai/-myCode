package low.low_3_listnode;

public class X05_IsPalindrome {
    public boolean isPalindrome(ListNode head) {
        ListNode fast = head;
        ListNode low = head;
        while (fast.next!=null){
            fast = fast.next.next;
            low = low.next;
        }
        return false;
    }


}
