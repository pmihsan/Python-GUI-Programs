import PySimpleGUI as sg

bw: dict = {'size':(5,1), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#F8F8F8")}
bt: dict = {'size':(5,1), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#F1EABC")}
bo: dict = {'size':(5,1), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#ECA527"), 'focus':True}

layout = [
    [sg.Text("Perform Basic calculation operations")],
    [sg.Text('0.0000', size=(20,2), justification='right', font=('Digital-7',15), text_color='red', background_color='white' , key="_DISPLAY_")],
    [sg.Button('CLS',**bt), sg.Button('CE',**bt), sg.Button('%',**bt), sg.Button('/',**bt)],
    [sg.Button('7',**bw), sg.Button('8',**bw), sg.Button('9',**bw), sg.Button('*',**bt)],
    [sg.Button('4',**bw), sg.Button('5',**bw), sg.Button('6',**bw), sg.Button('-',**bt)],
    [sg.Button('1',**bw), sg.Button('2',**bw), sg.Button('3',**bw), sg.Button('+',**bt)],
    [sg.Button('0',**bw), sg.Button('.',**bw), sg.Button('^',**bt), sg.Button('=', **bo, bind_return_key=True)],
    [sg.Button('Exit')],
]

window = sg.Window("Calculator", layout,element_justification='right', margins=(10,20) )

var = {'front': [], 'back': [], 'decimal': False, 'x':0.0, 'y':0.0, 'result':0.0, 'operator':''}

def format_number() -> float:
    return float(''.join(var['front']) + '.' + ''.join(var['back']))

def update_display(display_value):
    try:
        window['_DISPLAY_'].update(value='{:,.4f}'.format(display_value))
    except:
        window['_DISPLAY_'].update(value=display_value)

def num_click(event):
    global var
    if var['decimal']:
        var['back'].append(event)
    else:
        var['front'].append(event)
    update_display(format_number())

def op_click(event):
    global var
    var['operator'] = event
    try:
        var['x'] = format_number()
    except:
        var['x'] = var['result']
    clear_click()

def clear_click():
    global var
    var['front'].clear()
    var['back'].clear()
    var['decimal'] = False

def calculate_click():
    global var
    var['y'] = format_number()
    try:
        var['result'] = eval(str(var['x']) + var['operator'] + str(var['y']))
        update_display(var['result'])
        write_his_on_file(1)
        clear_click()
    except:
        if var['operator'] == '^':
            a = float(var['x'])
            b = float(var['y'])
            var['result'] = str(a ** b)
            update_display(var['result'])
            write_his_on_file(1)
            clear_click()
        else:    
            update_display("ERROR!")
            write_his_on_file(0)
            clear_click()

def write_his_on_file(x):
    histfile = open('history.txt', 'a')

    if x == 0:
        histfile.write("Error => Invalid Input\n")
        print("Error => Invalid Input")
        return

    history = str(var['x']) + " " + var['operator'] + " " + str(var['y']) + " = " + str(var['result']) + "\n"
    histfile.write(history)
    print(history, end="")
    histfile.close()


while True:
    event, values = window.read()
    # print(event)
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    op_list = ['+', '-', '*', '/', '%', '^']
    esc_list = ['Escape:27', 'CLS', 'CE']
    if event in num_list:
        num_click(event)

    if event in op_list:
        op_click(event)

    if event in esc_list:
        clear_click()
        update_display(0.0)
        var['result'] = 0.0

    if event == '=':
        calculate_click()

    if event == '.':
        var['decimal'] = True
    
    if event == "Exit" or event == sg.WIN_CLOSED or event is None:
        break

window.close()