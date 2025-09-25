import java.util.*;

public class PrimMST {
    static int V = 5; // number of vertices

    // Function to find the vertex with minimum key value
    static int minKey(int key[], boolean mstSet[]) {
        int min = Integer.MAX_VALUE, minIndex = -1;
        for (int v = 0; v < V; v++) {
            if (!mstSet[v] && key[v] < min) {
                min = key[v];
                minIndex = v;
            }
        }
        return minIndex;
    }

    // Print MST stored in parent[]
    static void printMST(int parent[], int graph[][]) {
        int totalCost = 0;
        System.out.println("Edges in Prim's MST:");
        for (int i = 1; i < V; i++) {
            System.out.println(parent[i] + " - " + i + " : " + graph[i][parent[i]]);
            totalCost += graph[i][parent[i]];
        }
        System.out.println("Total Minimum Cost (Prim) = " + totalCost);
    }

    // Function to construct MST
    static void primMST(int graph[][]) {
        int parent[] = new int[V];   // Array to store constructed MST
        int key[] = new int[V];      // Key values to pick minimum weight edge
        boolean mstSet[] = new boolean[V]; // To represent set of vertices included

        Arrays.fill(key, Integer.MAX_VALUE);
        key[0] = 0;   // Start from vertex 0
        parent[0] = -1;

        for (int count = 0; count < V - 1; count++) {
            int u = minKey(key, mstSet); // Pick the min key vertex
            mstSet[u] = true;

            for (int v = 0; v < V; v++) {
                if (graph[u][v] != 0 && !mstSet[v] && graph[u][v] < key[v]) {
                    parent[v] = u;
                    key[v] = graph[u][v];
                }
            }
        }

        printMST(parent, graph);
    }

    public static void main(String[] args) {
        // Example graph represented using adjacency matrix
        int graph[][] = {
            {0, 2, 0, 6, 0},
            {2, 0, 3, 8, 5},
            {0, 3, 0, 0, 7},
            {6, 8, 0, 0, 9},
            {0, 5, 7, 9, 0}
        };

        primMST(graph);
    }
}