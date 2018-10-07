# -*- coding: utf-8 -*-
try:
    import requests as reqs
    import src.libs as lib
    from src.Colors import TextColor
    from threading import Thread
    from Config.WebConfig import define_headerdata
except Exception as err:
    raise SystemExit, TextColor.RED + "Something is wrong: %s"%(err) + TextColor.WHITE

class MainThread(Thread):
    def __init__(self, url_list_item, rhost):
        Thread.__init__(self)

        self.url = rhost
        self.guestList = url_list_item

    def run(self):
        for item in self.guestList:
            print self.url + item
            # response = reqs.get(url=self.url + item, headers=define_headerdata,
            #                     verify=False, allow_redirects=False)


def start_check_url(url_list_items, rhost):

    if rhost.endswith('/'):
        rhost = rhost[0: len(rhost) - 1]

    run_thread = MainThread(url_list_items, rhost)
    run_thread.setDaemon(True)
    run_thread.start()


def Menu():
    print TextColor.CYAN + str('|----- Directory attack -----|')
    print '|1. Use wordlist <Dictionary>'
    print '|2. Use fhack database <Dictionary>'
    print '|3. Use bruteforce' + TextColor.WHITE

def CheckRhost():
    """ Function
        in this function first we check web site which is online or not
        then show menu to start
    """
    print
    rhost = raw_input(TextColor.PURPLE + ' ==> Enter url (e.g: http://example.com): ' + TextColor.WHITE)
    print TextColor.WARNING + str('[*] Checking RHOST --> %s'%(rhost)) + TextColor.WHITE
    try:
        response = reqs.get(url=rhost, headers=define_headerdata,
                            verify=False, allow_redirects=False)
        if response.status_code == 200:
            print TextColor.GREEN + str('[+] rhost has been set!! -- Done.') + TextColor.WHITE
            lib.sleep(.5)
            Menu()
            return rhost
        else:
            print TextColor.RED + 'Something wrong with rhost can not reach the rhost' + TextColor.WHITE
            return None
    except Exception as err:
        print TextColor.RED + str("Something is wrong %s"%(err)) + TextColor.WHITE
        return None

def WithWorldList(wordlist, rhost):
    path_list = set()
    print TextColor.WARNING + str('[*] please wait to load lines of %s'%(wordlist)) + TextColor.WHITE
    with open(wordlist, 'r') as file:
        for item in file.readlines():
            if item.startswith('/'):
                path_list.add(item[1: len(item)])
            else:
                path_list.add(item)
    print TextColor.GREEN + str('[+] All items add to the list succcessfully!! Done.') + TextColor.WHITE

    print TextColor.CYELLOWBG2 + TextColor.RED + str('[+] Beginning scan') + TextColor.WHITE
    start_check_url(path_list, rhost)

def Start():
    rhost = CheckRhost() #first we check that rhost is online or not

    choice = raw_input(TextColor.PURPLE + ' ==> Enter your choice: ' + TextColor.WHITE)

    if choice == "1":
        filePath = raw_input(TextColor.HEADER + str('[*] Enter wordlist path: ') + TextColor.WHITE)
        WithWorldList(filePath, rhost)
    elif choice == "2":
        pass
    elif choice == "3":
        pass

    