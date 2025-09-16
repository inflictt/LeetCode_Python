num=[1,2,3]
def num_plus_one(num):
    #this n will the number extractted from the list num and then we will be adding to it ...
    n=0
    for i in num:
        n=n*10+i
    n+=1
    #empty list so we can again store the element and show back to user
    l=[]
    for i in str(n):
        l.append(int(i))#appending as in order to store the final output
    return l

print(num_plus_one(num))