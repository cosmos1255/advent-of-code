import java.util.*;
import java.io.*;

public class DayTwo {

	public int[] parseInput(String input) {
		String[] vals = input.split("x");
		int[] lwh = {Integer.parseInt(vals[0]), Integer.parseInt(vals[1]), Integer.parseInt(vals[2])};
		return lwh;
	}

	public int calcSqFt(int l, int w, int h) {
		int a = l*w, b = w*h, c = l*h;
		int min_side = Math.min(a, Math.min(b, c));
		return 2*a + 2*b + 2*c + min_side;
	}

	public int calcRibbon(int l, int w, int h) {
		int max_side = Math.max(Math.max(l, w), h);
		int bow = l*w*h;

		if (max_side == l) {
			return 2*w + 2*h + bow;
		}
		else if (max_side == w) {
			return 2*l + 2*h + bow;
		}
		else if (max_side == h) {
			return 2*l + 2*w + bow;
		}
		return -1;
	}

	public int[] solution(List<String> input) {
		// output format ret_arr[<part 1>, <part 2>]
		int[] ret_arr = new int[2];

		// some necessary variables
		int tot_sqft = 0; // part 1
		int tot_ft_ribbon = 0; // part 2
		int input_len = input.size();
		for (int i = 0; i < input_len; i++) {
			// format: lwh[<len>, <wid>, <height>]
			int[] lwh = parseInput(input.get(i));
			tot_sqft += calcSqFt(lwh[0], lwh[1], lwh[2]);
			tot_ft_ribbon += calcRibbon(lwh[0], lwh[1], lwh[2]);
		}

		ret_arr[0] = tot_sqft;
		ret_arr[1] = tot_ft_ribbon;

		return ret_arr;
	}

	public static void main(String[] args)
	{
		// new class instance
		DayTwo d2 = new DayTwo();
		// handle input
		try {
			String filename = "input-files/day-two-input.txt";
			Scanner sc = new Scanner(new File(filename));
			List<String> input = new ArrayList<>();
			while (sc.hasNext()) {
				input.add(sc.next());
			}
			int[] ret_arr = d2.solution(input);
			System.out.println("Total square feet needed: " + ret_arr[0]);
			System.out.println("Total feet of ribbon needed: " + ret_arr[1]);
			sc.close();
		} catch (FileNotFoundException e) {}
	}
}