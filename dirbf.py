import urllib
import time
import sys


print('''
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '
''')
print('''
    --------------------------------------------------------------
                DIRECTORY BRUTE FORCE By 4nzeL4
                Author: [Akazh]
                Facebook: https://facebook.com/akazh.gov
    --------------------------------------------------------------
How to use:
1. input Your Wordlist Name
2. Select Method [status code, keyword]
3. Input Your Target
''')
world = raw_input('worldlist: ')
arg = open(world, 'r').readlines()
select = input('select: ')
tar = raw_input('target: ')

if select == 1:
	print('[INFO] Started on '+time.ctime())
	time.sleep(2)
	print('[INFO] Connecting to Target ...')
	time.sleep(5)
	print('[INFO] Connected!')
	time.sleep(2)
	print('[INFO] Starting Brute Force ...')

	for line in arg:
		lines = line.replace('\n', ' ')
		lines = tar + '/' + lines
		url = urllib.urlopen(lines)
		status = url.code
		if status != 301 and status != 404:
			print("\n[+] Found!\n=>" + lines)
			file = open('result_dir.txt','w')
			file.write(lines)
			file.close()

elif select == 2:
	keyword = raw_input("Insert Keyword: ")
	print('[INFO] Started on '+time.ctime())
	time.sleep(2)
	print('[INFO] Connecting to Target ...')
	time.sleep(5)
	print('[INFO] Connected!')
	time.sleep(2)
	print('[INFO] Starting Brute Force ...')
	for line in arg:
		lines = line.replace('\n', ' ')
		lines = tar + '/' + lines
		url = urllib.urlopen(lines)
		if not keyword in url.read():
			print("\n[+] Found!\n=>" + lines)
			file = open('result_dir.txt','a')
			file.write(lines)
			file.close()
else:
	print("[!] SESSION CLOSED [!]")