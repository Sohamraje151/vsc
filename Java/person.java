import java.util.Scanner;
class personRecord
{
	int pid;
	String pname;
	int age;
	String gender;
	public personRecord(){
			pid=101;
			pname="person name";
			age=20;
			gender="male";

	}
	public personRecord(int pid,String pname,int age,String gender){
   		this.pid=pid; 
       	this.pname=pname; 
       	this.age=age;
       	this.gender=gender;
	}
	public void get_data(){
		   System.out.println("Enter Person's Information.\nEnter Id:");
	       Scanner x=new Scanner(System.in);
		   pid=x.nextInt();
	       System.out.println("Enter Name:");
		   Scanner y=new Scanner(System.in);
		    pname=y.nextLine();
		   System.out.println("Enter Age:");
 		   age=x.nextInt();
		   System.out.println("Enter gender:");
		   gender=y.nextLine();
		System.out.println("______________________________________");
	}
	public void put_data(){
		System.out.println("Id     : "+pid);
		System.out.println("Name   : "+pname);
		System.out.println("Age    : "+age);
		System.out.println("gender : "+gender);
		System.out.println("______________________________________");
	}
}
class person{

	public static void main(String args[])
	{
		int lmt,i;
		Scanner in=new Scanner(System.in);
		System.out.println("_________Default Person's Information____________");
		personRecord s1=new personRecord();// object s1 create for default constructor.
		s1.put_data();
		System.out.println("How many records you want to enter? ");
		lmt=in.nextInt();
		personRecord s2[]=new personRecord[10];
		for(i=0;i<lmt;i++)
		{
			s2[i]=new personRecord();
		}
		for(i=0;i<lmt;i++)
		{
			s2[i].get_data();
		}
		
		System.out.println("___________Person's Information____________");

		for(i=0;i<lmt;i++)
		{
			s2[i].put_data();
		}
	
	}
}
