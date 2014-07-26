Title: recon2kn.py
Author: W. Daniels (OneWest)
Version: 1.0

Desc:	This is a quick script I wrote up, as part of the OSCP course, 
	to generate keepnote pages for initial network scans. It is loosely
	based on reconscan.py by Mike Czumak (if you don't need the keepnote
	pages I highly recommend his script) I'm not a programmer and make no
	guarantees regarding functionality or anything else. The user accepts
	all legal responsibility. You're welcome to redistribute or modify as you
	see fit but please maintain original author attribution. If you have
	any questions, comments, suggestions or want to talk security I'm usually
	on the offsec chan. 

Instructions:
	1) BACKUP YOUR KEEPNOTE NOTEBOOK or create a new one
	2) Copy the recon2kn files into your notebook's main folder
	3) Add target IPs to IPList.txt (one per line)
	4) Run recon2kn.py and follow the prompts
	5) Reload notebook to see scan results (file > reload notebook)
	Note: To use options 4-7 you first need to create target lists:
      	      SNMPList.txt, SMBList.txt, FTPList.txt and HTTPList.txt.
      	      You can do this manually or generate them with option 3.
