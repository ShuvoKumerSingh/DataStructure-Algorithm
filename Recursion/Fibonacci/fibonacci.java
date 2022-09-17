import java.util.Scanner;

class Main{
    public static int fibonacci(int n)
    {
        if(n==0 || n==1)
        {
            return n;
        }
        else return fibonacci(n-1) + fibonacci(n-2);

    }
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        int user;
        while(true)
        {
            System.out.println("Enter Number: ");
            user = scanner.nextInt();
            if(user>=0) break;
            System.out.println("Number can not be  zero");
        }
        System.out.println(fibonacci(user));
    }


}