

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class ACMICPCTeam {
	public static void main(String[] args) {
		Scanner stdin=new Scanner(System.in);
		Scanner stdin2=new Scanner(System.in);
		int n=stdin.nextInt();
		int m=stdin.nextInt();
		String[] ss =new String[n];
		
		for(int i=0;i<n;i++)
		{
			
			ss[i]= stdin.next();	
		}
		ArrayList<Integer> ans=new ArrayList<>();
		int k=0;
		for(int i=0;i<n;i++)
		{
			for(int j=i+1;j<n;j++)
			{
				int count=0;
				int t=0;
				while(t<m)
				{
					if(ss[i].charAt(t)=='1' || ss[j].charAt(t)=='1')
						count++;
                    t++;
				}
				ans.add(count);
			}
		}
//		System.out.println(ans);
		Collections.sort(ans);
		int q=ans.get(ans.size()-1);
		System.out.println(q);
		int count2=0;
		for(int h:ans)
		{
			if(h==q)
			{
				count2++;
			}
		}
		System.out.println(count2);
		

		
	}

}
