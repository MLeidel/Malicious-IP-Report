If you happen to run a web server you can check your logs to find IP's from 
all over the world that are constantly at work trying to break in.  
Fail2ban software works with your server logs and firewall to automaticaly 
block (jail) repeated login attempts. Fail2ban keeps its own logs.

These programs and commands capture the Fail2ban log (ip) information to 
produce a spreadsheet file listing the ip, country, city, region, latitude, 
and longitude of these attackers. It also queries websites for lists of malicious 
ip addresses to compare to your captured Fail2ban ips.

Download the database file from https://lite.ip2location.com/file-download