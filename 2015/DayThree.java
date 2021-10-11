import java.util.*;
import java.io.*;

class Tuple {
	private int x;
	private int y;
	public Tuple(int x, int y) {
		this.x = x;
		this.y = y;
	}

	public boolean containsCoords(int x, int y) {
		if (this.x == x && this.y == y)
			return true;
		return false;
	}
}

public class DayThree {

	public int[] solution(String input) {
		// output format ret_arr[<part 1>, <part 2>]
		int[] ret_arr = new int[2];

		// some necessary variables
		// part 1
		List<Tuple> xy_coords = new ArrayList<>();
		xy_coords.add(new Tuple(0, 0));
		int x = 0, y = 0;

		// part 2
		List<Tuple> santa_and_robot = new ArrayList<>();
		santa_and_robot.add(new Tuple(0, 0));
		int santa_x = 0, santa_y = 0;
		int robo_x = 0, robo_y = 0;


		int input_len = input.length();
		for (int i = 0; i < input_len; i++) {
			boolean containsCoords = false;
			// read in directions
			char dir = input.charAt(i);
			switch (dir) {
				// up
				case '^': {
					// part 1
					y++;
					// part 2
					if (i % 2 == 0) {
						santa_y++;
					} else {
						robo_y++;
					}
					break;
				}
				// right
				case '>': {
					// part 1
					x++;
					// part 2
					if (i % 2 == 0) {
						santa_x++;
					} else {
						robo_x++;
					}
					break;
				}
				// down
				case 'v': {
					// part 1
					y--;
					// part 2
					if (i % 2 == 0) {
						santa_y--;
					} else {
						robo_y--;
					}
					break;
				}
				// left
				case '<': {
					// part 1
					x--;
					// part 2
					if (i % 2 == 0) {
						santa_x--;
					} else {
						robo_x--;
					}
					break;
				}
			}
			// part 1
			// check for x and y inside of the list
			for (int j = 0; j < xy_coords.size(); j++) {
				if (xy_coords.get(j).containsCoords(x, y)) {
					containsCoords = true;
					break;
				}
			}
			if (!containsCoords) {
				xy_coords.add(new Tuple(x, y));
			}

			// part 2
			containsCoords = false;	
			// check for santa_x/y or robo_x/y in respective lists
			for (int j = 0; j < santa_and_robot.size(); j++) {
				if (i % 2 == 0) {
					if (santa_and_robot.get(j).containsCoords(santa_x, santa_y)) {
						containsCoords = true;
						break;
					}
				} else {
					if (santa_and_robot.get(j).containsCoords(robo_x, robo_y)) {
						containsCoords = true;
						break;
					}
				}
			}
			if (!containsCoords) {
				if (i % 2 == 0) {	
					santa_and_robot.add(new Tuple(santa_x, santa_y));
				} else {
					santa_and_robot.add(new Tuple(robo_x, robo_y));
				}
			}

		}

		ret_arr[0] = xy_coords.size();
		ret_arr[1] = santa_and_robot.size();

		return ret_arr;
	}

	public static void main(String[] args)
	{
		// new class instance
		DayThree d3 = new DayThree();
		// handle input
		try {
			String filename = "input-files/day-three-input.txt";
			Scanner sc = new Scanner(new File(filename));
			String input = sc.nextLine();
			int[] ret_arr = d3.solution(input);
			System.out.println("Houses visited " + ret_arr[0]);
			System.out.println("Santa houses + robo houses visited: " + ret_arr[1]);
			sc.close();
		} catch (FileNotFoundException e) {}
	}
}