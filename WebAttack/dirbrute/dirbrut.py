# -*- coding: utf-8 -*-
try:
    import socket as sock
    import src.libs as lib
    from src.Colors import TextColor
    from threading import Thread
except Exception as err:
	raise SystemExit, TextColor.RED + "Something is wrong: %s"%(err) + TextColor.WHITE

class MainThread(Thread):
    def __init__(self):
        pass

    def run():
        pass

def start_check_url(url_list_items, rhost):
    pass

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
    rhost = raw_input(TextColor.CURL + 'Enter url: ' + TextColor.WHITE)
    print TextColor.WARNING + str('[*] Checking RHOST --> %s'%(rhost)) + TextColor.WHITE
    try:
        soc_init = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        status = soc_init.connect_ex((rhost, 80))
        soc_init.shutdown(sock.SHUT_RDWR)
        soc_init.close()
        if status == 0:
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
    print TextColor.WARNING + str('[*] please wait to load line of %s'%(wordlist)) + TextColor.WHITE
    with open(wordlist, 'r') as file:
        for item in file.readlines():
            path_list.add(item)
    print TextColor.GREEN + str('[+] All items add to the list succcessfully!! Done.') + TextColor.WHITE

    print TextColor.CYELLOWBG2 + TextColor.RED + str('[+] Beginning scan') + TextColor.WHITE
    start_check_url(path_list, rhost)

def Start():
    rhost = CheckRhost() #first we check that rhost is online or not

    choice = raw_input(TextColor.PURPLE + 'Fhack ~/web-attack/dirbrut/# Enter your choice: ' + TextColor.WHITE)

    if choice == "1":
        filePath = raw_input(TextColor.HEADER + str('Enter wordlist path: ') + TextColor.WHITE)
        WithWorldList(filePath, rhost)
    elif choice == "2":
        pass
    elif choice == "3":
        pass

    