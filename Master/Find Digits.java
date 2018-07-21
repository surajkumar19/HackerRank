//package algorithms;

import java.util.Scanner;



public class FindDigits {
	public static void main(String[] args) {
		Scanner stdin=new Scanner(System.in);
		long t=stdin.nextLong();
		for (int i=0;i<t;i++)
		{
			long z=stdin.nextLong();
			String s=String.valueOf(z);
			char[] c=s.toCharArray();
			int count=0;
			for(int j=0;j<c.length;j++)
			{
				int k=Integer.parseInt(String.valueOf(c[j]));
				if(c[j]!='0' && z%k==0)
				{
					count++;
				}
			}
			System.out.println(count);
		}
	}

}
