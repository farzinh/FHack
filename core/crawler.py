# -*- coding: utf-8 -*-

from src.Colors import TextColor
from src.libs import sleep
import src.libs as lib

''' Function
    name: SetWebSiteUrl
    parameters: url of site --> example: http://example.com
    return: That web site is available or not -> then 
'''
def SetWebSiteUrl(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        print TextColor.RED + str('\n[-]Please enter url correctly\n') + TextColor.WHITE
    else:
        try:
            print TextColor.WARNING + str('[*] Please wait to get response from %s ...'%(url)) + TextColor.WHITE

            headers = {
                "user-agent":
                    "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25"
            }

            if url.startswith('http://'):
                response = lib.requests.get(url, headers=headers , allow_redirects=False).status_code
            else:
                response = lib.requests.get(url, headers=headers, verify=False, allow_redirects=False).status_code

            if response == 200:
                print TextColor.GREEN + str('[+] Remote host has been set ...') + TextColor.WHITE
                sleep(0.5)
                print TextColor.WARNING + str('[+] Start crawl ...') + TextColor.WHITE
                num = raw_input(TextColor.GREEN + str('Enter depth of crawl: ') + TextColor.WHITE)
                GetAllLinks(url, num)
            else:
                print TextColor.RED + str('[-] Fail to set rhost :(') + TextColor.WHITE
                lib.sys.exit(TextColor.RED + "\nError\n" + TextColor.WHITE)

        except Exception as err:
            print TextColor.RED + str('[-] Some error with socket-> %s'%(err)) + TextColor.WHITE

''' Function
    name: GetAllLinks
    parameter: url of site -> example: http://example.com
    return: get all link in source code of web page
'''
def GetAllLinks(url, num):
    if url.startswith('http://'):
        pass

#------------------------------------------------------------------------Classes

class Crawler(object):
    def __init__(self, root, depth):
        self.root = root
        self.host = lib.urlparse.urlparse(root)[1] #Get host name from url
        self.depth = depth

        self.urls_seen = set()       #Used to avoid putting duplicate links in queue
        self.urls_remembered = set() #For reporting to user
        self.visited_links = set()   #Used to avoid re-processing a page

        self.num_links = 0           #Links found (and not excluded by filters)
        self.num_followed = 0        #Links followed




