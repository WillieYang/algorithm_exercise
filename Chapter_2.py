List = [3, 2, 5, 9, 7, 4, 20]
Min = 8
for i in List:
    print('i is %d' % i)
    for j in List:
        print('j is %d' % j)
        if j < Min:
            Min = j
            print('Min is %d' % Min)
print('The minimum number is: %d' % Min)