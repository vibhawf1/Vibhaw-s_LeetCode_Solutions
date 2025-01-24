class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        str_nums = ""  # Equivalent to `string str` in C++
        n = len(nums)
        presum = []

        # Building the string representation of the numbers and prefix sums
        for num in nums:
            str_nums += str(num)
            presum.append(len(str_nums))

        count = 0
        seen_pairs = set()  # Equivalent to `set<pair<int, int>> st` in C++

        # First loop to check splits starting from the beginning
        for j in range(1, (n - 1) // 2 + 1):
            a = str_nums[:presum[j - 1]]
            b = str_nums[presum[j - 1]:presum[j + j - 1]]

            if a == b:
                seen_pairs.add((j, j))
                count += (n - (2 * j))

        # Second loop to check other splits
        for i in range(1, n):
            for j in range(1, (n - i) // 2 + 1):
                if (i, j) in seen_pairs:
                    break

                a = str_nums[presum[i - 1]:presum[i - 1 + j]]
                b = str_nums[presum[i + j - 1]:presum[i + j - 1 + j]]

                if a == b:
                    count += 1

        return count
