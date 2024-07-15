nums = [1,3,14,2,17,4,3,6,15,2]
# rem = []
# for i in nums:
#     if i < 5:
#         rem.append(i)
# print(rem)
# for i in rem:
#     nums.remove(i)
# print(nums)

# nums = [1,3,14,2,17,4,3,6,15,2]
# i = 0
# while i < len(nums):
#     if nums[i] < 5:
#         nums.remove(nums[i])
#     else:
#         i += 1
# print(nums)

# nums = [1,3,14,2,17,4,3,6,15,2]
# for i in nums[-1::-1]:
#     if i < 5:
#         nums.remove(i)
# print(nums)

# nums = [1,3,14,2,17,4,3,6,15,2]
# for i in nums:
#     if i < 5:
#         nums.remove(i)
# print(nums)

num2 = nums.copy()
print(id(nums))
print(id(num2))
print(num2)

for i in nums[:]:
    if i < 5:
        nums.remove(i)
print(nums)

