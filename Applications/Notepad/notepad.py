import PySimpleGUI as sg
sg.change_look_and_feel('BrownBlue')

WIN_W: int = 50
WIN_H: int = 25
filename: str = None

new_file: str = 'New File (CTRL+N)'
open_file: str = 'Open File (CTRL+O)'
save_file: str = 'Save File (CTRL+S)'

menu_layout: list = [
    ['File', [new_file, open_file, save_file, 'Save As', '---', 'Exit']],
    ['Tools', ['Word Count']],
    ['Help', ['About']]
]

layout: list = [
    [sg.Menu(menu_layout)],
    [sg.Text('> New File <', font=('Consolas', 10), size=(WIN_W, 1), key='_INFO_')],
    [sg.Multiline(font=('Consolas', 12), size=(WIN_W, WIN_H), key='_BODY_')]
]

window: object = sg.Window('Notepad', layout=layout, margins=(0,0), resizable=True, return_keyboard_events=True)
window.read(timeout=1)
window.maximize()
window['_BODY_'].expand(expand_x=True, expand_y=True)

def new_file_menu() -> str:
    window['_BODY_'].update(value='')
    window['_INFO_'].update(value='> New File <')
    filename = None
    return filename

def open_file_menu() -> str:
    try:
        filename: str = sg.popup_get_file('Open File', no_window=True)
    except:
        return
    
    if filename not in (None, '') and not isinstance(filename, tuple):
        with open(filename, 'r') as f:
            window['_BODY_'].update(value=f.read())
        window['_INFO_'].update(value=filename)
    return filename

def save_file_menu(filename: str):
    if filename not in (None, '') and not isinstance(filename, tuple):
        with open(filename, 'w') as f:
            f.write(values.get('_BODY_'))
        window['_INFO_'].update(value=filename)
    else:
        save_file_as_menu()

def save_file_as_menu() -> str:
    try:
        filename: str = sg.popup_get_file('Save File As', save_as=True, no_window=True)
    except:
        return
    if filename not in (None, '') and not isinstance(filename, tuple):
        with open(filename,'w') as f:
            f.write(values.get('_BODY_'))
        window['_INFO_'].update(value=filename)

    return filename

def word_count():
    words: list = [w for w in values['_BODY_'].split(' ') if w != '\n']
    word_count: int = len(words)
    sg.PopupQuick("Word Count: {:,d}".format(word_count),auto_close=False)

def about_me():
    sg.PopupQuick('"All great things have small beginnings"', auto_close=False)

while True:
    event, values = window.read()

    if event in (None, 'Exit'):
        break
    if event in (new_file, 'n:78'):
        filename = new_file_menu()
    if event in (open_file, 'o:79'):
        filename = open_file_menu()
    if event in (save_file, 's:83'):
        save_file_menu(filename)
    if event in ('Save As', ):
        filename = save_file_as_menu()
    if event in ('Word Count', ):
        word_count()
    if event in ('About', ):
        about_me()
