import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution_the_Second {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();

	    /* Observations:
	     * 1) If a number exists that meets the criteria, it must be of the form:
	     * 
	     * 5...3
	     *
	     * Where digits preceding the ellipsis are 5's, and numbers following the ellipsis are 3's.
	     * We are looking for the LARGEST number whose digits consist only of 5's and 3's; for 
	     * any number whose 5's & 3's intermingle, there is another number with the same counts
	     * for its 5's & 3's where the digits do not intermingle:
	     *
	     * 5353          |   5533
	     * # of 5's = 2  |   # of 5's = 2
	     * # of 3's = 2  |   # of 5's = 2
	     *
	     * Here it can be seen that the counts are the same, but 5533 > 5353
	     */

	    // i     = # of 5's
	    // n - i = # of 3's
	    boolean found = false;
	    for (int i = n; i >= 0; --i) {
		if ( (i % 3 == 0) && ((n - i) % 5 == 0) ) {
		    found = true;
		    for (int i5 = 0; i5 < i; ++i5) { System.out.print("5"); }
		    for (int i3 = 0; i3 < (n - i); ++i3) { System.out.print("3"); }
		    System.out.println(""); // newline
		    break;
		}

	    }
	    // if "A Decent Number" doesn't exist
	    if (!found) {
		System.out.println("-1");
	    }
        }
    }
}
