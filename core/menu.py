# -*- coding: utf-8 -*-

try:
    from src.Colors import TextColor
    from src.libs import sys
except Exception as err:
    raise SystemExit, TextColor.RED + "Something is wrong: %s" % (err) + TextColor.WHITE


# show items of attack
class ShowItems:
    def __init__(self):
        pass

    def ShowMenu(self):
        sys.stdout.write(TextColor.GREEN + str('\t\t1. Website Attack \t'))
        print '2. Create Malware'
        sys.stdout.write(str('\t\t3. Social engineering \t'))
        print '4. Network attack'
        sys.stdout.write(str('\t\t5. Software analysis \t'))
        print '6. Information gathering'
        sys.stdout.write(str('\t\t7. Manage database'))
        print (str("\t0. Exit") + TextColor.WHITE)

    def ItemOfWebAttack(self):
        print TextColor.HEADER + TextColor.UNDERLINE + str("|------Web Application Pentest------|" + TextColor.WHITE)
        print TextColor.CYAN + str('|1. SQL Injections')
        print str('|2. XSS Attack')
        print str('|3. Admin page finder')
        print str('|4. Login password bruteforce')
        print str('|5. Crawl website')
        print str('|6. Directory finder')
        print str('|7. Reverse Ip LookUp')
        print str('|0. Exit') + TextColor.WHITE

    def ItemOfManageDatabase(self):
        print TextColor.HEADER + TextColor.UNDERLINE + str('|------Manage Database------|') + TextColor.WHITE
        print TextColor.CYAN + str('|1. Show all database')
        print str('|2. Insert to table')
        print str('|3. Raw query') + TextColor.WHITE
        print

    def ItemOfInformationGathering(self):
        print TextColor.HEADER + TextColor.UNDERLINE + str('|------Information Gathering------|') + TextColor.WHITE
        print TextColor.CYAN + str('|1. Reverse IP lookup')
        print TextColor.CYAN + str('|2. Whois')
        print str('|0. Exit') + TextColor.WHITE
