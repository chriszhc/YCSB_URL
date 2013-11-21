YCSB_URL
========
Currently, this repo does not have any data file or itermmediate files, since those workloads depend on the specific
use of YCSB, and some data is too huge to fit in Git hub.

So, we have a sample raw urls store at 

1. 1 million randomly selected
https://dl.dropboxusercontent.com/u/14532517/large_urls_1M.txt

2. 2 million sequentially selected
https://dl.dropboxusercontent.com/u/14532517/seq_url_2M.dat

3. 4 million sequentialy selected
https://dl.dropboxusercontent.com/u/14532517/seq_urls_4M.dat

We REVERSE the hostnames in the above urls and store them here
1. https://www.dropbox.com/s/lxkrfj9o952a0uy/large_urls_1M.txt_reverse.txt
2. https://www.dropbox.com/s/h1tysgsxn23kzwh/seq_url_2M.dat_reverse.txt
3. https://www.dropbox.com/s/zlbqctey7zb7bea/seq_urls_4M.dat_reverse.txt

and you can download it, and put it into urls folder, change generate scripts, you are good to go :)
