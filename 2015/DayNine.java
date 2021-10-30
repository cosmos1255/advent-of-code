import java.util.*;
import java.io.*;

public class DayNine {

    public int[][] parseInput(List<String> input, int numEdges) {
        // vertices ("iden", <pos (1-n)>)
        HashMap<String, Integer> verts = new HashMap<>();
        int vertCount = 0;

        List<String> start = new ArrayList<>();
        List<String> end = new ArrayList<>();
        int[] edge_len = new int[numEdges];
        for (int i = 0; i < numEdges; i++) {
            String[] input_str = input.get(i).split(" ");

            // get count of verts
            if (!verts.containsKey(input_str[0])) {
                verts.put(input_str[0], vertCount);
                vertCount++;
            }
            if (!verts.containsKey(input_str[2])) {
                verts.put(input_str[2], vertCount);
                vertCount++;
            }
            
            // fill out the following arrays
            start.add(input_str[0]);
            end.add(input_str[2]);
            edge_len[i] = Integer.parseInt(input_str[4]);
        }
        System.out.println(verts);  
        int[][] mat = new int[vertCount][vertCount];

        for (int i = 0; i < numEdges; i++) {
            int x = verts.get(start.get(i));
            int y = verts.get(end.get(i));
            mat[x][y] = edge_len[i];
            mat[y][x] = edge_len[i];
        }

        for (int i = 0; i < vertCount; i++) {
            for (int j = 0; j < vertCount; j++) {
                System.out.print(mat[i][j] + "\t");
            }
            System.out.println();
        }
        return mat;
    }
    public static void main(String[] args) {
        // new class
        DayNine d9 = new DayNine();

        // read in input
        try {
            String filename = "input-files/day-nine-input.txt";
            Scanner sc = new Scanner(new File(filename));

            // Read in lines of input to parse
            List<String> inputStrings = new ArrayList<>();
            while (sc.hasNextLine()) {
                inputStrings.add(sc.nextLine());
            }

            // parse input and return adjacency matrix
            int[][] mat = d9.parseInput(inputStrings, inputStrings.size());
            sc.close();
        } catch (FileNotFoundException e) {}
    }
}