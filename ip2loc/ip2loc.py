#!/usr/bin/env python3

'''
ip2loc.py
Input an IP address (like 2.16.219.255) and see what
country and city in the world it originated from.
(with some exceptions because the database
is a free version of the databases at https://www.ip2location.com/)
Author Michael Leidel (2019)
'''
import ipaddress
import sqlite3
import webbrowser
import sys

def dot2LongIP(ip_addr):
  return int(ipaddress.IPv4Address(ip_addr))

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
  return found

if len(sys.argv) > 1:
  ipv4 = sys.argv[1].strip()
else:
  ipv4 = input("enter ip ").strip()

target = dot2LongIP(ipv4)

conn = sqlite3.connect('ip2locationIPV4.db')

print("\n######################################")
print("######################################\n")
print ("ip: {} => {}".format(ipv4, target))

cursor = conn.execute("SELECT * FROM ip WHERE %s BETWEEN ip_from AND ip_to" % target)
for row in cursor:
  print ("     ip from = ", row[0])
  print ("       ip to = ", row[1])
  print ("country code = ", row[2])
  print ("country name = ", row[3])
  print (" region name = ", row[4])
  print ("   city name = ", row[5])
  print ("    latitude = ", row[6])
  print ("   longitude = ", row[7], "\n")

conn.close()

# search for reported attacks by this IP
if binary_search(ipv4):
  msg = "FOUND IN LIST OF KNOWN ATTACK IPs\n"
else:
  msg = "NOT FOUND IN ATTACKER LIST\n"

print(msg)

print("View more info on this IP address")
print("https://blackhat.directory/ip/{}".format(ipv4))
print()
print ("View approx location on map:")
print ("https://maps.google.com/?q={},{}".format(row[6], row[7]))
print()
print ("use ctrl-click to open in browser\n")

print("######################################")
print("######################################\n")

# webbrowser.open(...)
