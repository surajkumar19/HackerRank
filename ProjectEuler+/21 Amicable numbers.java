//package euler;



import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Amicablenumbers_1 
{
	
	public static int factors(int n) 
	{
			int sum=0;
			int k=(int) Math.sqrt(n);
			for(int i=1;i<=k;i++ )
			{
				
				
				if(n%i==0)
				{
					sum+=i;
					if((i*i)!=n && i!=1)
					{
						sum+=(n/i);
					}
					
					
				}
			}
			//System.out.println(fact);
			
			return sum;
					
			
			
		

	}

	public static void main(String[] args) {
		Scanner take=new Scanner(System.in);
		int t=take.nextInt();
		ArrayList<Integer> cases=new ArrayList<>();
		boolean [] some=new boolean[100000];
		Arrays.fill(some, Boolean.TRUE);
		for(int k=0;k<t;k++)
		{
			
			int z=take.nextInt();
			int sum=0,j=0;
			for(int i=200;i<z;i++)
			{
				if(some[i])
				{
					int x=factors(i);
					if(x!=i && factors(x)==i )
					{
						sum+=i;
						//System.out.println(i);
					}
					else {
						some[i]=False;
					}
				}
				
				
			}
			System.out.println(sum);
		}
		
		
		//System.out.println(sum);
		//System.out.println(factors(t));
		
	}
}
