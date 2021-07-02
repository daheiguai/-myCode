package sword_and_offer;

import java.util.Stack;

public class X09_CQueue {
    public Stack<Integer> stack1;
    public Stack<Integer> stack2;

    public X09_CQueue() {
        this.stack1 = new Stack();
        this.stack2 = new Stack();
    }

    public void appendTail(int value) {
        stack1.push(value);
    }


    public int deleteHead() {
        if (!stack2.isEmpty()){
            return stack2.pop();
        }else if (!stack1.isEmpty()){
            while (!stack1.isEmpty()){
                stack2.push(stack1.pop());
            }
            return stack2.pop();
        }
        return -1;
    }
}
