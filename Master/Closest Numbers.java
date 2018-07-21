import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class ClosestNumbers {
	public static void main(String[] args) {
		Scanner stdin=new Scanner(System.in);
		int t=stdin.nextInt();
		int[] a=new int[t];
		for(int i=0;i<t;i++)
		{
			
			a[i]=stdin.nextInt();
		}
		Arrays.sort(a);
		ArrayList<Integer> e=new ArrayList<>();
		int diff=Integer.MAX_VALUE;
		for(int i=0;i<t-1;i++)
		{
			if(Math.abs(a[i]-a[i+1])<=diff)
			{
				if(diff!=Math.abs(a[i]-a[i+1]))
				{
					e=new ArrayList<>();
					diff=Math.abs(a[i]-a[i+1]);
				}
				
				e.add(a[i]);
				e.add(a[i+1]);
			}
		}
		for(int k:e)
		{
			System.out.printf("%d ",k);
		}
	}

}
