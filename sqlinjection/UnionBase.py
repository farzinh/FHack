#this file created for union base attck method

try:
    import src.libs as lib
    from src.Colors import TextColor
    from Config.WebConfig import (define_headerdata)
except Exception as err:
    raise SystemExit, TextColor.RED + TextColor.BOLD + str("What happened :( something is wrong: %s" % (err)) \
                      + TextColor.WHITE

class UnionBaseAttack(object):
    def __init__(self, url, injectedChar):
        self.url = url
        self.injectedChar = injectedChar

        self.StartAttack(url, injectedChar)

    def StartAttack(self, url, injectedChar):
        response = lib.requests.get(url=url, headers=define_headerdata)



