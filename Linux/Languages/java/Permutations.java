//package Math;

import static java.lang.System.out;

public class Permutations
{
    int i = 0;

    public void show(String s, StringBuffer aux)
    {
	if (s.length() == 1)
	{
	    // out.println(aux+""+s.charAt(0)+ s.charAt(1));
	    // out.println(aux+""+s.charAt(1)+ s.charAt(0));
	    out.println(aux + s);
	}

	else
	{
	    for (int i = 0; i < s.length(); i++)
	    {
		aux.append(s.charAt(i));
		String sl = s.substring(0, i) + s.substring(i + 1);
		show(sl, aux);
		aux.deleteCharAt(aux.length() - 1);
	    }
	}
    }

    public static void main(String[] args)
    {
	Permutations per = new Permutations();
	long totalTime = 0;
	long startTime = 0;

	// for(int i = 0;i<25;i++)
	// {
	startTime = System.currentTimeMillis();
	per.show("JAKIN", new StringBuffer());
	totalTime = System.currentTimeMillis() - startTime;

	System.out.println("Tiempo demorado:\t" + totalTime + " milisegundos.");
    }
}
