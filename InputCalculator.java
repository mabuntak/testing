import java.util.Scanner;

public class InputCalculator {

    public static void inputThenPrintSumAndAverage()
    {
        Scanner scanner=new Scanner(System.in);
        int sum=0;
        int count=0;
        while (true)
        {
            boolean isAnInt=scanner.hasNextInt();
            if (isAnInt)
            {
                int number=scanner.nextInt();
                sum+=number;
                count++;
            }
            else{
                break;
            }
            scanner.nextLine();

        }
        long average=Math.round((float) sum / (float) count);
        System.out.println("SUM = "+sum+" AVG = "+average);
        scanner.close();
    }
}
