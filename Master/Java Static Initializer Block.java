static boolean flag=True;
static int B;
static int H;
static
{
    Scanner b=new Scanner(System.in);
    B=b.nextInt();
    H=b.nextInt();
    if (B<=0 || H<=0)
    {
    	System.out.println("java.lang.Exception: Breadth and height must be positive");
       
         System.exit(0);
    }
}