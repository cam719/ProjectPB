import math, sys
def getKey(keyfilen):
    with open(keyfilen, "r") as myfile:
            data = myfile.read().replace('\n','')   
            print "KEY = " + data 
    return data
    
def encrypt(num, e, n):
    #x^e % n = encyption of our decimal
    c = pow(num, e) % n
    return c

def readSentence(filename):
    with open(filename, "r") as myfile:
        data = myfile.read().replace('\n','')
    return data

def writeFile(enc_num,e,n, filename):
    f = open(filename, "w")
    #get space encrypted so we can print new line
    space =  encrypt(ord(" "), e, n)
    for i in range(len(enc_num)):
        if(enc_num[i] == space):
            f.write('\n' + str(enc_num[i]) + '\n')
        else:
            f.write(str(enc_num[i]) + " ")
    f.write("\n")
    f.close()
    
#encrypted list of ints
k = getKey(sys.argv[1])
list = k.split(",")
print list[1]
enc_num = []
n = int(list[1])
e = int(list[0])
encrypt(41, e, n)
data = readSentence(sys.argv[2])
data = data.strip('.')
print "DEBUG: DATE = " + data


#for every charac
for x in data:
    enc_num.append(encrypt(ord(x), e,n))
#test to print out enc_num list
for i in  range(len(enc_num)):
    print enc_num[i],
writeFile(enc_num, e, n, "o4.txt")