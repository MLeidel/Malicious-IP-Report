#getlists.py
# downloads mal ip lists from two different sources
# formats and combines into one file (cips.txt)


import requests

url = 'https://iplists.firehol.org/files/iblocklist_ciarmy_malicious.netset'
res = requests.get(url)
if res.status_code != 200:
    print("error")
else:
    with open("mal.txt", "w") as f:
        f.write(res.text)

url = 'https://lists.blocklist.de/lists/all.txt'
res = requests.get(url)
if res.status_code != 200:
    print("error")
else:
    with open("deALL.txt", "w") as f:
        f.write(res.text)

''' Fix the firehol iblocklist file (mal.txt) '''
with open("mal.txt", 'r') as f:
    lst = f.read().splitlines()

oo = open("mal.txt", "w")
for ip in lst:
    if ip.startswith("#"):
        continue  # bypass comment lines
    if ":" in ip:
        print("found " + ip)
        continue  # bypass entries that are not actual IP addresses
    if "/" in ip:
        i = ip.split("/")
        ip = i[0]
    oo.write(ip + "\n")
oo.close()

lst.clear()

''' Fix the blocklist.de file (deALL.txt) '''
with open("deALL.txt", 'r') as f:
    lst = f.read().splitlines()

oo = open("deALL.txt", "w")
for ip in lst:
    if ":" in ip:
        # print("found " + ip)
        continue  # bypass entries that are not actual IP addresses
    oo.write(ip + "\n")
oo.close()

lst.clear()

# now combine the two files (lists)

with open('mal.txt', 'r') as f:
    lst1 = f.read().splitlines()

with open('deALL.txt', 'r') as f:
    lst2 = f.read().splitlines()

lst3 = lst1 + lst2

finlst3 = sorted(set(lst3))  # sort and dedup

with open('cips.txt', 'w') as f:
    f.write('\n'.join(finlst3) + '\n')
