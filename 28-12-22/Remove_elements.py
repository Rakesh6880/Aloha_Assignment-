class Remove:
    def __init__(self, arr):
        self.a = arr

    def remove(self):
        res_arr = []
        for i in self.a:
            if i not in res_arr:
                res_arr += [i]
        return res_arr


n = list(map(int, input("Enter the Array Elements:").split()))
obj = Remove(n)
print(obj.remove())
