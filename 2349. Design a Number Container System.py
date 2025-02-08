import bisect

class NumberContainers:

    def __init__(self):
        self.index_to_num = {}  # Maps index to number
        self.num_to_indices = {}  # Maps number to a sorted list of indices

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_num:
            # Remove the index from the old number's list
            old_num = self.index_to_num[index]
            if old_num in self.num_to_indices:
                # Use bisect to find and remove the index efficiently
                idx_list = self.num_to_indices[old_num]
                pos = bisect.bisect_left(idx_list, index)
                if pos < len(idx_list) and idx_list[pos] == index:
                    idx_list.pop(pos)
                if not idx_list:
                    del self.num_to_indices[old_num]
        
        # Update the index to the new number
        self.index_to_num[index] = number
        
        # Add the index to the new number's list
        if number not in self.num_to_indices:
            self.num_to_indices[number] = []
        bisect.insort(self.num_to_indices[number], index)

    def find(self, number: int) -> int:
        if number in self.num_to_indices and self.num_to_indices[number]:
            return self.num_to_indices[number][0]
        return -1

        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
