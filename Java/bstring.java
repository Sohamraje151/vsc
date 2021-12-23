import java.util.*;
class bstring
{
    public static void main(String args[])
    {
        Scanner s=new Scanner(System.in);
        System.out.println("Enter any String:");
        String a=s.nextLine();
        StringBuffer b=new StringBuffer(a);
        
        System.out.println("Original String:"+a);
    
        System.out.println("After Insert:"+b.insert(0,"Hello "));
        
        System.out.println("After delete:"+b.delete(2,5));
        
        System.out.println("After append:"+b.append(" Thank you.!!"));
    
        System.out.println("After reverse:"+b.reverse());
        

    }
}