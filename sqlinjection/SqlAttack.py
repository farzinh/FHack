# -*- coding: utf-8 -*-
try:
    import src.libs as lib
    from src.Colors import TextColor
    from injection_defines import *
except Exception as err:
    raise SystemExit, TextColor.RED + TextColor.BOLD + str("What happened :( something is wrong: %s"%(err)) + TextColor.WHITE

define_data = {"user-agent":"Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25"}

class Attack(object):
    def __init__(self, url):
        self.url = url

        self.__TestVulnarability__()

    def __TestVulnarability__(self):
        global define_data
        print
        for item in define_injections_chars:
            lib.sys.stdout.write(TextColor.CYAN + str('[%s]'%(self.url + str(item))) + TextColor.WHITE)
            reposne = lib.requests.get(url=self.url + str(item), params=define_data)
            lib.sleep(.5)
            if reposne.content.find("You have an error in your SQL syntax;") or \
                    reposne.content.find("MariaDB server") or reposne.content.find("Unknown column"):
                print TextColor.RED + " => find vulnrability"
                break
            else:
                print TextColor.GREEN + ' => safe'

#todo: target = tncgroup.pk/content.php?Id=2





