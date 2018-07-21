import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.next();
         int count=0;
        for(char c:s.toCharArray())
        {
        	if(c>='A'&&c<='Z')
        	{
        		count++;
        	}
        }
        System.out.println(count+1);
    }
}
