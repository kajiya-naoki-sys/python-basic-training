def sample(*a, b=1) :
    a_sum = 0
    for i in range(len(a)):
        a_sum += a[i]
    return b + a_sum

print(sample(1))        #2
print(sample(1,2))      #4
print(sample(1,2,3))    #7
