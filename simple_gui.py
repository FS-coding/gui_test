""" 
A simple gui in PySimpleGUI that lists the files inside the selected document
"""

import PySimpleGUI as sg
import os


layout = [[[sg.Text('Enter directory'), 
            sg.In(size=(40, 1), enable_events = True, key='-FOLDER-'), 
            sg.FolderBrowse()], 
            [sg.MLine(size=(60,20), key='-ML1-')]],
            [sg.B('Generate'), 
             sg.B('Print'), # does nothing  
             sg.B('Cancel')]]

window = sg.Window('My GUI example', layout)

def list_files(location, folder):
    files = os.listdir(folder)
    if files == []:
        window[location].print('(directory is empty)', text_color='red')
    else:
        for file in files:
            window[location].print(file, text_color='green')


while True:             # Event Loop
    event, values = window.read()
    
    folder = values['-FOLDER-']
    
    if event in (None, 'Cancel'):
        break
    if event == 'Generate':
        # TO DO: that this command can be accessing just by pressing 'enter'
        
        if folder == '':
            window['-ML1-'].print('Select a folder', text_color='red')
        else:
            window['-ML1-'].print(f'Folder: {folder}:')
            list_files('-ML1-', folder)
window.close()