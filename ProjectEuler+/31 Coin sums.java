import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class CoinChangeProblem {
	public static void main(String[] args) {
		long[] coins= {0,1,2,5,10,20,50,100,200};
		Scanner take=new Scanner(System.in);
		long t=take.nextLong();
		ArrayList<Long>  z=new ArrayList<Long>();
		for(long k=0;k<t;k++)
		{
			z.add(take.nextLong());
		}
		
			long  n;
			n=Collections.max(z);
            long m=1000000007;
			long [][]matrix=new long[coins.length][ (int) (n+1)];
			
			for(long i=0;i<coins.length;i++)
			{
				
				for(long j=0;j<n+1;j++)
				{
					if(i==0)
					{
						if(j==0)
						{
							matrix[0][0]=1;
						}
						else {
							matrix[0][(int) j]=0;
						}
					}
					else
					{
						if(coins[(int) i]>j)
						{
							matrix[(int) i][(int) j]=matrix[(int) (i-1)][(int) j]%m;
						}
						else
						{
							matrix[(int) i][(int) j]=(matrix[(int) (i-1)][(int) j]%m+matrix[(int) i][(int) (j-coins[(int) i])]%m)%m;
						}
					}
					
				}
			}
			
//			for(long i=0;i<coins.length;i++)
//				{
//					for(long j=0;j<n+1;j++)
//					{
//						System.out.printf("%5d ",matrix[(int) i][(int) j]);
//					}
//					System.out.println();
//				}
////			System.out.println(matrix[coins.length-1][(int) n]%m);
		
			for(int k=0;k<t;k++)
			{
				long p=z.get(k);
				System.out.println(matrix[coins.length-1][(int) p]);
			}
		
		
	}

}
