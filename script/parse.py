import sys

f=open("../urls/small_1000.txt", 'r')
count = 0
urls = {}
for line in f :
    urls[count] = line[:-1] # delete \n
    count += 1

f.close()



for line in sys.stdin :
    cols = line.split()
    if (cols[0] == "SCAN") or (cols[0] == "INSERT") :
        firstUrl = int(cols[2][4:]) % 1000
        if cols[0] == "SCAN" :
            numUrl = int(cols[3])
            lastUrl = (firstUrl + numUrl - 1) % 1000
            print cols[0], cols[1], urls[firstUrl], urls[lastUrl], numUrl
        else :
            print cols[0], cols[1], urls[firstUrl]

