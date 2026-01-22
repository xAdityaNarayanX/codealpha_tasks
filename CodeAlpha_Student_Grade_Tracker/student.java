import java.util.ArrayList;
import java.util.Scanner;

public class student {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        ArrayList<String> names = new ArrayList<>();
        ArrayList<Integer> marks = new ArrayList<>();

        System.out.print("Enter number of students: ");
        int n = sc.nextInt();

        
        for (int i = 0; i < n; i++) {
            System.out.print("\nEnter student name: ");
            names.add(sc.next());

            System.out.print("Enter marks: ");
            marks.add(sc.nextInt());
        }

        int total = 0;
        int highest = marks.get(0);
        int lowest = marks.get(0);

        
        for (int m : marks) {
            total += m;

            if (m > highest)
                highest = m;

            if (m < lowest)
                lowest = m;
        }

        double average = (double) total / n;

        
        System.out.println("\n----- Student Summary Report -----");
        for (int i = 0; i < n; i++) {
            System.out.println(names.get(i) + " : " + marks.get(i));
        }

        System.out.println("\nAverage Marks: " + average);
        System.out.println("Highest Marks: " + highest);
        System.out.println("Lowest Marks: " + lowest);

        sc.close();
    }
}
