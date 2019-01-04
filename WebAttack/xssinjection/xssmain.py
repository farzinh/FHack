try:
    from src.Colors import TextColor
    import src.libs as lib
    from Config.WebConfig import define_headerdata
    from .payloads.loader import MakeSelection
    from Config.RecOS import IsOSDarwin, IsOSLinux
    from Utilities.BaseClass import ShowProgress
except Exception as err:
    raise SystemExit, 'Something is wrong: %s' % err


def PrintXssMask():
    maskString = TextColor.GREEN + str("""
    
                Do want search XSS vulnerability ?
                
                                            vulnerable site
                     __.__.__.__.__           ____   __ 
                    (              )         |    | |==|
                    (   Find XSS   ) <====>  |____| |  |
                    (______________)         /::::/ |__|
                      (_)     (_)
                      |=|     |=|
    
    """) + TextColor.WHITE
    return maskString


def MainXSS():
    print PrintXssMask()

    output = MakeSelection()

    rhost = raw_input(TextColor.CVIOLET + str('~/WebAttack/XSSAttack/# Enter site url: ') + TextColor.WHITE)


    response = lib.requests.get(url=rhost, params=None, headers=define_headerdata, verify=False)

    if response.status_code == 200:
        searchType = raw_input(TextColor.CVIOLET + str(
            '~/WebAttack/XSSAttack/# Do you wanna test whole of the site <y/n>: ') + TextColor.WHITE)

        StartAttack(output, rhost, searchType)


def StartAttack(output, rhost, searchType):

    if searchType == 'y':
        pass #todo = fix this section of code



    if type(output) == list:

            define_headerdata['referer'] = rhost

            findXss = False
            counter = 0

            for item in output:
                if item == " " or item == '\n' or item == "":
                    continue

                response = lib.requests.get(url=rhost, headers=define_headerdata, verify=False)

                if IsOSDarwin():  # parser os lxml not working on mac OS <Darwin>
                    soup = lib.BS(response.content, "html.parser")
                else:
                    soup = lib.BS(response.content, "lxml")

                ShowProgress('... Testing payload [%d] please wait ' % counter, counter)
                counter += 1

                with lib.requests.Session() as session:
                    for line in soup.find_all('input', {'type': 'text'}):

                        parameter = str(lib.urlparse.urlparse(line['name'])[2])

                        response = session.get(url=rhost, params={parameter: str(item)}, verify=False)

                        if response.content.find(str(item)) is not -1:
                            print
                            counter += 1

                            ShowProgress('... Testing payload [%d] please wait ' % counter, counter)
                            print
                            print TextColor.GREEN + '[+] => XSS found with: %s on input => %s' \
                                  % (item, lib.urlparse.urlparse(line['name'])[2]) + TextColor.WHITE
                            print
                            findXss = True

                if findXss:
                    break

    if not findXss:
        print
        print TextColor.RED + 'This site [%s] is not vulnerabale' % rhost + TextColor.WHITE
        print


if __name__ == "__main__":
    try:
        MainXSS()
    except Exception as err:
        raise SystemExit, TextColor.RED + 'Something is wrong: %s' % err + TextColor.RED
