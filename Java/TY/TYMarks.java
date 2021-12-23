package TY;
import java.util.*;
public class TYMarks
{   public int Theory;
    public int Practicals;
    public void accept()
    {   
        Scanner s=new Scanner(System.in);
        System.out.println("Enter Total Marks of Theory:");
        Theory=s.nextInt();
        System.out.println("Enter Total Marks of Practicals:");
        Practicals=s.nextInt();
    }
    public void display()
    {
        System.out.println("Total Marks of Computer:"+Theory);
        System.out.println("Total Marks of Maths:"+Practicals);
    }
}