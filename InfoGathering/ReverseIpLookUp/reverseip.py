try:
    import src.libs as lib
    from .Mask import MASK
    from src.Colors import TextColor
    import json
    import os
except Exception as err:
    raise SystemError, '\033[0m' + 'Something is wrong with libraries: %s' % err + '\033[0m'


def LOW():  # with some data
    DEFINE_HEADERS = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0 Iceweasel/22.0',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    try:
        print
        url = raw_input('\033[94m' + '==> Enter site url or ip (e.g.:example.com): ' + '\033[0m')

        if not os.path.exists(
                './outputs/Info-Gathering/' + 'LOW-' + url):  # check that destination file is exist or  not
            open('./outputs/Info-Gathering/' + 'LOW-' + url, 'a')  # if not we create that file

        response = lib.requests.post(url='https://domains.yougetsignal.com/domains.php',
                                     data={
                                         'remoteAddress': url
                                     },
                                     headers=DEFINE_HEADERS, verify=False)

        jsonRes = json.loads(response.text)

        remoteAddress = jsonRes['remoteAddress']
        remoteIpAddress = jsonRes['remoteIpAddress']

        print '\033[34m' + "[+] Remote address is: %s" % remoteAddress + '\033[0m'
        print '\033[34m' + "[+] Remote Ip address is: %s" % remoteIpAddress + '\033[0m'

        print
        print '\033[31m' + '-----------------Domains on this Server-----------------' + "\033[0m"
        print

        with open('./outputs/Info-Gathering/' + 'LOW-' + url, 'a') as file:
            for item in jsonRes['domainArray']:
                print '\033[33m' + str(item[0]) + '\033[0m'
                file.write(str(item[0]) + '\n')
    except Exception:
        raise SystemExit, '\033[31m' + 'Something is wrong: check your input or email topcodermc@gmail.com' + '\033[0m'


def HIGH():
    print 'Loading .... not complete yet'


def ReverseIpLookUp():
    if not os.path.exists('./outputs/Info-Gathering'):
        os.mkdir('./outputs/Info-Gathering')

    MASK()
    print
    selectedDepth = raw_input(TextColor.WHITESMOKE + 'info-gath/ReverseIp/# Selecte one item: ' + TextColor.WHITE)

    if selectedDepth == '1':
        LOW()
    elif selectedDepth == '2':
        HIGH()
    else:
        raise SystemExit, TextColor.RED + '[-] Please Enter number from subment items' + TextColor.WHITE
