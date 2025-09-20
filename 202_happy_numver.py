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

num = 19 
for j in range(5):
    sum=0
    for i in (str(num)):
        i=int(i)
        val=i*i
        sum+=val
    num=sum
    if sum==1:
        return True
    else:
        return False
    print(sum)