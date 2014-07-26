#!/usr/bin/python 

#Title: recon2kn.py
#Author: W. Daniels (OneWest)
#Version: 1.0
#
#Desc:	This is a quick script I wrote up, as part of the OSCP course, 
#	to generate keepnote pages for initial network scans. It is loosely
#	based on reconscan.py by Mike Czumak (if you don't need the keepnote
#	pages I highly recommend his script) I'm not a programmer and make no
#	guarantees regarding functionality or anything else. The user accepts
#	all legal responsibility. You're welcome to redistribute or modify as you
#	see fit but please maintain original author attribution. If you have
#	any questions, comments, suggestions or want to talk security I'm usually
#	on the offsec chan. 
#
#Instructions:
#	1) BACKUP YOUR KEEPNOTE NOTEBOOK or create a new one
#	2) Copy the recon2kn files into your notebook's main folder
#	3) Add target IPs to IPList.txt (one per line)
#	4) Run recon2kn.py and follow the prompts
#	5) Reload notebook to see scan results (file > reload notebook)
#	Note: To use options 4-7 you first need to create target lists:
#      	      SNMPList.txt, SMBList.txt, FTPList.txt and HTTPList.txt.
#      	      You can do this manually or generate them with option 3.

import os
import sys
import subprocess

while True:
	
	print "---------------------------------------------------------------------"
	print "--------------------------Recon to Keepnote--------------------------"
	print "---------------------Author: W. Daniels (OneWest)--------------------"
	print "---------------------------------------------------------------------\n"
	print "***BACKUP YOUR KEEPNOTE NOTEBOOK or create a new one before running**"
	print "[1] Create folders and \"notes\" pages for each IP in IPList.txt"
	print "[2] Run quick nmap scans and output to keepnote"
	print "[3] Run full nmap scans, generate service lists and output to keepnote"
	print "[4] Run snmpcheck and output to keepnote (still WIP)"
	print "[5] Run enum4linux and output to keepnote"
	print "[6] Run ftp-anon.nse and output to keepnote"
	print "[7] Run nikto and output to keepnote (this is slow right now)"
	print "[8] Instructions"
	print "[9] Exit"
	
	selection = input("Selection: ")
	
	if selection == 1: #create folders
		execfile("ipfolders.py")
	
	elif selection == 2: #nmap quick scan
		target = str(raw_input("Target (blank to use IPList.txt): "))
		if target == '':
			with open('IPList.txt') as data:
				for line in data:
					if line != '':
						execute = "./nmapquick.py " + line
	                			subprocess.call(execute, shell=True)
			data.close()
	        elif target != '':
			execute = "./nmapquick.py " + target
	                subprocess.call(execute, shell=True)
	
	elif selection == 3: #nmap full scan
	        target = str(raw_input("Target (blank to use IPList.txt): "))
		if target == '':
	                with open('IPList.txt') as data:
	                	for line in data:
	                        	if line != '':
						execute = "./nmapfull.py " + line
	                			subprocess.call(execute, shell=True)
			data.close()
	        elif target != '':
			execute = "./nmapfull.py " + target
	                subprocess.call(execute, shell=True)	
	
	elif selection == 4: #snmpcheck
	        target = str(raw_input("Target (blank to use SNMPList.txt): "))
	        if target == '':
	                with open('SNMPList.txt') as data:
	                	for line in data:
					if line != '':
						execute = "./snmpenum.py " + line
	                			subprocess.call(execute, shell=True)
			data.close()
	        elif target != '':
			execute = "./snmpenum.py " + target
	                subprocess.call(execute, shell=True)
	
	elif selection == 5: #enum4linux
	        target = str(raw_input("Target (blank to use SMBList.txt): "))
	        if target == '':
	                with open('SMBList.txt') as data:
	                	#iplist = (line.rstrip('\r\n') for line in data)
	                	for line in data:
					if line != '':
						execute = "./smbenum.py " + line
	                			subprocess.call(execute, shell=True)
			data.close()
	        elif target != '':
			execute = "./smbenum.py " + target
	                subprocess.call(execute, shell=True)
	
	elif selection == 6: #ftp anon nse
	        target = str(raw_input("Target (blank to use FTPList.txt): "))
	        if target == '':
	                with open('FTPList.txt') as data:
	                	for line in data:
					if line != '':
						target = line.split(':')[0]
						port = line.split(':')[1]
						execute = "./ftpenum.py " + target + " " + port
	                			subprocess.call(execute, shell=True)
			data.close()
	        elif target != '':
			port = str(raw_input("Port: "))
			execute = "./ftpenum.py " + target + " " + port
	                subprocess.call(execute, shell=True)
	
	elif selection == 7: #nikto
	        target = str(raw_input("Target (blank to use HTTPList.txt): "))
	        if target == '':
	                with open('HTTPList.txt') as data:
	                	#iplist = (line.rstrip('\r\n') for line in data)
	                	for line in data:
					if line != '':
						target = line.split(':')[0]
						port = line.split(':')[1]
						execute = "./httpenum.py " + target + " " + port
	                			subprocess.call(execute, shell=True)
			data.close()
	        elif target != '':
			port = str(raw_input("Port: "))
			execute = "./httpenum.py " + target + " " + port
	                subprocess.call(execute, shell=True)
	
	elif selection == 8: #instructions
		print "\n1) BACKUP YOUR KEEPNOTE NOTEBOOK or create a new one"
		print "2) Copy the recon2kn files into your notebook's main folder"
		print "3) Add target IPs to IPList.txt (one per line)"
		print "4) Run recon2kn.py and follow the prompts"
		print "5) Reload notebook to see scan results (file > reload notebook)\n"
		print "Note: To use options 4-7 you first need to create target lists:"
		print "      SNMPList.txt, SMBList.txt, FTPList.txt and HTTPList.txt."
		print "      You can do this manually or generate them with option 3.\n"
		raw_input("**Press enter to continue**")
		
		
	elif selection == 9: #exit
		break
