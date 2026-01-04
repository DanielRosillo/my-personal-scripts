package tools;

import java.io.ByteArrayOutputStream;
import static java.lang.System.out;

public class StringXOREncoder
{
    private final String KEY = "BOOZ";
    private final String HEX_STRING = "0123456789ABCDEF"; // Hexadecimal string for conversion

    public String encode(String str)
    {
	byte[] data = str.getBytes();
	int keyLen = KEY.length();

	// XOR encryption
	for (int i = 0; i < data.length; i++)
	{
	    data[i] = (byte) (data[i] ^ KEY.charAt(i % keyLen));
	}

	// Convert byte array to hex string
	StringBuilder hexStringBuilder = new StringBuilder();
	for (byte b : data)
	{
	    hexStringBuilder.append(hexChar((b >> 4) & 0x0F));
	    hexStringBuilder.append(hexChar(b & 0x0F));
	}

	return hexStringBuilder.toString();
    }

    // Helper method to convert int 0-15 to hexadecimal character
    private char hexChar(int value)
    {
	return HEX_STRING.charAt(value & 0x0F);
    }

    public String decode(String str)
    {
	ByteArrayOutputStream baos = new ByteArrayOutputStream(str.length() / 2);

	// Convert hex string to byte array
	for (int i = 0; i < str.length(); i += 2)
	{
	    baos.write((HEX_STRING.indexOf(str.charAt(i)) << 4) | HEX_STRING.indexOf(str.charAt(i + 1)));
	}

	byte[] b = baos.toByteArray();
	int len = b.length;
	int keyLen = KEY.length();

	// XOR decryption
	for (int i2 = 0; i2 < len; i2++)
	{
	    b[i2] = (byte) (b[i2] ^ KEY.charAt(i2 % keyLen)); // XOR byte with key
	}

	return new String(b);
    }
    
    static public void main(String ...args)
    {
	StringXOREncoder encoder = new StringXOREncoder();
	String data = encoder.encode("TEST");
	out.println(data);
	out.println(encoder.decode(data));
    }
}
