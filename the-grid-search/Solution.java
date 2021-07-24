import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){ // begin ath test case
            int R = in.nextInt();
            int C = in.nextInt();
            String G[] = new String[R]; // Grid
            for(int G_i=0; G_i < R; G_i++){
                G[G_i] = in.next();
            }
            int r = in.nextInt();
            int c = in.nextInt();
            String P[] = new String[r]; // Pattern
            for(int P_i=0; P_i < r; P_i++){
                P[P_i] = in.next();
            }

	    String result = ( solveCase(G, P, R, C, r, c) ) ? "YES" : "NO";	    
	    System.out.println(result);
        } // end ath test case
    }

    static boolean solveCase(String G[], String P[], int R, int C, int r, int c) {
	int counter = 0;       // # of integers matched
	int patternSize = r * c;
	boolean match = false; // true when counter == patternSize
	// iterate through the grid, looking for the pattern
	for (int G_j = 0; G_j < R; ++G_j) {
	    for (int G_i = 0; G_i < C; ++G_i) {
		// if the first integer of the pattern is encountered
		  if (G[G_j].charAt(G_i) == P[0].charAt(0)) {
		    // search for the rest of the pattern
		    for (int P_j = 0; P_j < r; ++P_j) {
			 for (int P_i = 0; P_i < c; ++P_i){
			    if (G[G_j + P_j].charAt(G_i + P_i) == P[P_j].charAt(P_i)) {
				    ++counter;
				    // if the pattern is found, return true
				    if (counter == patternSize) {
				        match = true;
				        return match;
				    }
			    } else { 
				    counter = 0;
				    break;
			    }   
			 }
			 // stop looking for the pattern if a mismatch is encountered
			 if (counter == 0) break;
		    }
		} else if ( (C - (G_i + 1)) < c) { // not enough columns remaining in this row of G
		    break;
		}
	    }
	    if ( (R - (G_j + 1)) < r) { // not enough rows remaining in G
		break;
	    }
	}
	// pattern was not found
	return match;
    }
}
