# -*- coding: utf-8 -*-

from src.Colors import TextColor
from src.libs import sys

#show items of attack
class ShowItems():
	def __init__(self):
		pass

	def ShowMenu(self):
		sys.stdout.write(TextColor.GREEN + str('\t\t1. Website Attack \t'))
		print '2. Create Malware'
		sys.stdout.write(str('\t\t3. Social engineering \t'))
		print '4. Network attack'
		sys.stdout.write(str('\t\t5. Software analysis \t'))
		print '6. Information gathering' + TextColor.WHITE

	def ItemOfWebAttack(self):
		print TextColor.HEADER + TextColor.UNDERLINE + str("|--------------------Web Application Pentest --" + TextColor.WHITE)
		print TextColor.CYAN + str('|1. SQL Injections')
		print str('|2. XSS Attack')
		print str('|3. Admin page finder')
		print str('|4. Admin page bruteforce')
		print str('|0. Exit') + TextColor.WHITE
