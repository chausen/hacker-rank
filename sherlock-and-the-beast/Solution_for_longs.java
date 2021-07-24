import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.lang.*; // Math.pow
import java.util.*; // Vector

public class Solution {
    // Rule 1: digits can only be 3's and/or 5's
    // Rule 2: # of 3's it contains is divisible by 5
    // Rule 3: # of 5's it contains is divisible by 3
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();           
            
            // get the n-digit number consisting of all 5's
            long maxNumber = 0;
            for (int i = 0; i < n; ++i) {
                maxNumber += 5 * Math.pow(10, i);                
            }
                        
            /* BINARYNUMBER              
             * will store radix 10 integers mimicking binary (1, 10, 11, 100, 101, 111...) throughout the iteration
             * this number will be multiplied by 2, and subtracted from maxNumber to turn 5's into 3's 
             * Example: 555 - (1*2) = 553; 555 - (10*2) = 535; ... ; 555 - (111 * 2) = 333
             */
            long binaryNumber; 
            long testNumber; // will store numbers to test under Rules 2 & 3
            boolean foundNumber = false; // becomes true if the a number exists that meets all the rules
            // iterate through each possible number with n digits that conforms to Rule 1
            for (int i = 0; i < Math.pow(2, n); ++i) {
                binaryNumber = Long.parseLong( Long.toBinaryString(i) );                 
                testNumber = maxNumber - binaryNumber * 2;
                // if the number meets Rule 2, and Rule 3
                if (getDigitCount(testNumber, 5L) % 3 == 0 && getDigitCount(testNumber, 3L) % 5 == 0) {
                    foundNumber = true;
                    System.out.println(testNumber);
                    break; // no need to keep searching                    
                }
            }
            if (foundNumber != true) {
                System.out.println(-1);
            }
        }
    }
    // helper method to Solution
    // returns the number of occurences of n in longToSearch
    private static int getDigitCount(long longToSearch, long n) {
        int count = 0;
        Vector digits = toDigitVector(longToSearch);
        for (int i = 0; i < digits.size(); ++i) {
            if ( digits.get(i) == n )
                ++count;             
        }
        return count;
    }
    
    // helper method to getDigitCount
    // converts a long, n, into an long vector whose elements are the digits of n
    private static Vector toDigitVector(long n) {        
        Vector digits = new Vector();
        while (n != 0) {           
            // add the last digit to the first index of digits; subsequent adds shift elements to the right
            // this way the Vector isn't created in reverse order
            digits.add(0, n % 10L); 
            n /= 10L; // truncate the last digit 
        }    
        return digits;
    }
}
