import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.lang.*; // Math.pow
import java.util.*; // Vector

/* 
 * This solution only works for numbers smaller than 2^31 - 1
 */


public class Solution {
    // Rule 1: digits can only be 3's and/or 5's
    // Rule 2: # of 3's it contains is divisible by 5
    // Rule 3: # of 5's it contains is divisible by 3
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();           
            
            System.out.println("===== TEST CASE " + a0 + " =====");
            // get the n-digit number consisting of all 5's
            int maxNumber = 0;
            for (int i = 0; i < n; ++i) {
                maxNumber += 5 * Math.pow(10, i);                
            }
            System.out.println("maxNumber: " + maxNumber);
                        
            /* BINARYNUMBER              
             * will store radix 10 integers mimicking binary (1, 10, 11, 100, 101, 111...) throughout the iteration
             * this number will be multiplied by 2, and subtracted from maxNumber to turn 5's into 3's 
             * Example: 555 - (1*2) = 553; 555 - (10*2) = 535; ... ; 555 - (111 * 2) = 333
             */
            int binaryNumber; 
            int testNumber; // will store numbers to test under Rules 2 & 3
            boolean foundNumber = false; // becomes true if the a number exists that meets all the rules
            // iterate through each possible number with n digits that conforms to Rule 1
            for (int i = 0; i < Math.pow(2, n); ++i) {
                binaryNumber = Integer.parseInt( Integer.toBinaryString(i) );
                System.out.println("binaryNumber: " + binaryNumber);
                testNumber = maxNumber - binaryNumber * 2;
                System.out.println("testNumber: " + testNumber);
                // if the number meets Rule 2, and Rule 3
                if (getDigitCount(testNumber, 5) % 3 == 0 && getDigitCount(testNumber, 3) % 5 == 0) {
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
    // returns the number of occurences of n in intToSearch
    private static int getDigitCount(int intToSearch, int n) {
        int count = 0;
        Vector digits = toDigitVector(intToSearch);
        for (int i = 0; i < digits.size(); ++i) {
            if ( digits.get(i) == n )
                ++count;             
        }
        System.out.println("Number of " + n + "'s " + count);
        return count;
    }
    
    // helper method to getDigitCount
    // converts an integer, n, into an int vector whose elements are the digits of n
    private static Vector toDigitVector(int n) {
        Vector digits = new Vector();
        while (n != 0) {           
            // add the last digit to the first index of digits; subsequent adds shift elements to the right
            // this way the Vector isn't created in reverse order
            digits.add(0, n % 10); 
            n /= 10; // truncate the last digit 
        }
        return digits;
    }
}

