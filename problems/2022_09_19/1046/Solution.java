class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> heap = new PriorityQueue<>(Comparator.reverseOrder());
        for (int stone : stones) {
            heap.offer(stone);
        }

        while (heap.size() > 1) {
            int stone1 = heap.poll();
            int stone2 = heap.poll();
            if (stone1 != stone2) {
                heap.offer(Math.abs(stone1 - stone2));
            }
        }

        return heap.peek() == null ? 0 : heap.peek();
    }
}