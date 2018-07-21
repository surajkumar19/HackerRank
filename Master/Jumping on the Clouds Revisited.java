//package algorithms;


import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class JumpingonthClouds {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int c[] = new int[n];
        int e=100;
        for(int c_i=0; c_i < n; c_i++){
            c[c_i] = in.nextInt();
            
        }
        int j=0;
        int y=0;
        do 
        {
        	y=(k+y)%n;
        	if(c[y]==1)
        	{
        		e=e-3;
        	}
        	else {
        		e=e-1;
        	}
        }while(y!=0);
        System.out.println(e);
        
        
    }
}