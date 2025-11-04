numBottles = 15
numExchange = 4
sum=numBottles
while True:
    full = numBottles//numExchange#3full , 
    empty = (numBottles%numExchange)+full #3empty now+3full now =6empt=6//4=
    sum=sum+full
    numBottles=empty
    if numBottles<numExchange:
        break
print(sum)