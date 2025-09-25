import java.util.*;

public class Main {

    // Job structure
    static class Job {
        char id;      // Job ID
        int deadline; // Deadline of job
        int profit;   // Profit if job is completed before deadline

        Job(char id, int deadline, int profit) {
            this.id = id;
            this.deadline = deadline;
            this.profit = profit;
        }
    }

    // Function to schedule jobs to maximize profit
    static void jobScheduling(Job[] jobs, int n) {
        // Sort jobs by descending profit
        Arrays.sort(jobs, (a, b) -> b.profit - a.profit);

        // Find maximum deadline
        int maxDeadline = 0;
        for (Job job : jobs) {
            maxDeadline = Math.max(maxDeadline, job.deadline);
        }

        // Result slots
        char[] result = new char[maxDeadline];
        Arrays.fill(result, '-'); // initially empty
        boolean[] slot = new boolean[maxDeadline]; // occupied slots

        int totalProfit = 0;

        // Place jobs greedily
        for (Job job : jobs) {
            // Find a free slot from job.deadline - 1 backwards
            for (int j = Math.min(maxDeadline, job.deadline) - 1; j >= 0; j--) {
                if (!slot[j]) {
                    slot[j] = true;
                    result[j] = job.id;
                    totalProfit += job.profit;
                    break;
                }
            }
        }

        // Print scheduled jobs
        System.out.print("Job sequence: ");
        for (char c : result) {
            if (c != '-') System.out.print(c + " ");
        }
        System.out.println("\nTotal Profit: " + totalProfit);
    }

    public static void main(String[] args) {
        Job[] jobs = {
            new Job('A', 2, 100),
            new Job('B', 1, 19),
            new Job('C', 2, 27),
            new Job('D', 1, 25),
            new Job('E', 3, 15)
        };

        int n = jobs.length;
        jobScheduling(jobs, n);
    }
}