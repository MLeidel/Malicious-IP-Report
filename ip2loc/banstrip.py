# banstrip.py
# Input: ban.txt
# Output: banned.txt
# Reads the output of "banned" ip's from fail2ban
# Run "banned" and produce a file called "ban.txt"
# This program extracts just the ip's
# sorts and dedups them.

slst = []

oo = open("banned.txt", "w")

with open("ban.txt") as f:
    for line in f:
        inx = line.rindex("Ban")
        sip = line[inx+4:].strip()
        slst.append(sip)

finlst = sorted(set(slst))  # sort and dedup

for ip in finlst:
    oo.write(ip + "\n")
    # print(ip)

# print("unique ip's = " + str(len(finlst)))
oo.close()
