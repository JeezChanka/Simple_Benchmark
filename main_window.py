import PySimpleGUI as sg
import win32api
import win32file    

def getLayoutMainWindow():
    drives = get_removable_drives()
    print(drives)
    for drive in drives:
        win32api.GetVolumeInformation(drive)
        
    return [[sg.Text('Benchamark dysków przenośnych', pad=(10,10))], 
            [sg.Text('Wybierz dysk:', pad=(0,10)), sg.OptionMenu(values=drives, key='-DISKS-', size=(10, 60))],
            [sg.Button(button_text='Start', size=(7,1), pad=(0,10)),sg.Exit(button_text="Wyjście", size=(7,1))]]
    

def get_removable_drives():
    """Returns a list containing letters from removable drives"""
    drive_list = win32api.GetLogicalDriveStrings()
    drive_list = drive_list.split("\x00")[0:-1]  # the last element is ""
    list_removable_drives = []
    for letter in drive_list:
        if win32file.GetDriveType(letter) == win32file.DRIVE_REMOVABLE:
            list_removable_drives.append(letter)
    return list_removable_drives 