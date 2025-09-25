import java.util.*;

public class KruskalMST {

    // Edge class
    static class Edge implements Comparable<Edge> {
        int src, dest, weight;

        Edge(int s, int d, int w) {
            src = s;
            dest = d;
            weight = w;
        }

        public int compareTo(Edge other) {
            return this.weight - other.weight;
        }
    }

    // Disjoint Set (Union-Find) for cycle detection
    static class DisjointSet {
        int[] parent, rank;

        DisjointSet(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }

        int find(int x) {
            if (parent[x] != x)
                parent[x] = find(parent[x]);
            return parent[x];
        }

        void union(int x, int y) {
            int rootX = find(x), rootY = find(y);
            if (rootX == rootY) return;

            if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }

    // Kruskal's MST function
    static void kruskalMST(int V, List<Edge> edges) {
        Collections.sort(edges); // sort edges by weight
        DisjointSet ds = new DisjointSet(V);

        int mstWeight = 0;
        System.out.println("Edges in Kruskal's MST:");

        for (Edge e : edges) {
            if (ds.find(e.src) != ds.find(e.dest)) {
                ds.union(e.src, e.dest);
                mstWeight += e.weight;
                System.out.println(e.src + " - " + e.dest + " : " + e.weight);
            }
        }

        System.out.println("Total weight of MST = " + mstWeight);
    }

    public static void main(String[] args) {
        int V = 4; // number of vertices
        List<Edge> edges = new ArrayList<>();

        // Example graph
        edges.add(new Edge(0, 1, 10));
        edges.add(new Edge(0, 2, 6));
        edges.add(new Edge(0, 3, 5));
        edges.add(new Edge(1, 3, 15));
        edges.add(new Edge(2, 3, 4));

        kruskalMST(V, edges);
    }
}