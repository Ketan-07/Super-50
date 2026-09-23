
# 33. Count frequency of list elements

numbers = [1, 2, 2, 3, 3, 3]
freq = {}

for i in numbers:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

for i,j in freq.items():
    print(i,j,sep="  ->  ",end=" times \n")
