try:
    from src.Colors import TextColor
    import src.libs as lib
    from Config.WebConfig import define_headerdata
    from Config.RecOS import IsOSDarwin, IsOSLinux
except Exception as err:
    raise SystemExit, 'Something is wrong: %s'% err

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

    rhost = raw_input(TextColor.CVIOLET + "Fhack/webAttack/XSS/# Enter site url: " + TextColor.WHITE)

    define_headerdata['referer'] = rhost

    response = lib.requests.get(url=rhost, headers=define_headerdata, verify=False)

    if IsOSDarwin():  # parser os lxml not working on mac OS <Darwin>
        soup = lib.BS(response.content, "html.parser")
    else:
        soup = lib.BS(response.content, "lxml")

    for line in soup.find_all('input', {'type': 'text'}):
        print lib.urlparse.urlparse(line['name'])[2]



if __name__ == "__main__":
    try:
        MainXSS()
    except Exception as err:
        raise SystemExit, TextColor.RED + 'Something is wrong: %s'% err + TextColor.RED
