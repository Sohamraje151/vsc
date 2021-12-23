import java.util.*;
class prime
{
    public static void main(String args[])
    {
        int a;
        String s=" ";
        a=Integer.parseInt(args[0]);
        int num[]=new int[a];
        System.out.println("Prime numbers from 0 to "+a+" are:");
        for(int i=0;i<a;i++)
        {
            num[i]=i;
            boolean isP=true;
            for(int j=2;j<i;j++)
            {
                if(i%j==0)
                    {
                        isP=false;
                        break;
                    }
            }
            if(isP)
            {
                System.out.print(s+num[i]);

            }   
        }
    }
}
