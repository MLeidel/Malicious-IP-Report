If you happen to run a web server you can check your logs to find IP's from 
all over the world that are constantly at work trying to break in.  
Fail2ban software works with your server logs and firewall to automaticaly 
block (jail) repeated login attempts. Fail2ban keeps its own logs.

These programs and commands capture the Fail2ban log (ip) information to 
produce a spreadsheet file listing the ip, country, city, region, latitude, 
and longitude of these attackers. It also queries websites for lists of malicious 
ip addresses to compare to your captured Fail2ban ips.

Download the database file from https://lite.ip2location.com/file-download
Use the "csv" download that has the last columns as latitude and longitude.

ip2locfile.py uses sqlite. Create the table and columns like this:

CREATE TABLE "ip" ( `ip_from` INTEGER, `ip_to` INTEGER, `country_code` TEXT, `country_name` TEXT, `region_name` TEXT, `city_name` TEXT, `latitude` TEXT, `longitude` TEXT )

Then import the downloaded csv file using your favorite sqlite db manager or ...

related: 
https://sites.google.com/view/programtuto/linux-console/ip2location
https://www.fail2ban.org/wiki/index.php/MANUAL_0_8#Introduction
https://www.blocklist.de/en/index.html
http://iplists.firehol.org/?ipset=iblocklist_ciarmy_malicious


