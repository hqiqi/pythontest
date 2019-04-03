import statistics
import sys

def average(ls):
    ls = list(ls)

    lr = []
    la = sorted(ls)

    mea = statistics.mean(ls)
    print ("The mean is: "+ str(mea))
    if (mea-la[0]) > (la[-1]-mea):
        lr = [ls.index(la[0]),la[0]]
    else:
        lr = [ls.index(la[-1]),la[-1]]
    return lr
lis = []
for element in sys.argv[1:]:
        lis.append(int(element))
arr = average(lis)
print (arr[0],arr[1])
