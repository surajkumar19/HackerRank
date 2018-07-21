


import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class ConnectedCellsGrid {
	static int n,m;
	static boolean[][] mat;
	static int[][] matrix;


    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        m= in.nextInt();
        matrix = new int[n][m];
        mat=new boolean[n][m];
        for(int matrix_i = 0; matrix_i < n; matrix_i++){
            for(int matrix_j = 0; matrix_j < m; matrix_j++){
                matrix[matrix_i][matrix_j] = in.nextInt()-1;
            }
        }
        
        int mx = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (matrix[i][j] == 0)
                    mx = java.lang.Math.max(mx, ff(i, j));
            }
        }
//        int result = connectedCell(matrix);
        System.out.println(mx);
        in.close();
    }
    

    
    static int ff(int i, int j) 
    {
        if (i < 0 || i >= n || j < 0 || j >= m || matrix[i][j] == -1 || matrix[i][j] == 1)
            return 0;
        else 
        {
        	matrix[i][j] = 1;
        		return 1 + ff(i+1, j) + ff(i-1, j) + 
                   ff(i, j+1) + ff(i, j-1) + 
                   ff(i+1, j-1) + ff(i-1, j+1) + 
                   ff(i+1, j+1) + ff(i-1, j-1);
        }
    
}
}
