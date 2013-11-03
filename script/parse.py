import sys

num_urls = 1000

f=open("../input.txt", 'r')
count = 0
urls = {}
for line in f :
    urls[count] = line[:-1] # delete \n
    count += 1

f.close()



for line in sys.stdin :
    cols = line.split()
    if (cols[0] == "SCAN") or (cols[0] == "INSERT") :
        firstUrl = int(cols[2][4:]) % num_urls
        if cols[0] == "SCAN" :
            numUrl = int(cols[3])
            lastUrl = (firstUrl + numUrl - 1) % num_urls
            print cols[0], urls[firstUrl], urls[lastUrl], numUrl
        else :
            print cols[0], urls[firstUrl]
#
