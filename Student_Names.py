s = open('StudentNames.txt', 'r')
tmp=s.readline().rstrip('\n')
print(tmp)
count=1
while(tmp!=""):
    tmp=s.readline().rstrip('\n')
    print(tmp)
    count+=1
print(count)
s.close()