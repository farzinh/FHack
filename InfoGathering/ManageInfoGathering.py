try:
    from src.Colors import TextColor
    from .ReverseIpLookUp.reverseip import ReverseIpLookUp
except Exception as err:
    raise SystemError, '\033[31m' + 'Some error happened please check it: %s' % err + '\033[0m'


# main function that control all item in information gathering
def mainInfoGathering():
    print
    selectedItem = raw_input(TextColor.GREEN + 'Fhack ~/Info-Gathering/# ' + TextColor.WHITE)
    ManageSelectedItems(selectedItem)
    print


def ManageSelectedItems(selectedItem):
    if selectedItem == '1':
        ReverseIpLookUp()
    else:
        print TextColor.RED + '[-] Please select from menu' + TextColor.WHITE
