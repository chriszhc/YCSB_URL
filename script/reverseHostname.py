# Author: Wenlu Hu

fn = "../urls/seq_urls_4M.dat"
fin = open(fn, 'r') 
fout = open(fn+"_reverse.txt", 'w')

for line in fin:
    # print line
    import string
    if line.startswith('http://'):
        line = line[7:]
    else:
        if line.startswith('https://'):
            line = line[8:]
        else:
            # discard anomaly lines
            print "ERROR! line: ", line
            continue
    '''
    i = string.find(line, 'http://')
    if i > -1:
        line = line[i+7:]
    else:
        i = string.find(line, 'https://')
        if i > -1:
            line = line[i+8:]
    '''
    # print '-', line

    hostname, sep, directory = line.partition('/')    
    # print hostname

    hnparts = hostname.split('.')
    # print hnparts
    
    r_hostname = ''
    for part in hnparts:
        r_hostname = part + '.' + r_hostname
    # remove the '.' at then end
    r_hostname = r_hostname[:-1]
    # print r_hostname

    res = r_hostname + sep + directory
    print res[:-1]
    fout.write(res)

fin.close()
fout.close()
print "Done!"
