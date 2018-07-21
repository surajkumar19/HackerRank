//package euler;

import java.util.Scanner;

public class Nonabundantsums {
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
		
		int [] sums=new int[28124];
		int i=0;
		for(i=0;i<=28123;i++)
		{
			int z=factors(i);
			if(i==z)
			{
				sums[i]=0;
			}
			else if(i<z)
			{
				sums[i]=1;
			}
			else
			{
				sums[i]=-1;
			}
		}
		Scanner take =new Scanner(System.in);
		int t=take.nextInt();
		for(int xx=0;xx<t;xx++)
		{
			int flag=0,j;
			int n=take.nextInt();
			if(n>28123 )
			{
				System.out.println("YES");
			}
			else if(n==28123)
			{
				System.out.println("NO");
			}
			else 
			{
				for(j=1;j<n;j++)
				{
					if((sums[j]==1)&&(sums[n-j]==1))
					{
						//System.out.println("YES");
						
						flag=1;
						break;
					}
				}
				if(flag==0)
				{
					System.out.println("NO");
				}
				else {
					System.out.println("YES");
					//System.out.println(j);
				}
			}
		}
		
	}

}
