import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n, c = 0;
        int m = 0;
        in.nextInt(); // Ignore first int
        while (in.hasNextInt()) {
            n = in.nextInt();
            if (n > m) {
                c = 1;
                m = n;
            } else if (n == m) {
                c += 1;
            }
        }
        System.out.println(c);
    }
}
