#!usr/bin/env python

from src.Colors import TextColor
from core.menu import ShowItems
from src.Mask import MaskTerminal
from sqlinjection import test_website_main

define_MAX_MenuItem = 6
define_MAX_MenuItem_WEB_ATTACK = 4

def Switch_Menu_Item(number):
	subMenu = ShowItems()
	if number == '1':
		while True:
			subMenu.ItemOfWebAttack()
			choose = raw_input(TextColor.GREEN + str('Choose your item:') + TextColor.WHITE)

			if choose == '0':
				print
				break

			if choose > define_MAX_MenuItem_WEB_ATTACK and not choose.isdigit():
				print TextColor.WARNING + str('\nPlease Enter <0-4>\n') + TextColor.WHITE
			elif choose == '1':
				test_website_main.start()

	else:
		print 'On construction'

def main():

	global define_MAX_MenuItem

	mainMask = MaskTerminal()
	mainMask.ShowMask()
	mainMenu = ShowItems()

	while True:
		mainMenu.ShowMenu()
		choose = raw_input(TextColor.BLUE + str('Choose your item:') + TextColor.WHITE)

		if choose > define_MAX_MenuItem and not choose.isdigit():
			print TextColor.WARNING + '\nPlease Enter <1-6>\n' + TextColor.WHITE
		else:
			Switch_Menu_Item(choose)

if __name__ == "__main__":
	try:
		main()
	except Exception as err:
		print TextColor.RED + str(err) + TextColor.WHITE
	except KeyboardInterrupt:
		print TextColor.PURPLE + str('\nGood luck :)\n') + TextColor.WHITE
