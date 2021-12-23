package SY;
import java.util.*;
public class SYMarks
{   public int computerTotal;
    public int mathsTotal;
    public int electronicsTotal;
    public void accept()
    {   
        Scanner s=new Scanner(System.in);
        System.out.println("Enter Total Marks of Computer:");
        computerTotal=s.nextInt();
        System.out.println("Enter Total Marks of Maths:");
        mathsTotal=s.nextInt();
        System.out.println("Enter Total Marks of Electronics:");
        electronicsTotal=s.nextInt();
    }
    public void display()
    {
        System.out.println("Total Marks of Computer:"+computerTotal);
        System.out.println("Total Marks of Maths:"+mathsTotal);
        System.out.println("Total Marks of Electronics:"+electronicsTotal);
    }
}