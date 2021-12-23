package games;
import java.util.*;
public class indoor
{   
    public int pid; 
    public String pname; 
    public String pgame; 
    public indoor()
    {
        Scanner s1=new Scanner(System.in);
        Scanner s2=new Scanner(System.in);
        System.out.println("_______Indoor games player_______");
        System.out.println("Enter ID of player:");
        pid=s1.nextInt();
        System.out.println("Enter name of player:");
        pname=s2.nextLine();
        System.out.println("Enter name of indoor Game:");
        pgame=s2.nextLine();
    }
    public void display()
    {
        System.out.println("ID of player:"+pid);
        System.out.println("Name of player:"+pname);
        System.out.println("Name of Indoor game:"+pgame);

    }
}
