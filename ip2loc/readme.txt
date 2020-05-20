About makebanned

Fail2ban process produces logs of jailed IP addresses that
have attempted to break into the server mostly via ssh.

Makebanned, a combination of shell commands, and two
python 3.? programs, uses Fail2ban logs to procude a file
called 'banned.csv'. This file describes the source information
for each of these IP addresses and whether or not they are already
know to be 'hostile' addresses (have a record of attacks.)

(getlists.py) downloads the ip lists
(banstrip.py) converts ban.txt to banned.txt 
(ip2locfile.py) produces banned.csv 

THESE WEBSITES PROVIDE THE HOSTILE IP LISTS
	THAT MAKE UP THE 'cips.txt' file:
		see getlists.py
