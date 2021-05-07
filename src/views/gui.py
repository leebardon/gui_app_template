import PySimpleGUI as sg


sg.theme("DarkTeal2")
layout = [[sg.T("")], 
         [sg.Text("Qlikview Excel File: "),sg.Input(), sg.FileBrowse(key="-IN-")],
         [sg.Button("Select")],
         [sg.Button("Exit")]]

###Building Window
window = sg.Window('H&S Courses - Incomplete', layout, size=(600,150))
    
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Select":
        data_path = values["-IN-"]
        

