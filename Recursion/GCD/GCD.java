import java.util.Scanner;

public class GCD {
    // Using Euclidean Algorithm
    private static int gcd(int a, int b)
    {
        // if the number is negative then it's convert negative numbers to positive.
        // First two if condition section...
        if(a<0)
        {
            return -1*a;
        }
        if(b<0)
        {
            return -1*b;
        }

        if(b == 0) return a;
        else return gcd(b, a%b);
    }

    private static int getOutput() {
        Scanner scanner = new Scanner(System.in);
        int num1;
        int num2;
        while(true)
        {
            System.out.println("How to find Greatest Common Divisor between two numbers");

            System.out.print("Enter number1: ");
            num1 = scanner.nextInt();

            System.out.print("Enter number2: ");
            num2 = scanner.nextInt();

            if(num1>=0 && num2>=0) break;
            System.out.println("The Numbers must be positive integer only");
        }
        return gcd(num1, num2);
    }

    public static void main(String[] args)
    {
        System.out.println(getOutput());
    }


}
