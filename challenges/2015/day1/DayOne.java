import java.util.*;
import java.io.*;

public class DayOne {

	public int[] solution(String input) {
		// output format ret_arr[<part 1>, <part 2>]
		int[] ret_arr = new int[2];

		int input_size = input.length();
		// part 1 input
		int curr_floor = 0;
		// part 2 input 
		boolean isFirst = true; // set false after we enter basement
		for (int i = 0; i < input_size; i++) {
			if (input.charAt(i) == '(')
				curr_floor++;
			else 
				curr_floor--;
			if (curr_floor < 0 && isFirst) {
				ret_arr[1] = i+1;
				isFirst = false;
			}	
		}
		ret_arr[0] = curr_floor;
		return ret_arr;
	}

	public static void main(String[] args)
	{
		// new class instance
		DayOne d1 = new DayOne();
		// handle input
		try {
			String filename = "input-files/day-one-input.txt";
			Scanner sc = new Scanner(new File(filename));
			String input = sc.next();

			int[] ret_arr = d1.solution(input);
			System.out.println("Final floor: " + ret_arr[0]);
			System.out.println("First basement entrance position: " + ret_arr[1]);
			sc.close();
		} catch (FileNotFoundException e) {}
	}
}