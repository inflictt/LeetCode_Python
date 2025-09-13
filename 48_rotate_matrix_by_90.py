# rotate by 90 
#not an inplace solution but works fine 
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
r=len(matrix)
c=len(matrix[0])
#creating a new array to store 0 in start and then update later
t=[[0]*r for _ in range(c)]
for i in range(r):
    for j in range(c):
        #base case for transpose
        t[j][i]=matrix[i][j]
        #reversing the transposed array in order to get the final output
for i in range(r):
    t[i].reverse()
print(t,end="")
print()

    