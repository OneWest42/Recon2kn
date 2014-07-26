#!/usr/bin/python
import os
import sys

def foldernode(line, order):
	"Create node.xml for each folder"
	nodeid = "100" + line.translate(None, ".")
	dir = line + "/node.xml"
	file = open(dir, "w")
	file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
	file.write("<node>\n")
	file.write("<version>6</version>\n")
	file.write("<dict>\n")
	file.write("  <key>expanded</key><true/>\n")
	file.write("  <key>title</key><string>")
	file.write(line)
	file.write("</string>\n")
	file.write("  <key>nodeid</key><string>")
	file.write(nodeid)
	file.write("</string>\n")
	file.write("  <key>modified_time</key><integer>1405349827</integer>\n")
	file.write("  <key>version</key><integer>6</integer>\n")
	file.write("  <key>content_type</key><string>application/x-notebook-dir</string>\n")
	file.write("  <key>created_time</key><integer>1405349827</integer>\n")
	file.write("  <key>info_sort_dir</key><integer>1</integer>\n")
	file.write("  <key>order</key><integer>")
	file.write(order)
	file.write("</integer>\n")
	file.write("  <key>info_sort</key><string>order</string>\n")
	file.write("</dict>\n")
	file.write("</node>\n")
	file.close()
	return

def notesnode(line):
	os.mkdir(line + "/notes")
	nnodeid = "110" + line.translate(None, ".")
	dir = line + "/notes/node.xml"
	nnodef = open(dir, "w")
	nnodef.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
	nnodef.write("<node>\n")
	nnodef.write("<version>6</version>\n")
	nnodef.write("<dict>\n")
	nnodef.write("  <key>title</key><string>")
	nnodef.write("Notes")
	nnodef.write("</string>\n")
	nnodef.write("  <key>nodeid</key><string>")
	nnodef.write(nodeid)
	nnodef.write("</string>\n")
	nnodef.write("  <key>modified_time</key><integer>1405349827</integer>\n")
	nnodef.write("  <key>version</key><integer>6</integer>\n")
	nnodef.write("  <key>content_type</key><string>text/xhtml+xml</string>\n")
	nnodef.write("  <key>created_time</key><integer>1405349827</integer>\n")
	nnodef.write("  <key>info_sort_dir</key><integer>1</integer>\n")
	nnodef.write("  <key>order</key><integer>0</integer>\n")
	nnodef.write("  <key>info_sort</key><string>order</string>\n")
	nnodef.write("</dict>\n")
	nnodef.write("</node>\n")
	nnodef.close()
	return

def notespage(line):
	npagef = open(line + "/notes/page.html", "w")
	npagef.write("<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" ")
	npagef.write("\"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">\n")
	npagef.write("<html xmlns=\"http://www.w3.org/1999/xhtml\"><body><br/>")
	npagef.write("Hostname: <br/>\n")
	npagef.write("Operating System: <br/>\n")
	npagef.write("Domain: <br/>\n")
	npagef.write("</body></html>\n")
	npagef.close()
	return

counter = 0
nodeid = ""
with open('IPList.txt') as data:
	iplist = (line.rstrip('\r\n') for line in data)
	for line in iplist:
		if line != '':
			counter += 1
			os.mkdir(line)
			order = str(counter)
			foldernode(line, order) #add counter
			notesnode(line)
			notespage(line)
	data.close()
print "Done"	
