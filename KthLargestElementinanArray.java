import java.util.Random;

class Solution {
    public int findKthLargest(int[] nums, int k) {
        int n = nums.length;
        // Kth largest is (n - k)th smallest in sorted order
        return quickSelect(nums, 0, n - 1, n - k);
    }

    private int quickSelect(int[] nums, int left, int right, int k_smallest) {
        if (left == right) {
            return nums[left];
        }

        Random random = new Random();
        int pivotIndex = left + random.nextInt(right - left + 1);

        pivotIndex = partition(nums, left, right, pivotIndex);

        if (k_smallest == pivotIndex) {
            return nums[k_smallest];
        } else if (k_smallest < pivotIndex) {
            return quickSelect(nums, left, pivotIndex - 1, k_smallest);
        } else {
            return quickSelect(nums, pivotIndex + 1, right, k_smallest);
        }
    }

    private int partition(int[] nums, int left, int right, int pivotIndex) {
        int pivot = nums[pivotIndex];
        swap(nums, pivotIndex, right);  // Move pivot to end
        int storeIndex = left;

        for (int i = left; i < right; i++) {
            if (nums[i] < pivot) {
                swap(nums, storeIndex, i);
                storeIndex++;
            }
        }

        swap(nums, storeIndex, right);  // Move pivot to its final place
        return storeIndex;
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}