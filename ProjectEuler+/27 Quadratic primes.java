

import java.util.*;
public class Quadraticprimes {
	public static boolean prime(int n)
	{
		int i=1,j=0;
		while(i<=((int)java.lang.Math.sqrt(n))+1)
		{
			if(n%i==0)
			{
				j++;
			}
			i++;
		}
		if(j==1)
		{
			return True;
		}
		else
		{
			return False;
		}
		
	}
	
	public static void main(String[] args) {
		Scanner take=new Scanner(System.in);
		int t=take.nextInt();
		int n=0;
		int count=0;
		HashMap<Integer, String> ha=new HashMap<>();
		int y;
		for(int i=-t;i<t+1;i++)
		{
			for(int j=-t;j<t+1;j++)
			{
				n=0;
				count=0;
				//y=j;
				//int a1=(int) java.lang.Math.pow(i,n);
				
				int pp=(((n*n)+(i*n)+j));
				while((pp>0) && (pp%2!=0) && (pp%3!=0))
						{
							if(prime(pp))
							{
								count++;
								n++;
								pp=(((n*n)+(i*n)+j));
							}
							else
							{
								break;
							}
							
						}
				
				String s3=String.valueOf(i)+" "+String.valueOf(j);
				ha.put(count, s3);
			}
			
		}
		//System.out.print(ha);
		Set<Integer> st=ha.keySet();
		int max= Collections.max(st);
		System.out.println(ha.get(max));
		 
	}
}
