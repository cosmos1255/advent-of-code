import java.util.*;
import java.io.*;

public class DaySix {
	// lights from [0-999][0-999]
	final int x = 1000, y = 1000;
	boolean[][] lights = new boolean[x][y];
	int[][] brightness = new int[x][y];

	// PART 2
	public int countLights2() {
		int count = 0;
		for (int i = 0; i < x; i++) {
			for (int j = 0; j < y; j++) {
				count += brightness[i][j];
			}
		}
		return count;
	}

	public void solution2(String input) {
		// <"toggle" || <"turn"> <"on/off"> <x1, y1> <"through"> <x2, y2>
		String[] input_args = input.split(" ");

		// first coords, last coords
		int x1 = 0, x2 = 0, y1 = 0, y2 = 0;
		boolean toggle = false;

		// parse input
		if (input_args[0].equals("toggle")) {
			String[] xy1 = input_args[1].split(",");
			String[] xy2 = input_args[3].split(",");
			x1 = Integer.parseInt(xy1[0]);
			y1 = Integer.parseInt(xy1[1]);
			x2 = Integer.parseInt(xy2[0]);
			y2 = Integer.parseInt(xy2[1]);
			toggle = true;
		} else {
			String[] xy1 = input_args[2].split(",");
			String[] xy2 = input_args[4].split(",");
			x1 = Integer.parseInt(xy1[0]);
			y1 = Integer.parseInt(xy1[1]);
			x2 = Integer.parseInt(xy2[0]);
			y2 = Integer.parseInt(xy2[1]);
		}

		// act on parsed input
		if (toggle) {
			for (int i = x1; i <= x2; i++) {
				for (int j = y1; j <= y2; j++) {
					brightness[i][j] += 2;
				}
			}
		} else {
			for (int i = x1; i <= x2; i++) {
				for (int j = y1; j <= y2; j++) {
					if (input_args[1].equals("on")) {
						brightness[i][j]++;
					} else {
						brightness[i][j]--;
						if (brightness[i][j] < 0) {
							brightness[i][j] = 0;
						}
					}
				}
			}
		}
	}

	// PART 1
	public int countLights() {
		int count = 0;
		for (int i = 0; i < x; i++) {
			for (int j = 0; j < y; j++) {
				count += (lights[i][j]) ? 1 : 0;
			}
		}
		return count;
	}

	public void solution(String input) {
		// <"toggle" || <"turn"> <"on/off"> <x1, y1> <"through"> <x2, y2>
		String[] input_args = input.split(" ");

		// first coords, last coords
		int x1 = 0, x2 = 0, y1 = 0, y2 = 0;
		// toggle or turn off/on
		boolean toggle = false;

		// parse input
		if (input_args[0].equals("toggle")) {
			String[] xy1 = input_args[1].split(",");
			String[] xy2 = input_args[3].split(",");
			x1 = Integer.parseInt(xy1[0]);
			y1 = Integer.parseInt(xy1[1]);
			x2 = Integer.parseInt(xy2[0]);
			y2 = Integer.parseInt(xy2[1]);
			toggle = true;
		} else {
			String[] xy1 = input_args[2].split(",");
			String[] xy2 = input_args[4].split(",");
			x1 = Integer.parseInt(xy1[0]);
			y1 = Integer.parseInt(xy1[1]);
			x2 = Integer.parseInt(xy2[0]);
			y2 = Integer.parseInt(xy2[1]);
		}

		// act on parsed input
		if (toggle) {
			for (int i = x1; i <= x2; i++) {
				for (int j = y1; j <= y2; j++) {
					lights[i][j] = (lights[i][j]) ? false : true;
				}
			}
		} else {
			for (int i = x1; i <= x2; i++) {
				for (int j = y1; j <= y2; j++) {
					if (input_args[1].equals("on")) {
						lights[i][j] = true;
					} else {
						lights[i][j] = false;
					}
				}
			}
		}
	}

	public static void main(String[] args) {
		// create new class instance
		DaySix d6 = new DaySix();

		// read in input
		try {
			String filename = "input-files/day-six-input.txt";
			Scanner sc = new Scanner(new File(filename));
			while (sc.hasNextLine()) {
				String input = sc.nextLine();
				d6.solution(input);
				d6.solution2(input);
			}
			System.out.println("The number of lights on: " + d6.countLights());
			System.out.println("Brightness: " + d6.countLights2());
			sc.close();
		} catch (FileNotFoundException e) {}
	}
}