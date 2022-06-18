import PySimpleGUI as sg 
import os.path

# Window Layout of two columns
file_list_columns = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40,20),
            key="-FILE LIST-"
        )
    ],
]

# for now will only show the name of the chosen file
image_viewer_column = [
    [sg.Text("Choose an image from the list on the left:")],
    [sg.Text(size=(40,1), key="-TOUT-")],
    [sg.Image(key='-IMAGE-')],
]

# Full Layout
layout = [ 
    [ 
        sg.Column(file_list_columns),
        sg.VSeparator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Image Viewer", layout)


# event loop
while True:
    event, values = window.read()
    if event == "EXIT" or event == sg.WIN_CLOSED:
        break
    # Folder name was given so make a list of files
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get the list of files in the folder
            file_list = os.listdir(folder)
        except:
            file_list = []
        
        fnames = [
            f 
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-": # A file was chosen from the list
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except:
            pass


window.close()