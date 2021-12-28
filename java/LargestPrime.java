public class LargestPrime {
    public static int getLargestPrime(int number)
    {
        if (number<=1)
        {
            return -1;
        }

        int largest=0;
        for (int i=2; i<=number;i++)
        {
            if (isPrime(i) && number%i==0)
            {
                    number=number/i;
                    largest=i;
            }

        }
        System.out.println(largest);
        return largest;

    }

    public static boolean isPrime(int number)
    {
        for (int i=2;i<number;i++)
        {
            if (number%i==0)
            {
                return false;
            }
        }
        return true;
    }
}
