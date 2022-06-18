import PySimpleGUI as sg 

layout = [
    [sg.Text("Hello From PySimpleGUI")],
    [sg.Button("CLICK ME!")]
]

# Create the Window
window = sg.Window("Demo", layout, margins=(120,50))

# Creating an event loop
while True:
    event, values = window.read()
    # Terminate the program if user closes the window or 
    # if he clicks the button
    if event == "CLICK ME!" or event == sg.WIN_CLOSED:
        break


window.close()
