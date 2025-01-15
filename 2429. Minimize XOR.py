class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Count the number of 1s in the binary representation of num2
        target_ones = bin(num2).count("1")
        remaining_ones = target_ones
        binary_result = ""

        # Step 1: Build the binary result from the binary representation of num1
        for bit in bin(num1)[2:]:
            if bit == "1" and remaining_ones > 0:
                binary_result += "1"
                remaining_ones -= 1
            else:
                binary_result += "0"

        # Step 2: Add additional 1s to the least significant zero positions if needed
        if remaining_ones > 0:
            adjusted_result = ""
            for bit in reversed(binary_result):
                if bit == "0" and remaining_ones > 0:
                    adjusted_result = "1" + adjusted_result
                    remaining_ones -= 1
                else:
                    adjusted_result = bit + adjusted_result

            binary_result = adjusted_result

        # Step 3: If there are still ones left, append them to the result
        if remaining_ones > 0:
            binary_result += "1" * remaining_ones

        # Convert the binary result back to an integer
        return int(binary_result, 2)
