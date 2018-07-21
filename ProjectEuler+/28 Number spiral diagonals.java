//package euler;

import java.util.Scanner;

public class Number_spiral_diagonals {
	public static void main(String[] args) {
		Scanner take=new Scanner(System.in);
		long t=take.nextLong();
		for (long j=0;j<t;j++)
		{
			long p=take.nextLong();
		    long modulas=1000000007;
            long value=333333336;
			long number1=(long)((p)/2)%modulas;
             long diagonal=(8*(number1%modulas))%modulas;
                //System.out.println(diagonal);
            diagonal=(diagonal*((number1+1)%modulas))%modulas;
                //System.out.println(diagonal);
            diagonal=(diagonal*((((2*(number1))%modulas)+1)%modulas)%modulas)%modulas;
                //System.out.println(diagonal);
            diagonal=(diagonal*value)%modulas;
             long diagonal1=(2*(number1%modulas))%modulas;
            diagonal1=(diagonal1*((number1+1)%modulas))%modulas;
             long diagonal2=(4*(number1%modulas))%modulas;
             long diagonal3=(1%modulas);
           long  realsolution=(diagonal+diagonal1)%modulas;
            realsolution=(realsolution+diagonal2)%modulas;
            realsolution=(realsolution+diagonal3)%modulas;
            System.out.println(realsolution);
		}
		take.close();
		
	}

}
