#!usr/bin/env python

try:
	from src.Colors import TextColor
	from core.menu import ShowItems
	from src.Mask import MaskTerminal
	from WebAttack.sqlinjection import sql_website_attack
	from WebAttack.crawler import crawler as craw
	from WebAttack.dirbrute import dirbrut
	from src import libs
except Exception as err:
	raise SystemExit, TextColor.RED + str('\nSome thing wrong in libraries: %s\n'%(err)) + TextColor.WHITE

reload(libs.sys)
libs.sys.setdefaultencoding('utf-8') # this line set the all encoding of project to utf-8

define_MAX_MenuItem = 6
define_MAX_MenuItem_WEB_ATTACK = 4

def Switch_Menu_Item(number):
	subMenu = ShowItems()
	if number == '1': #web attack menu items
		while True:
			subMenu.ItemOfWebAttack()
			choice = raw_input(TextColor.GREEN + str('Fhack ~/web-attack/# ') + TextColor.WHITE)
			if choice == '0':
				print
				break
				
			if choice == '1':
				sql_website_attack.start()
			elif choice == '5':
				url = raw_input(TextColor.PURPLE + TextColor.BOLD + str('Fhack ~/web-attack/Crawler/# Enter url of rhost: ') \
											 + TextColor.WHITE)
				if url.endswith('/'):
					url = url[0:len(url) - 1]
				craw.SetWebSiteUrl(url=url)
			elif choice == '6':
				dirbrut.Start()
	else:
		print 'On construction'

def main():

	global define_MAX_MenuItem

	mainMask = MaskTerminal()
	mainMask.ShowMask()
	mainMenu = ShowItems()

	while True:
		mainMenu.ShowMenu()
		choose = raw_input(TextColor.BLUE + str('Fhack~# ') + TextColor.WHITE)

		if choose > define_MAX_MenuItem and not choose.isdigit():
			print TextColor.WARNING + '\n[*]Please Enter <1-6>\n' + TextColor.WHITE
		else:
			Switch_Menu_Item(choose)

if __name__ == "__main__":
	try:
		main()
	except Exception as err:
		print TextColor.RED + str(err) + TextColor.WHITE
	except KeyboardInterrupt:
		print TextColor.PURPLE + str('\nGood luck :)\n') + TextColor.WHITE
