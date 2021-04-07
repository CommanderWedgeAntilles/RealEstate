import PySimpleGUI as sg
import os.path
import json



left=[
    [sg.Text("Name: "), sg.In()],
    [sg.Text("Address: "), sg.In()],
    [sg.Text("Bedrooms: "), sg.In()],
    [sg.Text("Bathrooms: "), sg.In()],
    [sg.Text("Floors: "), sg.In()],
    [sg.Text("Square Feet: "), sg.In()]
    ]
right=[[sg.Text("Additional Info")],[sg.In(default_text='Extra Info about Property', size=(100,300))]]





layout = [
    [sg.Button("Back"), sg.Button("Home")],
    [sg.Text("Property Information for Evaluation")],
    [sg.Column(left, element_justification='l'),sg.Column(right, element_justification='c')],
    [sg.Button("Submit")]
]

window=sg.Window("Property Evaluation Application",layout)


while True:
    event,values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == "Back":
        break
    elif event == "Home":
        break
    elif event == "Submit":
        break
window.close()

