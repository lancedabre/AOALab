import java.util.*;

class Item {
    int weight, value;

    Item(int w, int v) {
        weight = w;
        value = v;
    }
}

public class FractionalKnapsack {

    static double getMaxValue(int capacity, Item[] arr) {
        // Sort by value-to-weight ratio (descending order)
        Arrays.sort(arr, (a, b) -> 
            Double.compare((double)b.value / b.weight, (double)a.value / a.weight)
        );

        double totalValue = 0.0;

        for (Item it : arr) {
            if (it.weight <= capacity) {
                // Take the whole item
                capacity -= it.weight;  // <-- you had capacity = it.weight (wrong)
                totalValue += it.value;
            } else {
                // Take the fraction of the item that fits
                totalValue += it.value * ((double)capacity / it.weight);
                break;
            }
        }

        return totalValue;
    }

    public static void main(String[] args) {
        int capacity = 50; // Knapsack capacity
        Item[] arr = {
            new Item(60, 100),
            new Item(100, 120),
            new Item(120, 240)
        };

        double maxValue = getMaxValue(capacity, arr);
        System.out.println("Maximum value in Knapsack = " + maxValue);
    }
}