#!/usr/bin/python
import os
import sys
import subprocess

ipaddr = sys.argv[1].strip()
os.mkdir(ipaddr + "/SNMPEnum")

#Create node.xml for each snmpcheck
nodeid = "114" + ipaddr.translate(None, ".")
nodef = open(ipaddr + "/SNMPEnum/node.xml", "w")
nodef.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
nodef.write("<node>\n")
nodef.write("<version>6</version>\n")
nodef.write("<dict>\n")
nodef.write("  <key>title</key><string>")
nodef.write("SNMP Check")
nodef.write("</string>\n")
nodef.write("  <key>nodeid</key><string>")
nodef.write(nodeid)
nodef.write("</string>\n")
nodef.write("  <key>modified_time</key><integer>1405349827</integer>\n")
nodef.write("  <key>version</key><integer>6</integer>\n")
nodef.write("  <key>content_type</key><string>text/xhtml+xml</string>\n")
nodef.write("  <key>created_time</key><integer>1405349827</integer>\n")
nodef.write("  <key>info_sort_dir</key><integer>1</integer>\n")
nodef.write("  <key>order</key><integer>4</integer>\n")
nodef.write("  <key>info_sort</key><string>order</string>\n")
nodef.write("</dict>\n")
nodef.write("</node>\n")
nodef.close()

#Create page.html with header for each snmpcheck
pagef = open(ipaddr + "/SNMPEnum/page.html", "w")
pagef.write("<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" ")
pagef.write("\"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">\n")
pagef.write("<html xmlns=\"http://www.w3.org/1999/xhtml\">\n")
pagef.write("<head>\n")
pagef.write("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />\n")
pagef.write("<title>SNMP Check</title>\n")
pagef.write("</head><body><tt><span style=\"font-family: Sans\"><b>snmpcheck -t ")
pagef.write(ipaddr)
pagef.write("</b><br/>\n")
pagef.write("</span></tt><span style=\"font-family: Sans\">\n")

#Run nmap, print out and write to page.html
print "--------------SNMPCheck started for %s-------------------\n" % (ipaddr)
snmpenum = "snmpcheck -t " + ipaddr

output = subprocess.check_output(snmpenum, shell=True)
lines = output.split("\n")
for line in lines:
 	print line
	line = line.replace(" ", " &nbsp;")
	line = line.replace("<", "&lt;")
	line = line.replace(">", "&gt;")
	pagef.write(line)
	pagef.write("<br/>\n")
	
	
#Add footer to page.html
pagef.write("<tt><br/>\n<br/>\n</tt></span></body></html>")
pagef.close()

print "--------------SNMPCheck finished for %s------------------\n" % (ipaddr)


		
