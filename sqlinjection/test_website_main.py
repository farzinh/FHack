from Config.WebConfig import define_headerdata

try:
	import core.crawler as craw
	from src.Colors import TextColor
	import src.libs as lib
	import os
	import SqlAttack
	from Config.WebConfig import (define_headerdata)
except Exception as err:
	raise SystemExit, TextColor.RED + str("Something wring in importing the libraries: %s"%(err)) + TextColor.WHITE

def menu():
	print TextColor.WARNING + str('1. use file') + TextColor.WHITE
	print TextColor.WARNING + str('2. use url') + TextColor.WHITE

class Check_WebSite(object):

	def __init__(self):
		pass

	def CheckWithFile(self):
		print
		url_path = raw_input(TextColor.CYAN + TextColor.BOLD + '~# => Enter path of file:' + TextColor.WHITE)
		if not os.path.exists(url_path):
			print
			print TextColor.RED + ' File dose not exist' + TextColor.WHITE
			print
			return
		else:
			urls = set()
			lib.sleep(0.2)
			print
			print TextColor.WARNING + '[*]Please wait to load datas ...' + TextColor.WHITE

			with open(url_path, 'r') as file:
				for line in file.readlines():
					url = line.strip('\n').split('/')
					if bool(lib.re.search('\d', url[len(url) - 1])):
						urls.add(line.strip('\n'))
					else:
						continue

			print TextColor.GREEN + '[+]Done all links loaded ...' + TextColor.WHITE
			print TextColor.CYAN + '[+]All Links: %d'%(len(urls)) + TextColor.WHITE
			print TextColor.HEADER + TextColor.BOLD + '[+]-------Starting the test-------[+]' + TextColor.WHITE
			print
			lib.sleep(.5)

			for item in urls:
				print TextColor.CYAN + TextColor.BOLD + '[+]Test on => [%s]'%(item.strip('\n'))
				self.start(item)

	def CheckWithUrl(self):
		print
		url = raw_input(TextColor.CYAN + TextColor.BOLD + '~# => Enter url (e.g:http://exapmle.com/index.php?id=1) : ' \
						+ TextColor.WHITE)
		lib.sys.stdout.write(TextColor.BLUE + '[*]wait for getting response: ')
		reposne = lib.requests.get(url=url, params=define_headerdata)
		print reposne.status_code
		if reposne.status_code == 200:
			SqlAttack.Attack(url=url)
		else:
			print TextColor.WARNING + TextColor.BOLD + '[-]error in reposne' + TextColor.WARNING

	def start(self, url):
		lib.sys.stdout.write(TextColor.BLUE + '\t[*]wait for getting response: ')
		reposne = lib.requests.get(url=url, params=define_headerdata)
		print reposne.status_code
		if reposne.status_code == 200:
			SqlAttack.Attack(url=url)
		else:
			print TextColor.WARNING + TextColor.BOLD + '\t[-]error in reposne' + TextColor.WARNING


def start():
	print
	print TextColor.BOLD + TextColor.WARNING + str('''
	            ______
		   | _____|
		   |_|000// 
		---| |-------> SQL INJECTIONS
		   | |__| |
		   |______|
	''') + TextColor.WHITE
	print TextColor.WARNING + TextColor.BOLD + "-------------------------------------------------" + TextColor.WHITE
	menu()

	choose = raw_input(TextColor.BOLD + TextColor.PURPLE + 'Fhack~/sql-injection# ' + TextColor.WHITE)
	if choose == '1':
		Check_WebSite().CheckWithFile()
	elif choose == '2':
		Check_WebSite().CheckWithUrl()
	else:
		print TextColor.RED + str('Please choose item between <1-2>') + TextColor.WHITE


if __name__ == "__main__":
	start()
