l1=[20,50,80,33]
l2=l1.copy()
l2[2]=56
print(l1)
print(l2)

# shoolow copy
import copy
l1=[55,88,97,[20,78],32,13]
l2=copy.copy(l1)
l1[3][1]=67
print(l1)
print(l2)


# deep copy
import copy
l1=[55,88,97,888,32,13]
l2=copy.deepcopy(l1)
l1[3]=4444
print(l1)
print(l2)