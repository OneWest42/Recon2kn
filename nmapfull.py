#!/usr/bin/python
import os
import sys
import subprocess

ipaddr = sys.argv[1].strip()
smbfound = 0
snmpfound = 0
os.mkdir(ipaddr + "/NmapFullScan")

#Create node.xml for each nmap scan
nodeid = "112" + ipaddr.translate(None, ".")
nodef = open(ipaddr + "/NmapFullScan/node.xml", "w")
nodef.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
nodef.write("<node>\n")
nodef.write("<version>6</version>\n")
nodef.write("<dict>\n")
nodef.write("  <key>title</key><string>")
nodef.write("Nmap: Full Scan")
nodef.write("</string>\n")
nodef.write("  <key>nodeid</key><string>")
nodef.write(nodeid)
nodef.write("</string>\n")
nodef.write("  <key>modified_time</key><integer>1405349827</integer>\n")
nodef.write("  <key>version</key><integer>6</integer>\n")
nodef.write("  <key>content_type</key><string>text/xhtml+xml</string>\n")
nodef.write("  <key>created_time</key><integer>1405349827</integer>\n")
nodef.write("  <key>info_sort_dir</key><integer>1</integer>\n")
nodef.write("  <key>order</key><integer>3</integer>\n")
nodef.write("  <key>info_sort</key><string>order</string>\n")
nodef.write("</dict>\n")
nodef.write("</node>\n")
nodef.close()

#Create page.html with header for each nmap scan
pagef = open(ipaddr + "/NmapFullScan/page.html", "w")
pagef.write("<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" ")
pagef.write("\"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">\n")
pagef.write("<html xmlns=\"http://www.w3.org/1999/xhtml\">\n")
pagef.write("<head>\n")
pagef.write("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />\n")
pagef.write("<title>Nmap: Full Scan</title>\n")
pagef.write("</head><body><tt><span style=\"font-family: Sans\"><b>nmap -p* -sV ")
pagef.write(ipaddr)
pagef.write("</b><br/>\n")
pagef.write("</span></tt><span style=\"font-family: Sans\">\n")

#Run nmap, print out and write to page.html
print "--------------Nmap(Full Scan) started for %s-------------\n" % (ipaddr)
fullnmap = "nmap -p* -sV " + ipaddr
#print fullnmap
output = subprocess.check_output(fullnmap, shell=True)
lines = output.split("\n")
for line in lines:
 	print line
	port = ""
	line = line.replace(" ", " &nbsp;")
	line = line.replace("<", "&lt;")
	line = line.replace(">", "&gt;")
	pagef.write(line)
	pagef.write("<br/>\n")
	port = line.split('/')[0]
	ipandport = ipaddr + ":" + port + "\n"
	if "http" in line:
		if "open" in line: 
			httplist = open("HTTPList.txt", "a")
			httplist.write(ipandport)
			httplist.close()
			#print ipandport
	if "ftp" in line:
		if "open" in line:
			ftplist = open("FTPList.txt", "a")
			ftplist.write(ipandport)
			ftplist.close()
			#print ipandport
	if "netbios-ssn" in line:
		if "open" in line:
			if smbfound == 0:
				smblist = open("SMBList.txt", "a")
				smblist.write(ipaddr + "\n")
				smblist.close()
				#print ipandport
				smbfound = 1 #only write ip once
	if "snmp" in line:
		if "open" in line:
			if snmpfound == 0:
				snmplist = open("SNMPList.txt", "a")
				snmplist.write(ipaddr + "\n")
				snmplist.close()
				#print ipandport
				snmpfound = 1 #only write ip once
	

#Add footer to page.html
pagef.write("<tt><br/>\n<br/>\n</tt></span></body></html>")
pagef.close()

print "--------------Nmap(Full Scan) finished for %s------------\n" % (ipaddr)


		
