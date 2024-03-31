#wAP to create a list of any specific size. Arrange all the elements in ascending order. Display list before and after sorting

n = int(input("Enter size of list: "))
l = []
for i in range(n):
    ele = int(input("Enter element: "))
    l.append(ele)
print("List before sorting:", l)
l.sort()
print("List after sorting:", l)