import sys

inputURL = sys.argv[1]
inputLoad = sys.argv[2]
inputTxn = sys.argv[3]
outputLoad = sys.argv[4]
outputTxn = sys.argv[5]

try:
    urls = open(inputFile, 'r')
    url_list = urls.readlines();
    urls.close()
    
    int_url_map = open(outputFile, 'w')
except IOError, e:
    print 'Cannot open file'
    print e.strerror

for url in url_list:
    int_url_map.write(str(url_list.index(url)))
    int_url_map.write(url)
