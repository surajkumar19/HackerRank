//package plag_project;

import java.util.Scanner;

public class Doublebasepalindromes {
	public static void main(String[] args) {
		
		Scanner take=new Scanner(System.in);
		long n =take.nextLong();
		long b=take.nextLong();
		
		long sum=0;
		
		for(long i=1;i<n;i++)
		{ 
			if(ispal(String.valueOf(i)))
			{
				String bb=(Long.toString(i,(int) b));
				if( ispal(bb))
				{
					sum+=i;
				}
			}
			
		}
		System.out.println(sum);
		
		
	}



static boolean ispal(String s)
{
	
	while (s.length()!=0 && s.length()!=1 && (s.charAt(0))==(s.charAt(s.length()-1)) )
	{
		
		s=s.substring(1, s.length()-1);
		
		
	}
	if (s.length()==0 ||s.length()==1)
	{
	return True;
	}
	else
	{
		return False;
	}
}

}