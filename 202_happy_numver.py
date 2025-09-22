# #happy number
# eg=19
# sum1=0
# for i in (str(eg)):
#     i=int(i)
#     val=i*i
#     sum1+=val
# print(sum1)
# sum2=0
# for i in (str(sum1)):
#     i=int(i)
#     val=i*i
#     sum2+=val
# print(sum2)
# sum3=0
# for i in (str(sum2)):
#     i=int(i)
#     val=i*i
#     sum3+=val
# print(sum3)
# sum4=0
# for i in (str(sum3)):
#     i=int(i)
#     val=i*i
#     sum4+=val
# print(sum4)
# if sum4==1:
#     print(f"{eg} is an happy number as it ends down to 1 only")
# else:print(f"{eg} is not a happy number")

def sumofsquare(n):
    output=0
    while n:
        digit=n%10#takes n and give the remainder which is the right most number
        digit=digit**2#then the number is being squared 
        output+=digit#and then it get added to a output variable
        n=n//10#and before again getting out of the loop the number floor divided in order to remove the number which was being squared 
    return output
def mainfun(n):
    visit=set()#creating a set for thhis or a hashmap as in to check we have seen or visited the number before hand or not
    while n not in visit:
        visit.add(n)#if not visited by us then we add it to our set
        n=sumofsquare(n)#usng a helper function in order to give the sum of square of the number 
        if n==1:#and upon getting the final n we check its value for the happy number condition 
            return True
    return False
n=19
check=mainfun(n)
print(check)