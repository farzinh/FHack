try:
    from src.Colors import TextColor
except Exception as err:
    raise SystemExit, '%s' % err

#todo = I must work here

def XssTypeOfDepth():
    pass

def MakeSelection():
    print TextColor.WHITESMOKE + "\t\t => [1]. Use Fhack database for payloads"
    print "\t\t => [2]. Use payloads file (from ./payloads/payloads)"
    print "\t\t => [3]. Use my single payload"
    print "\t\t => [4]. Exit " + TextColor.WHITE

    choice = raw_input(TextColor.CVIOLET + "Fhack/WebAttack/XSS/# Make your choice (1-3): " + TextColor.WHITE)

    if choice == "1":
        UseFhackDataBase()
    elif choice == "2":
        UsePayloadFiles()
    elif choice == "3":
        UseSinglePayload()


def UseFhackDataBase():
    pass


def UsePayloadFiles():
    pass


def UseSinglePayload():
    pass