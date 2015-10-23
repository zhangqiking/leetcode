def capacity(up,down,h):
    return 0.5*(up+down)*h

def most_water(array):
    length=len(array)
    max_water=0
    ID=[]
    for i in range(length-1):
        for j in range(i+1,length):
            h=j-i
            temp=capacity(array[i],array[j],h)
            if (temp>max_water):
                max_water=temp
                ID=[i+1,j+1]
    print max_water
    print ID

most_water([2,4,6,8,2,1,3])









