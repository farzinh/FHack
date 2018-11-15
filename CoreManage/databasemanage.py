try:
    from src.Colors import TextColor
    import os
    from core.managesqlitedb import DirectoryFinerDB
except Exception as err:
    TextColor.RED + str(err) + TextColor.WHITE

def StartManageDBs():
    choice = raw_input('Enter your choice<1-5>:')

    if choice == '1': #show all database that fhack use
        ShowAllDBs()
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


def ShowAllDBs():
    #list_of_files = {}
    list_of_alldbs = list()
    for (dirpath, dirnames, filenames) in os.walk('.'):
        for filename in filenames:
            #list_of_files[filename] = os.sep.join([dirpath, filename])
            if filename.endswith('.db'):
                list_of_alldbs.append(filename)

