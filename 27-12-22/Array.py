"""Given two arrays a[] and b[] respectively of size n and m, the task is to print the count of elements in the intersection (or common elements) of the two arrays."""
# Intersection of array
class Intersection_of_array:
    def __init__(self,arr1,arr2):
        self.arr1=arr1
        self.arr2=arr2
    def Intersection(self):
        res_arr=self.arr1
        for i in range(len(self.arr2)):
            if self.arr2[i] not in res_arr:
                res_arr+=[self.arr2[i]]
        return res_arr
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
ob=Intersection_of_array(arr1,arr2)
a=ob.Intersection()
print(a)