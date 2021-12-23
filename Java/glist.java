import games.indoor;
import games.outdoor;
import java.util.*;
class glist
{
    public static void main(String args[])
    {
        glist obj=new glist();
        System.out.println(obj.hashCode());
        obj=null;
        System.gc();
        System.out.println("End of Garbage collection");
        
        int od,ind,i;
		Scanner in=new Scanner(System.in);
        System.out.println("How many records you want to enter in Indoor games? ");
        ind=in.nextInt();
        indoor a[]=new indoor[10];
        for(i=0;i<ind;i++)
        {
            a[i]=new indoor();
        }
        System.out.println("How many records you want to enter in Outdoor games? ");
		od=in.nextInt();
        outdoor b[]=new outdoor[10];
        for(i=0;i<ind;i++)
        {
            b[i]=new outdoor();
        }
        System.out.println("___________List of Indoor games players____________");
        for(i=0;i<ind;i++)
        {
            a[i].display();
        }
        System.out.println("___________List of Outdoor games players____________");
        for(i=0;i<ind;i++)
        {
            b[i].display();
        }
    }
    @Override
        protected void finalize()
        {
        System.out.println("Finalized method called");
        }
}
