

import java.util.Scanner;

public class down {
	static int[] count = new int[1000001];

	public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int Q = in.nextInt();
        for(int a0 = 0; a0 < Q; a0++){
            int N = in.nextInt();

           System.out.println(counting(N));
            
            
            
        }
    }




public static int counting(int n) {
    if (n <= 3) return n;
    if (count[n] > 0) return count[n];
    int min = Integer.MAX_VALUE;
    for (int i=2; i<=Math.sqrt(n); i++) {
        if (n % i == 0) {
            
            min = Math.min(min, 1 + counting(n/i));
        }
    }
    min = Math.min(min, 1 + counting(n-1));
    count[n] = min;
    return min;
}
}