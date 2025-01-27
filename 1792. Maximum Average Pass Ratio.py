import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Calculate the potential gain in pass ratio for each class
        heap = [((p / t) - ((p + 1) / (t + 1)), p, t) for p, t in classes]
        heapq.heapify(heap)  # Use a min-heap to efficiently find the class with the max potential gain

        # Assign extra students one by one to maximize the overall gain
        for _ in range(extraStudents):
            _, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, ((p / t) - ((p + 1) / (t + 1)), p, t))  # Recalculate gain

        # Calculate the final average pass ratio
        return sum(p / t for _, p, t in heap) / len(classes)
