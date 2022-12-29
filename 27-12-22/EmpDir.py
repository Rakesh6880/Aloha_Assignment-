class Employee:
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
        return x,self.id


lst = [["ID","Name","Gender","City","Salary"]]
ids=[]
while True:
    n = int(input("\n\nEnter the options:\n"
                  "1:Add an Employee\n"
                  "2:Delete an Employee\n"
                  "3:Display Employee\n"
                  "4:Update Employee details\n"
                  "5:Search Employee\n"
                  "6:Exit\n"
                  "Your Choose:"))
    if n == 1:
        obj = Employee()
        obj.details()
        p,q=obj.employeedata()
        if q not in ids:
            ids+=[q]
            lst+=[p]
        else:
            print("\n\nEmployee ID already exist\n\n")
    elif n == 2:
        m=input("Enter the Employee ID:")
        for i in range(len(ids)):
            if ids[i]==m:
                s=lst.pop(i)
                j=lst[0]+s
                a = 0
                k = []
                while a != 5:
                    x = []
                    for i in range(len(j)):
                        x += [len(j[i][a])]
                    k += [max(x)]
                    a += 1
                k += [0]
                for i in range(len(j)):
                    for h in range(len(j[0])):
                        print(j[i][h] + ' ' * abs(len(j[i][h]) - k[h]), end='\t')
                    print()
                print("\n\n")
                break
        else:
            print("\n\nEmployee ID Does not exist\n\n")

    elif n == 3:
        a = 0
        k = []
        while a != 5:
            x = []
            for i in range(len(lst)):
                x += [len(lst[i][a])]
            k += [max(x)]
            a += 1
        k += [0]
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                print(lst[i][j] + ' ' * abs(len(lst[i][j]) - k[j]), end='\t')
            print()
        print("\n\n")
    elif n == 4:
        m = int(input("\nEnter the Employee ID:"))
        for i in range(len(lst)):
            if lst[i][0] == m:
                x = i
                break
        a = int(input("\nEnter the Choose:\n"
                      "1:Name\n"
                      "2:Gender\n"
                      "3:City\n"
                      "4:Salary\n"
                      "your Choose:"))

        v = input("\nEnter the Change:")
        lst[x][a] = v

    elif n==5:
        a=int(input("Enter the Employee ID:"))
        for i in range(len(lst)):
            if lst[i][0]==a:
                j=lst[0]+lst[i]
                break
        a = 0
        k = []
        while a != 5:
            x = []
            for i in range(len(lst)):
                x += [len(lst[i][a])]
            k += [max(x)]
            a += 1
        k += [0]
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                print(lst[i][j] + ' ' * abs(len(lst[i][j]) - k[j]), end='\t')
            print()
        print("\n\n")

    else:
        break




