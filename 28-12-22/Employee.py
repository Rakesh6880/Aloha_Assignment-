class ChooseOption:
    def __init__(self):
        self.n = 0

    def choose(self):
        lst = [["ID", "Name", "Gender", "City", "Salary"]]
        ids = ['ID']
        while True:
            self.n = int(input("\n\nEnter the options:\n"
                               "1:Add an Employee\n"
                               "2:Delete an Employee\n"
                               "3:Display Employee\n"
                               "4:Update Employee details\n"
                               "5:Search Employee\n"
                               "6:Exit\n"
                               "Your Choose:"))
            if self.n == 1:
                obj1 = EmployeeEntry()
                obj1.details()
                x, p = obj1.employeedata()
                lst += [x]
                ids += [p]
            elif self.n == 2:
                m = input("Enter the Employee ID:")
                obj1 = EmployeeDelete(ids, lst, m)
                obj1.display()
            elif self.n == 3:
                obj1 = EmployeeDisplay(lst)
                obj1.display()
            elif self.n == 4:
                m = input("Enter the Employee ID:")
                obj1 = EmployeeDetailsChange(lst, m)
                obj1.change()
            elif self.n == 5:
                m = input("Enter the Employee ID:")
                obj1 = EmployeeSearch(lst, m)
                obj1.search()
            elif self.n == 6:
                exit(0)
            else:
                print("Entered Invalid Input")


class EmployeeEntry:
    def __init__(self):
        self.id = ''
        self.name = ""
        self.gender = ""
        self.city = ""
        self.salary = ''

    def details(self):
        self.id = input("Enter the ID:")
        self.name = input("Enter the Name:")
        self.gender = input("Enter the Gender:")
        self.city = input("Enter the City:")
        self.salary = input("Enter the Salary:")

    def employeedata(self):
        x = [self.id, self.name, self.gender, self.city, self.salary]
        return x, self.id


class EmployeeDelete:
    def __init__(self, x, lst, id):
        self.x = x
        self.lst = lst
        self.id = id

    def display(self):
        for i in range(len(self.x)):
            if self.x[i] == self.id:
                s = self.lst.pop(i)
                j = [self.lst[0],s]
                obj2 = EmployeeDisplay(j)
                obj2.display()
                break
        else:
            print("\n\nEntered Input is Invalid\n\n")


class EmployeeDisplay:
    def __init__(self, lst):
        self.lst = lst

    def display(self):
        a = 0
        k = []
        while a != 5:
            x = []
            for i in range(len(self.lst)):
                x += [len(self.lst[i][a])]
            k += [max(x)]
            a += 1
        k += [0]
        for i in range(len(self.lst)):
            for j in range(len(self.lst[0])):
                print(self.lst[i][j] + ' ' * abs(len(self.lst[i][j]) - k[j]), end='\t')
            print()
        print("\n\n")


class EmployeeDetailsChange:
    def __init__(self, lst, id):
        self.lst = lst
        self.id = id

    def change(self):
        for i in range(len(self.lst)):
            if self.lst[i][0] == self.id:
                x=i
                break
        a = int(input("\nEnter the Choose:\n"
                      "1:Name\n"
                      "2:Gender\n"
                      "3:City\n"
                      "4:Salary\n"
                      "your Choose:"))
        v = input("\nEnter the Change:")
        self.lst[x][a] = v
        ob=EmployeeDisplay(self.lst)
        ob.display()


class EmployeeSearch:
    def __init__(self, lst, id):
        self.lst = lst
        self.id = id

    def search(self):
        for i in range(len(self.lst)):
            if self.lst[i][0] == self.id:
                j = [self.lst[0],self.lst[i]]
                break
        obj3 = EmployeeDisplay(j)
        obj3.display()


if __name__ == '__main__':
    obj = ChooseOption()
    obj.choose()
