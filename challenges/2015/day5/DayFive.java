import java.util.*;
import java.io.*;

public class DayFive {

	public boolean partTwo(String input) {
		boolean two_pair = false;
		boolean sandwich = false;
		int input_len = input.length();

		// check for two pairs, non-overlapping
		// storing substrings to test
		List<String> sub_strs = new ArrayList<>();
		for (int i = 0; i < input_len-1; i++) {
			String sub_str = input.substring(i, i+2);
			if (sub_strs.contains(sub_str) && (sub_strs.indexOf(sub_str) != sub_strs.size()-1)) {
				two_pair = true;
				break;
			}
			sub_strs.add(sub_str);
		}

		// check for sandwich ("xyx", "aba", "eee", etc.)
		for (int i = 0; i < input_len-2; i++) {
			String sub_str = input.substring(i, i+3);
			if (sub_str.charAt(0) == sub_str.charAt(2)) {
				sandwich = true;
				break;
			}
		}
		if (two_pair && sandwich)
			return true;
		return false;
	}

	public boolean partOne(String input) {
		int vowels = 0;
		boolean double_let = false;
		int input_len = input.length();
		for (int i = 0; i < input_len-1; i++) {
			String sub_str = input.substring(i, i+2);
			// test for wrong strings
			switch (sub_str) {
				case "ab": {
					return false;
				}
				case "cd": {
					return false;
				}
				case "pq": {
					return false;
				}
				case "xy": {
					return false;
				}
			}
			// test for doubles
			if (sub_str.charAt(0) == sub_str.charAt(1))
				double_let = true;
		}
		char[] input_arr = input.toCharArray();
		for (char c : input_arr) {
			switch (c) {
				case 'a':{
					vowels++;
					break;
				}
				case 'e':{
					vowels++;
					break;
				}
				case 'i':{
					vowels++;
					break;
				}
				case 'o':{
					vowels++;
					break;
				}
				case 'u':{
					vowels++;
					break;
				}
			}
		}
		if ((vowels >= 3) && double_let)
			return true;
		return false;
	}

	public static void main(String[] args) {
		// create class instance
		DayFive d5 = new DayFive();
		// read input from file
		try {
			String filename = "input-files/day-five-input.txt";
			int nice_counter = 0;
			int nice_counter_2 = 0;

			Scanner sc = new Scanner(new File(filename));
			while (sc.hasNext()) {
				String input = sc.next();
				if (d5.partOne(input)) {
					nice_counter++;
				}
				if (d5.partTwo(input)) {
					nice_counter_2++;
				}
			}
			System.out.println("Part 1: There were " + nice_counter + " nice strings.");
			System.out.println("Part 2: There were " + nice_counter_2 + " nice strings.");
			sc.close();
		} catch (FileNotFoundException e) {}
	}
}