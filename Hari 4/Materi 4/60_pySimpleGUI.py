import PySimpleGUI as sg

layout = [[sg.Button('klik saya')]]

window = sg.Window('Contoh Program PySimpleGUI', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'klik saya':
        print('Tombol diklik')

window.close()
