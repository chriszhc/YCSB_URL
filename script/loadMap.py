import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]

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
