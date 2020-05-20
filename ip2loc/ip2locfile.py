#!/usr/bin/env python3

'''
ip2locfile.py
Michael Leidel (2020)
Run fail2ban on your web server.
fail2ban creates a log file called /var/log/fail2ban.log
pull out the "Ban" IPs with:
  zgrep ' Ban ' /var/log/fail2ban.log*
  creating a file called ban.txt
Then run banstrip.py to create a file of just IP address's
This program uses these IP addresses and the ip2locationIPV4.db
to create a csv of information about the IPs.
'''
import ipaddress
import sqlite3
import sys


def dot2LongIP(ip_addr):
  return int(ipaddress.IPv4Address(ip_addr))

def q(s):
  return "'" + s + "'"

with open("cips.txt", 'r') as f:
    lst = f.read().splitlines()

def binary_search(item):
  first = 0
  last = len(lst)-1
  found = False
  while( first<=last and not found):
    mid = (first + last)//2
    if lst[mid] == item :
      found = True
    else:
      if item < lst[mid]:
        last = mid - 1
      else:
        first = mid + 1
  if found:
    return "YES"
  else:
    return "NO"

conn = sqlite3.connect('ip2locationIPV4.db')
oo = open("banned.csv", "w")
oo.write("IP,CODE,NAME,REGION,CITY,LAT,LON,KNOWN\n")

with open("banned.txt") as fin:
  for ip in fin:
    ip = ip.strip()
    target = dot2LongIP(ip)
    cursor = conn.execute("SELECT * FROM ip WHERE %s BETWEEN ip_from AND ip_to" % target)
    for row in cursor:
      oo.write(ip + ",")
      oo.write(row[2] + ",")
      oo.write(q(row[3]) + ",")
      oo.write(q(row[4]) + ",")
      oo.write(q(row[5]) + ",")
      oo.write(row[6] + ",")
      oo.write(row[7] + "," + binary_search(ip) + "\n")
      print("               " + "\r", end="")
      print(ip + "\r", end="")

conn.close()
oo.close()
