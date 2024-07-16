class Solution:
    def countBits(self, n):
        nums = []
        binary = []
        num = []
        count = 0
        while n > count:
            nums.append(count)
            count += 1
        for i in nums:
            joined = 0
            if i ==0:
                num.append(0)
            elif i == 1:
                num.append(1)
            else:
                while i > 1:
                    if i % 2 == 1:
                        num.append(1)
                    elif i % 2 == 0:
                        num.append(0)
                for i in num:
                    joined += i
                binary.append(joined)
        return binary
    
test = Solution()
print(test.countBits(5))