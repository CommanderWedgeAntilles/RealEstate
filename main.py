import PySimpleGUI as sg
import os.path
import json
import numpy as np
from np import array
#import Home
#import EES
#import EPS
#import DES


def home():
    layout = [
    [sg.Text("Property Evaluation", size=(40,5))],
    [sg.Image("house.png", size=(200,200))], [sg.Button("Review")],
    [sg.Button("Evaluate")]]
    title = "Property Evaluation Application"

    
    window1=sg.Window("Property Evaluation Application",layout)

    #window["-IMAGE-"].update("house.png")

    while True:
        event,values = window1.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "Review":
            EES()
            break
        elif event == "Evaluate":
            EPS()
            break
        
    window1.close()


    return

def EES():

    with open('searches.json') as json_file:
        data = json.load(json_file)
    print(data)

    name = data['previous']['name']
    value = data['previous']['value']
    address = data['previous']['address']
    print(name)

    l= len(data['previous']['name'])
    print(l)
    print(name[0])

    def searchList(y):
            return [sg.Text(name[y]), sg.Text(value[y]), sg.Text(address[y])]

    def search(y):
        for x in range(0,l):
            a = array([0,0])
            a[x] = (str(name[x])+ " " + str(value[x]) + " " + str(address[x]))
            return a
    
    searched = search(l)

    layout = []
    layout += [[sg.Button("Back")], [sg.Text("Previous Evaluation", size=(40,5))]]
    layout += [searchList(x) for x in range(0,l)]
    layout += [[sg.Combo(searched)],[sg.Button("View Selected")]]

    window2=sg.Window("Previous Evaluation",layout)

    while True:
        event,values = window2.read()

        if event == sg.WIN_CLOSED:
            break
        if event == "Back":
            home()
            break
    window2.close()
    print("worked")
    return 

def DES(x):

    with open('searches.json') as json_file:
        data = json.load(json_file)

    name = data['current']['name']
    value = data['current']['value']
    address = data['current']['address']
    bedroom = data['current']['bedrooms']
    bathroom = data['current']['bathrooms']
    floor = data['current']['floors']
    sqft = data['current']['sqft']
    info = data['current']['info']



    info=[[sg.Text(bedroom[0]), sg.Text(bathroom[0])], [sg.Text(floor[0]), sg.Text(sqft[0])], [sg.Text(info[0])]]

    valueInfo=[[sg.Text(value[0])],
    [sg.Text('loan estimate')],
    [sg.Text('tax estimate')],
    [sg.Text('total cost')]]


    layout = [[sg.Button("Back"), sg.Button("Home")],[sg.Text("Evalation Display")],[sg.Column(info, element_justification='l'),sg.Column(valueInfo, element_justification='c')]]

    window3 = sg.Window("Display Evaluation",layout)

    event,values=window3.read()

    while True:
        event,values = window3.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Back":
            if x == 0:
                EPS()
                break
            elif x == 1:
                EES()
                break
        if event == "Home":
            home()
            break

    window3.close()
    return

def EPS():
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
        [sg.Button("Back")],
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
            home()
            break
        elif event == "Submit":
            #GUI->json file(move current to previous, replace with this data)->Model->analysis->json(update current)
            DES(0)
            break
    window.close()
    print("worked EPS")
    return

home()
# location= (600,600)
# window=sg.Window("main", location=location).Layout(layout)




# while True:
#     event,values = window.read()

#     if event == sg.WIN_CLOSED:
#         break
#     elif event == "Review":
#         layout, title = EES()
#         if event == sg.WIN_CLOSED:
#             break
#         elif event == "Back":
#             break
#         window.close()
#     elif event == "Evaluate":
#         EPS()
#         break

    
    
# window.close()