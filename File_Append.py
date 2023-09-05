#learn about append
import datetime

currentDT = datetime.datetime.now()
print (str(currentDT))

file=open("TryAppend.txt", 'a')
file.write((str(currentDT)+'\n'))
file.close()

with open("TryWrite.txt", "w") as writeFile:
    writeFile.write(str(currentDT)+"\n")


