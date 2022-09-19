import java.util.Scanner;

public class Power {


    private static int powerOfNumber(int base, int exp)
    {
        if(exp == 0) return 1;
        if(exp == 1) return base;
        else return base * powerOfNumber(base, exp - 1);
    }

    private static int getResult() {
        Scanner scanner = new Scanner(System.in);
        int base;
        int exp;
        while(true)
        {
            System.out.print("Enter base: ");
            base = scanner.nextInt();

            System.out.print("Enter exponent: ");
            exp = scanner.nextInt();

            if(base>=0 && exp>=0) break;
            System.out.println("The base & exponent must be positive integer only");
        }
        return powerOfNumber(base, exp);
    }

    public static void main(String[] args)
    {
        int result = getResult();
        System.out.println(result);
    }


}


