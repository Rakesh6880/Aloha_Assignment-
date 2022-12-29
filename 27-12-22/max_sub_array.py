class Array:
    def __init__(self, arr, subarrlen):
        self.a = arr
        self.l = subarrlen

    def max_arr(self):
        self.a.sort(reverse=True)
        x = []
        for i in range(self.l):
            x += [self.a[i]]
        return x


n = list(map(int, input("Enter the list:").split()))
m = int(input("Enter the length of sub Array:"))
if m >= len(n):
    print("Length of Sub Array should be less than length of given Array")
else:
    obj = Array(n, m)
    print(obj.max_arr())
