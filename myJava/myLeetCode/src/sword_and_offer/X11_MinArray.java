package sword_and_offer;

public class X11_MinArray {
    public int minArray(int[] numbers) {
        if (numbers.length == 0) return 0;
        if (numbers.length == 1) return numbers[0];
        int j = 0;
        for (int i = 1; i < numbers.length; i++) {
            if (numbers[j]>numbers[i]){
                return numbers[i];
            }
            j++;
        }
        return numbers[0];
    }
}
