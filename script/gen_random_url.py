# argv[1]: url list
# argv[2]: url sample size

import sys

url_sample_size = int(sys.argv[2])

f_urls = open (sys.argv[1], 'r')
count = 0
total_count = 0
for line in f_urls :
    count += 1
    if count == 100 :
        print line.strip()
        count = 0
        total_count += 1
    if total_count >= url_sample_size :
        break
