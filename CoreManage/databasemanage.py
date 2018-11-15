try:
    from src.Colors import TextColor
    from core.managesqlitedb import DirectoryFinerDB
except Exception as err:
    TextColor.RED + str(err) + TextColor.WHITE

def StartManageDBs():
    choice = raw_input('Enter your choice<1-5>:')

    if choice == '1': #show all database that fhack use
        ShowAllDbs()
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    else:
        print 'Please Select <1-5>'


def ShowAllDbs():
    pass