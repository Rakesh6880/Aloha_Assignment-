

# TwoSum
class TwoSum:
    def __init__(self, arr, target):
        self.arr = arr
        self.x = target

    def Twosum(self):
        for i in range(len(self.arr) - 1):
            for a in range(i, len(self.arr)):
                if self.arr[i] + self.arr[a] == self.x:
                    break
            break
        return [i, a]


arr = list(map(int, input().split()))
target = int(input())
ob = TwoSum(arr, target)
print(ob.Twosum())
