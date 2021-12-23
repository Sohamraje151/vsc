import SY.SYMarks;
import TY.TYMarks;
import java.util.*;
public class student
{
   
    
    
    public static void main(String args[]){
        SYMarks s=new SYMarks();
        TYMarks d=new TYMarks();
        s.accept();
        s.display();
        d.accept();
        d.display();
        int sy;
        int ty;
         int rno;
        String name;
        Scanner s1=new Scanner(System.in);
        System.out.println("Enter Roll number:");
        rno=s1.nextInt();
        Scanner s2=new Scanner(System.in);
        System.out.println("Enter Your name:");
        name=s2.nextLine();
        sy=(s.computerTotal+s.mathsTotal+s.electronicsTotal);
        ty=(d.Theory+d.Practicals);
        System.out.println("Roll number:"+rno);
        System.out.println("Student name:"+name);

        int total=(sy+ty)/5;
        if (total>=70){
        System.out.println("Grade - A");
        }
        else if (total>=60){
        System.out.println("Grade - B");
        }
        else if (total>=50){
        System.out.println("Grade - C");
        }
        else if (total>=40){
        System.out.println("Pass Class");
        }
        else{
        System.out.println("FAIL");       
        }
    }
}
