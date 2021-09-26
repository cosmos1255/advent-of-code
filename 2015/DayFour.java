import java.util.*;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class DayFour {

	public boolean fiveLeadingZeros(String s) {
		// part 1 uses 5, part 2 uses 6
		int num_zeros = 6;
		for (int i = 0; i < num_zeros; i++) {
			if (s.charAt(i) != '0')
				return false;
		}
		return true;
	}

	public Integer solution(String text_half, String num_half) {

		// input string
		String input = text_half + num_half;
		Integer temp_num_half = Integer.parseInt(num_half);

		while (true) {
			try {
				MessageDigest md = MessageDigest.getInstance("MD5");
				byte[] input_bytes = md.digest(input.getBytes());
				BigInteger input_num = new BigInteger(1, input_bytes);
				String input_text = input_num.toString(16);
				while (input_text.length() < 32) {
					input_text = "0" + input_text;
				}
				if (fiveLeadingZeros(input_text)) {
					System.out.println("Hashcode: " + input_text);
					return temp_num_half;
				}
			} catch (NoSuchAlgorithmException e) {
				throw new RuntimeException(e);
			}
			input = "";
			temp_num_half++;
			input = input + text_half + temp_num_half.toString();
		}
	}

	public static void main(String[] args) {
		// new class instance
		DayFour d4 = new DayFour();

		// string to be hashed
		String text_half = "ckczppom";
		String num_half = "1";
		System.out.println("Integer: " + d4.solution(text_half, num_half));
	}
}