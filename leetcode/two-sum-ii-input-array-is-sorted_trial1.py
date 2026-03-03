class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                 sums = numbers[i] + numbers[j]
                 if sums == target:
                    return [i+1, j+1]