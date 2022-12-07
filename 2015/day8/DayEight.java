import java.util.*;
import java.io.*;

public class DayEight {

    public int[] solution(List<String> input) {
        int numCharsTot = 0; // part 1 and 2
        int strCharsTot = 0; // part 1 only
        int newStrCharsTot = 0; // part 2 only
        int input_size = input.size();

        for (int i = 0; i < input_size; i++) {
            String str = input.get(i);
            int str_len = str.length();
            numCharsTot += str_len;

            // for loop not including first or last chars - PART 1
            for (int j = 1; j < str_len-1; j++) {
                if (str.charAt(j) == '\\') {
                    j++;
                    switch (str.charAt(j)) {
                        case 'x': {
                            strCharsTot++;
                            j+=2;
                            break;
                        }
                        default: {
                            strCharsTot++;
                            break;
                        }
                    }
                } else {
                    strCharsTot++;
                }
            }

            // for loop to encode a new string - PART 2
            newStrCharsTot += 2; // for outer quotes
            for (int j = 0; j < str_len; j++) {
                newStrCharsTot++;
                switch (str.charAt(j)) {
                    case '\"': {
                        newStrCharsTot++;
                        break;
                    }
                    case '\\':{
                        newStrCharsTot++;
                        break;
                    }
                }
            }   
        }

        // return int arr [ part1 , part2 ]
        int[] ret = new int[2];
        ret[0] = numCharsTot - strCharsTot;
        ret[1] = newStrCharsTot - numCharsTot;

        return ret;
    }
    public static void main(String[] args) {
        // instantiate the class
        DayEight d8 = new DayEight();

        // read in input from the file
        try {
            List<String> input = new ArrayList<>();
            String filename = "input-files/day-eight-input.txt";
            Scanner sc = new Scanner(new File(filename));
            while (sc.hasNextLine()) {
                input.add(sc.nextLine());
            }
            int[] sol = d8.solution(input);
            System.out.println("Characters - string chars = " + sol[0]);
            System.out.println("New encoded chars - Characters = " + sol[1]);
            sc.close();
        } catch (FileNotFoundException e) {}
    }
}