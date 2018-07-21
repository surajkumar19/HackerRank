

import java.util.*;

public class name_scores {
	public static void main(String[] args) {
		Scanner take=new Scanner(System.in);
		int a=Integer.parseInt(take.next());
		HashMap<String, Integer> ha=new HashMap<>();
		ArrayList<String> al = new ArrayList<String>();
		for(int k=1;k<=a;k++)
		{
			String s= take.next();
			
			 al.add(s);
		
		}
		Collections.sort(al);
		//System.out.println(al);
		int i=0;
		for(String c:al)
		{
			i++;
			int sum=0;
			for(Character c1:c.toCharArray())
			{
				sum=sum+c1-'A'+1;
			}
			
			ha.put(c, sum*i);
		}
		
		//System.out.println(ha);
		int b=Integer.parseInt(take.next());
		for(int k2=0;k2<b;k2++)
		{
			String s1= take.next();
			System.out.println(ha.get(s1));
		}
	}

}
