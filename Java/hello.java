import java.io.*;
import java.util.*;
class hello
{
    public static void main(String args[])
    {
        System.out.println("Hello java world...!!!\nEnter 1st number:");
    Scanner s= new Scanner(System.in);
    int a=s.nextInt();
        System.out.println("Enter 2nd number:");
    int b=s.nextInt();
    int c=a+b;
        System.out.println("Addition is:"+c);
    Scanner p= new Scanner(System.in);
        System.out.println("Enter your name:");
    String d=p.nextLine();
    Scanner q= new Scanner(System.in);
        System.out.println("Enter your College name:");
    String l=q.nextLine();
    Scanner r= new Scanner(System.in);
        System.out.println("Enter your address:");
    String k=r.nextLine();
        System.out.println("your name is:"+d);
        System.out.println("your College name is:"+l);
        System.out.println("your Address is:"+k);
    
    }
}