# -*- coding: utf-8 -*-
try:
    import src.libs as lib
    from src.Colors import TextColor
except Exception as err:
    raise SystemExit, TextColor.RED + TextColor.BOLD + str(" What happn :( something is wrong: %s"%(err)) + TextColor.WHITE

define_data = {
"user-agent":
"Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25"
}



class Attack(object):
    def __init__(self, url):
        self.url = url

    def TestVulnarability(self):
        reposne = lib.requests.get(url=self.url + "")