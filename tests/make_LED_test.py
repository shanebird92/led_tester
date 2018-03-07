
N=10
list2D = [ [0]*N for _ in range (N) ]

a1 = 4
b1 = 9
a2 = 4
b2 = 9

for i in range (a1, b1 + 1):
    for j in range (a2, b2 + 1):
        list2D[i][j]=1
print(list2D)
print(sum(sum(x) for x in list2D))
