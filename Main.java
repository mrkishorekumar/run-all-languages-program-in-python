import java.util.Scanner;
class Main
{
   public static void main(String args[])
   {
      String s;
      Scanner obj = new Scanner(System.in); /* create a object */
 
      System.out.println("Enter a string:");
      s = obj.nextLine(); /* Take string input and assign to variable */
      System.out.println("You entered string "+s); /* Print */
   }
}