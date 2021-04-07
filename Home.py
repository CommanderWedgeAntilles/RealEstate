import PySimpleGUI as sg
import os.path
import json
import EES

#dir_list = os.listdir("")
def home():
    layout = [
        [sg.Text("Property Evaluation", size=(40,5))],
        [sg.Image("house.png", size=(200,200))], [sg.Button("Review")],
        [sg.Button("Evaluate")]
    ]

    window=sg.Window("Property Evaluation Application",layout)

    #window["-IMAGE-"].update("house.png")

    while True:
        event,values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "Review":
            EES.EES()
            break
        elif event == "Evaluate":
            break
        
    window.close()