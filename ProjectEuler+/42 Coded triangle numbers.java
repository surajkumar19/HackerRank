//package euler;
import java.util.Scanner;

public class Codedtrianglenumbers {
	public static void main(String[] args) {
		
		Scanner take=new Scanner(System.in);
		long t=take.nextLong();
		for(long i=0; i<t;i++)
		{
			long n=take.nextLong();
//			System.out.println(factors(n*2));
			if(((Math.sqrt((8*n)+1)-1)/2)-Math.round((Math.sqrt((8*n)+1)-1)/2)==0)
			{
				System.out.println(Math.round((Math.sqrt((8*n)+1)-1)/2));
			}
			else {
				System.out.println(-1);
			}
			
			
		}
		
	}
}
	