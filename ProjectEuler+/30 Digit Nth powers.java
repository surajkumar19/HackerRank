

  
 
 import java.io.*;
 import java.util.*;
 import java.lang.Math;

 public class DigitNthpowers {

     public static void main(String[] args) {
         /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
         Scanner take= new Scanner(System.in);
         int a=take.nextInt();
         int b=(int) java.lang.Math.pow(10,a);
         int c=(int) java.lang.Math.pow(10,a-1);
        // System.out.println(b);
         //System.out.println(c);
         
    	 int sum2=0;
         for (int k=3;k< 600000;k++)
         {
        	 int sum1=0;
        	 int l=k;
        	 while(l>0)
        	 {
        		 int j=(int)(l%10);
        		 sum1+=java.lang.Math.pow(j,a);
        		 l=(int)(l/10);
        	 }
        	 if (sum1==k)
        	 {
        		 sum2+=k;
        	 }
        	 
        	 
         }
         System.out.println(sum2);
     }

	
 }
