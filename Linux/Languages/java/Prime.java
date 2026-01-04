
public class Prime
{
    public static boolean isPair(int value)
    {
        if (value == 0) return false;
        return (value % 2 == 0);
    }

    public static boolean isPrime(int value)
    {
        if (value <= 1) return false;
        else if (value == 2 || value == 3 || value == 5 || value == 7) return true;
        else if (isPair(value) || value % 3 == 0) return false;
        else
        {
            long sqrtN = (long) Math.sqrt(value);
            for (long i = 6L; i <= sqrtN; i += 6)
                if (value % (i - 1) == 0 || value % (i + 1) == 0) 
                    return false;
            return true;
        }
    }

    public static void printPrimes(int limit)
    {
        for(int i=0;i<=limit;i++)
        {
            if(isPrime(i))System.out.println(i);
        }
    }
}