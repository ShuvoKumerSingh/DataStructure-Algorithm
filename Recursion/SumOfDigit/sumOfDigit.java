import java.util.Scanner;

class Main{
    private static int sumOfDigit(int num)
    {
        if(num == 0)
        {
            return num;
        }
        return (num%10)  + sumOfDigit(num/10);

    }

    private static int getUser() {
        Scanner scanner = new Scanner(System.in);
        int user;
        while(true)
        {
            System.out.println("Enter Number: ");
            user = scanner.nextInt();
            if(user>=0) break;
            System.out.println("Number can not be  zero");
        }
        return user;
    }

    public static void main(String[] args)
    {
        int user = getUser();
        System.out.println(sumOfDigit(user));
    }


}
