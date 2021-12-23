import java.util.*;
class Student
{
  int rno;
  String name;
  void accept(int rn,String nm)
  {
    rno=rn;
    name=nm;
  }

class exam
{
  int m1,m2;
  void getmark(int s1,int s2)
  {
    m1=s1;
    m2=s2;
  }


class result
{
  int total;
  float per;
  void display()
  {
    total=m1+m2;
    per=(total*100)/200;
    System.out.println("Student Information\n-----------------------------\nRoll Number:"+rno+"\nStudent Name:"+name);
    System.out.println("Marks of Subject 1:"+m1);
    System.out.println("Total of Subject 2:"+m2);
    System.out.println("Total Marks:"+total);
    System.out.println("Percentage:"+per+"%");
      }
    }
  }
}
class j3
{
  public static void main(String[] args) {
    System.out.println("________Welcome here________");
    System.out.println("Enter Student Information:\nEnter Roll Number:");
    Scanner a=new Scanner(System.in);
    int Rno=a.nextInt();
    System.out.println("Enter Name:");
    Scanner b=new Scanner(System.in);
    String Name=b.nextLine();
    System.out.println("Enter Marks of Subject 1:");
    Scanner c=new Scanner(System.in);
    int n1=c.nextInt();
    System.out.println("Enter Marks of Subject 2:");
    int n2=c.nextInt();
    result R=new result();
    R.accept(Rno,Name);
    R.getmark(n1,n2);
    R.display();
  }
}