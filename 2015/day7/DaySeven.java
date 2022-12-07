import java.util.*;
import java.io.*;

public class DaySeven {
	public boolean isAlpha(String name) {
	    char[] chars = name.toCharArray();

	    for (char c : chars) {
	        if(!Character.isLetter(c)) {
	            return false;
	        }
	    }

	    return true;
	}

	public int solution_part2(List<String> input, int a_signal) {
		int instructions = input.size();

		HashMap<String, Integer> signals = new HashMap<String, Integer>();
		signals.put("b", a_signal);
		while (!signals.containsKey("a")) {
			for (int i = 0; i < instructions; i++) {
				// overwriting B
				signals.put("b", a_signal);
				// starts with:
				//  -> lowercase letters (signal)
				//  -> number (value to a signal)
				//  -> NOT instruction
				// conditions:
				//	-> if '->', assign value in front of '->' to next value
				//	-> if upper case letters, read instruction
				//		-> after instruction, read in either another signal or number
				String[] inst_str = input.get(i).split(" ");
				int len = inst_str.length;
				switch (len) {
					// assignment
					case 3: {
						if (isAlpha(inst_str[0]) && signals.containsKey(inst_str[0])) {
							signals.put(inst_str[2], signals.get(inst_str[0]));
						} else if (!isAlpha(inst_str[0])) {
							signals.put(inst_str[2], Integer.parseInt(inst_str[0]));
						}
						break;
					}
					// NOT operation
					case 4: {
						if (!isAlpha(inst_str[1])) {
							signals.put(inst_str[3], ~(Integer.parseInt(inst_str[1])));
						} else if (isAlpha(inst_str[1]) && signals.containsKey(inst_str[1])) {
							signals.put(inst_str[3], ~(signals.get(inst_str[1])));
						}
						break;
					}
					// Other operation
					case 5: {
						int first, second;
						String op = inst_str[1];
						if (isAlpha(inst_str[0]) && signals.containsKey(inst_str[0])) {
							first = signals.get(inst_str[0]);
						} else if (!isAlpha(inst_str[0])) {
							first = Integer.parseInt(inst_str[0]);
						} else {
							break;
						}
						if (isAlpha(inst_str[2]) && signals.containsKey(inst_str[2])) {
							second = signals.get(inst_str[2]);
						} else if (!isAlpha(inst_str[2])) {
							second = Integer.parseInt(inst_str[2]);
						} else {
							break;
						}
						
						// operations
						switch (op) {
							case "AND": {
								signals.put(inst_str[4], first & second);
								break;
							}
							case "OR": {
								signals.put(inst_str[4], first | second);
								break;
							}
							case "LSHIFT": {
								signals.put(inst_str[4], first << second);
								break;
							}
							case "RSHIFT": {
								signals.put(inst_str[4], first >> second);
								break;
							}
						}
						break;
					}
				}
			}
		}
		System.out.println(signals);
		return signals.get("a");
	}

	public int solution_part1(List<String> input) {
		int instructions = input.size();

		HashMap<String, Integer> signals = new HashMap<String, Integer>();
		while (!signals.containsKey("a")) {
			for (int i = 0; i < instructions; i++) {
				// starts with:
				//  -> lowercase letters (signal)
				//  -> number (value to a signal)
				//  -> NOT instruction
				// conditions:
				//	-> if '->', assign value in front of '->' to next value
				//	-> if upper case letters, read instruction
				//		-> after instruction, read in either another signal or number
				String[] inst_str = input.get(i).split(" ");
				int len = inst_str.length;
				switch (len) {
					// assignment
					case 3: {
						if (isAlpha(inst_str[0]) && signals.containsKey(inst_str[0])) {
							signals.put(inst_str[2], signals.get(inst_str[0]));
						} else if (!isAlpha(inst_str[0])) {
							signals.put(inst_str[2], Integer.parseInt(inst_str[0]));
						}
						break;
					}
					// NOT operation
					case 4: {
						if (!isAlpha(inst_str[1])) {
							signals.put(inst_str[3], ~(Integer.parseInt(inst_str[1])));
						} else if (isAlpha(inst_str[1]) && signals.containsKey(inst_str[1])) {
							signals.put(inst_str[3], ~(signals.get(inst_str[1])));
						}
						break;
					}
					// Other operation
					case 5: {
						int first, second;
						String op = inst_str[1];
						if (isAlpha(inst_str[0]) && signals.containsKey(inst_str[0])) {
							first = signals.get(inst_str[0]);
						} else if (!isAlpha(inst_str[0])) {
							first = Integer.parseInt(inst_str[0]);
						} else {
							break;
						}
						if (isAlpha(inst_str[2]) && signals.containsKey(inst_str[2])) {
							second = signals.get(inst_str[2]);
						} else if (!isAlpha(inst_str[2])) {
							second = Integer.parseInt(inst_str[2]);
						} else {
							break;
						}
						
						// operations
						switch (op) {
							case "AND": {
								signals.put(inst_str[4], first & second);
								break;
							}
							case "OR": {
								signals.put(inst_str[4], first | second);
								break;
							}
							case "LSHIFT": {
								signals.put(inst_str[4], first << second);
								break;
							}
							case "RSHIFT": {
								signals.put(inst_str[4], first >> second);
								break;
							}
						}
						break;
					}
				}
			}
		}
		System.out.println(signals);
		return signals.get("a");
	}

	public static void main(String[] args) {
		// initialize new class
		DaySeven d7 = new DaySeven();

		// read input
		try {
			String filename = "input-files/day-seven-input.txt";
			Scanner sc = new Scanner(new File(filename));
			// input string array
			List<String> input = new ArrayList<>();
			while (sc.hasNextLine()) {
				input.add(sc.nextLine());
			}
			int a_signal = d7.solution_part1(input);
			System.out.println("The final signal of 'a' was: " + a_signal);

			a_signal = d7.solution_part2(input, a_signal);
			System.out.println("The final signal of 'a' was: " + a_signal);
			sc.close();
		} catch (FileNotFoundException e){}
	}
}