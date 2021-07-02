package sword_and_offer;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
/*
太慢了
 */
public class X06_ReversePrint {
    public int[] reversePrint(ListNode head) {
        Stack<Integer> node = new Stack<>();
        while (head!=null){
            node.push(head.val);
            head = head.next;
        }
        int[] res = new int[node.size()];
        int i = 0;
        while (!node.isEmpty()){
            res[i] = node.pop();
            i++;
        }
        return res;
    }
}
