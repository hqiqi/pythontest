num = 1
line = ''
while num <= 99:
    if num%2 == 1:
        if num == 99:
            line += str(num)
            num+=1
        else:
            line += str(num) + ", "
            num+=1
    else:
        num+=1
print (line)