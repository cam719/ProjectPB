import math, sys


def getKey(keyfilen):
    with open(keyfilen, "r") as myfile:
            data = myfile.read().replace('\n','')   
            print "KEY = " + data 
    return data

def decrypt(num, d, n):
    #x^e % n = encyption of our decimal
    c = pow(num, d) % n
    return c

#reads encrypted integers into a list
def readFile(filename):
    with open(filename) as f:
        nums = [map(int, x.split()) for x in f if x.strip()]
    
    return nums

def writeFile(text, filename):
    f = open(filename, "w")
    f.write(text + '\n')
    f.close()

k = getKey(sys.argv[1])
list = k.split(",")
print list[1]
d = int(list[0])
n = int(list[1])
enc_num = []

p = decrypt(19292, d, n)
print p
plain_text = ""
data = readFile(sys.argv[2])

print data

#decrypt every value in our 2D array and append to a string
for i in range(len(data)):
    for j in range(len(data[i])):
        plain_text += str(unichr(decrypt(data[i][j], d, n)))
        

writeFile(plain_text, "decr2.txt")
    