import PySimpleGUI as sg
import win32api
import win32file    

def getLayoutMainWindow():
    drives = get_removable_drives()
    print(drives)
    
    for drive in drives:
        win32api.GetVolumeInformation(drive)
        
    if(drives == []):
        drives = [("<BRAK>")]
        
    return [[sg.Text('Benchamark dysków przenośnych', pad=(10,10))], 
            [sg.Text('Wybierz dysk:', pad=(0,10)), sg.OptionMenu(values=drives, key='-DISKS-', size=(10, 60), default_value=drives[0])],
            [sg.Button(button_text='Start', size=(7,1), pad=(0,10)), sg.Button(button_text='Odśwież', size=(7,1), pad=(10,10)),sg.Exit(button_text="Wyjście", size=(7,1))]]
    

def get_removable_drives():
    """Returns a list containing letters from removable drives"""
    drive_list = win32api.GetLogicalDriveStrings()
    drive_list = drive_list.split("\x00")[0:-1]  # the last element is ""
    # list_removable_drives = []
    # for letter in drive_list:
    #     if win32file.GetDriveType(letter) == win32file.DRIVE_REMOVABLE:
    #         list_removable_drives.append(letter)
    return drive_list 

def main_refresh(window):
    new_drives = get_removable_drives()
    print(new_drives)
    
    for drive in new_drives:
        win32api.GetVolumeInformation(drive)
        
    if(new_drives == []):
        new_drives = [("<BRAK>")]
    window['-DISKS-'].update(values=new_drives, size=(10, 60))
    window['-DISKS-'].update(new_drives[0])