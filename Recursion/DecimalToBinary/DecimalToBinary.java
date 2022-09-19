import java.util.Scanner;

public class DecimalToBinary {
    private static int decimalToBinary(int num)
    {

        if(num == 0) return 0;
        else return num%2 + decimalToBinary(num/2)*10;
    }

    private static int getOutput() {
        Scanner scanner = new Scanner(System.in);
        int user_inp;
        while(true)
        {
            System.out.println("How to convert a number from Decimal to Binary");

            System.out.print("Enter number: ");
            user_inp = scanner.nextInt();


            if(user_inp>=0) break;
            System.out.println("The Number must be positive integer only");
        }
        return decimalToBinary(user_inp);
    }

    public static void main(String[] args)
    {
        System.out.println(getOutput());
    }
}
