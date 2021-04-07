import PySimpleGUI as sg
import os.path
import json

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



#frame1=[]
info=[[sg.Text(bedroom[0]), sg.Text(bathroom[0])], [sg.Text(floor[0]), sg.Text(sqft[0])], [sg.Text(info[0])]]
#frame2=[]
valueInfo=[[sg.Text(value[0])],
[sg.Text('loan estimate')],
[sg.Text('tax estimate')],
[sg.Text('total cost')]]


layout = [[sg.Button("Back"), sg.Button("Home")],[sg.Text("Evalation Display")],[sg.Column(info, element_justification='l'),sg.Column(valueInfo, element_justification='c')]]

window = sg.Window("Display Evaluation",layout)

event,values=window.read()

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()