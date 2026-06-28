class Solution(object):
    def longestConsecutive(self, nums):
        longestSequence = 0
        num_set = set(nums)
        # if num - 1 doesn't exist, it's a new sequence
        # then while num + 1 in set keep incrementing longestsequence
        for num in num_set:
            if num - 1 in num_set:
                continue # ignore and continue
            current_num = num + 1 # new sequence
            sequence = 1
            while current_num in num_set:
                sequence += 1
                current_num += 1
            longestSequence = max(longestSequence, sequence)
        return longestSequence

        