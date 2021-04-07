import PySimpleGUI as sg
import os.path
import json



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

layout = []
layout += [[sg.Button("Back")], [sg.Text("Previous Evaluation", size=(40,5))]]
layout += [searchList(x) for x in range(0,l)]

window=sg.Window("Previous Evaluation",layout)

while True:
    event,values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == "Back":
        break
window.close()