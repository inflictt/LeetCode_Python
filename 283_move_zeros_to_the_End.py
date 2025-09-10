def moveZeroes(num):
    n = len(num)
    i = 0
    while i < n:   # we control i manually
        if num[i] == 0:
            del num[i]
            num.append(0)
            n -= 1   # length of useful part decreases
        else:
            i += 1   # only move forward if we didn't delete
    return num

num = [1,2,0,4,3,0,0,3,5,1]
ans = moveZeroes(num)
print(ans)   
