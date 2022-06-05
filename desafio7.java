import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int n = Integer.parseInt(in.nextLine());
        for (int i = 0; i < n; i++) {
            String username = in.nextLine();
            if (username.matches(MyRegex.pattern)) {
                System.out.println("Valid");
            } else {
                System.out.println("Invalid");
            }
        }
    }
    
    class MyRegex {
        public static final String pattern = "^[a-zA-Z][\\w]{7,29}$";
    }
}
