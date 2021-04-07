import PySimpleGUI as sg


layout = [[sg.Text("Processing Property Evaluation")],
    [sg.ProgressBar(max_value=1000, orientation='h', bar_color="red",key="progressbar")],
    [sg.Cancel()]]

window=sg.Window("Property Evaluation Progress",layout)
progress_bar = window['progressbar']

for i in range(0, 1000):
    event, values = window.read()
    if event == 'Cancel' or event == sg.WIN_CLOSED:
        break
    else:
        progress_bar.UpdateBar(i+1)
window.close()