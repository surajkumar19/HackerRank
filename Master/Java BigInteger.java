import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner take=new Scanner(System.in);
        BigInteger bi1 = new BigInteger(take.next());
        BigInteger bi2 = new BigInteger(take.next());
        System.out.println(bi1.add(bi2));
        System.out.println(bi1.multiply(bi2));
        
    }
}