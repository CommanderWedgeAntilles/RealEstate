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

def searchList(l):
        return [sg.Text(name), sg.Text(value), sg.Text(address)]


# prior_Searches = []
# for i in name:
#     prior_Searches += [sg.Text(name)]
#     prior_Searches += [sg.Text(value)]
#     prior_Searches += [sg.Text(address)]

#     print(prior_Searches)
#col1=[sg.Column(name)]


layout = []
layout += [[sg.Button("Back")], [sg.Text("Previous Evaluation", size=(40,5))]]
# for x in range(0,(l-1)):
#     layout += [searchList(x)] + [sg.Text({x})]
layout += [searchList(x) for x in range(0,l)]
#[[sg.Column(name),sg.Column(value), sg.Column(address)]]

window=sg.Window("Previous Evaluation",layout)

while True:
    event,values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == "Back":
        break
window.close()