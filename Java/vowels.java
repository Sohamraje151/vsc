// display the number of non vowels in the given word.
import java.util.*;
class vowels
{
    public static void main(String args[])
    {
        int count=0;
        System.out.println("Enter any word");
        Scanner s1=new Scanner(System.in);
        String a=s1.nextLine();
        for(int i=0;i<a.length();i++)
        {
            char ch=a.charAt(i);
            if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'||ch=='A'||ch=='E'||ch=='I'||ch=='O'||ch=='U'||ch==' ')
            {
                count=count;
            }
            else
            {
                count++;
            }
        }
        System.out.println("Number of non vowels in given word:"+count);
    }
}