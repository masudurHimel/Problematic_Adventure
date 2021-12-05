class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_list = {}
        temp_flag = 'x'
        for i in enumerate(nums):
            _ = temp_list.get(i[1], 'x')
            if _ != 'x':
                f = str(i[1]) + temp_flag
                temp_flag += 'x'
                temp_list[f] = i[0]
            else:
                temp_list[i[1]] = i[0]

        nums = sorted(nums)

        l = 0
        h = len(nums) - 1
        while l < h:
            if nums[l] + nums[h] > target:
                h -= 1
            elif nums[l] + nums[h] < target:
                l += 1
            elif nums[l] + nums[h] == target:
                if nums[l] == nums[h]:
                    _ = str(nums[h]) + 'x'
                    return [temp_list[nums[l]], temp_list[_]]
                return [temp_list[nums[l]], temp_list[nums[h]]]