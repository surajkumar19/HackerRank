import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        //int a,b,n;
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int z=1,y=b;
        System.out.printf("%d ",a+b);
        for(int j=0;j<n-1;j++)
        {
            z=2*z;
            y=y+(z*b);
            System.out.printf("%d ",a+y);
            
                
        }
            System.out.println("");
        }
        
        
        in.close();
    }
}
