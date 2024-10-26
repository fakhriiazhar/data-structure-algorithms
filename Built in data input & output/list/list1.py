#list
Mylist = [1,3,True,6,5]
print(Mylist)
A = [Mylist]*3
print(A)
Mylist[2]=45
print(A)

Mylist_A = [1024, 3, True, 6.5]
Mylist_A.append(False)
print(Mylist_A)
Mylist_A.insert(2,4.5)
print(Mylist_A)
print(Mylist_A.pop())
print(Mylist_A)
print(Mylist_A.pop(1))
print(Mylist)
Mylist_A.pop(2)
print(Mylist_A)
Mylist_A.sort()
print(Mylist_A)
Mylist_A.reverse()
print(Mylist_A)
print(Mylist_A.count(6.5))
print(Mylist_A.index(4.5))
Mylist_A.remove(6.5)
print(Mylist_A)
del Mylist_A[0]
print(Mylist_A)
