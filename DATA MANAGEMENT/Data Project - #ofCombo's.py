num = 4
sum1 =0
for x in range(13):
    die = [1,2,3,4,5,6]
    cards = [1,2]
    counter = 0
    for a in die:
        for b in die:
            for c in cards:
                for d in cards:
                    if (a+b+c+d == num):
                        print ("[",a,b,c,d,"]")
                        counter += 1
    num+=1
    print (counter)
    sum1 += counter
print (sum1)

    
