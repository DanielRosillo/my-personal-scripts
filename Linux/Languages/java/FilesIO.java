package tools;

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

/**
 * 
 * @author DanielRosillo
 * 
 */

public class FilesIO
{
    /**
     * 
     */
    private static final long serialVersionUID = 1L;
    private Stream<String> lines;

    public static void main(String[] args)
    {
	FilesIO s = new FilesIO();
	List<String> source = Arrays.asList("Pedro", "cantu");
	Path file = Paths.get("/mnt/DC/data.ini");

	s.create(file, source);
	s.read(file);

    }

    public void create(Path path, List<String> source)
    {
	System.out.println("Creando archivo...");
	try
	{
	    Files.write(path, source, Charset.forName("UTF-8"));
	    System.out.println("Archivo creado, direccion: " + path);
	}
	catch (IOException e)
	{
	    e.printStackTrace();
	}
    }

    public void read(Path path)
    {
	try
	{
	    lines = Files.lines(path);
	    System.out.println("Leyendo archivo: " + path.toString());
	    lines.forEach(System.out::println);
	}
	catch (IOException e)
	{
	    e.printStackTrace();
	}

    }
}