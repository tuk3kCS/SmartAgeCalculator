import PySimpleGUI as sg

layout = [
    [
        sg.Text('Nhập tuổi của bạn', key = '-TEXT-'),
        sg.Input(key = '-INPUT-'),
        sg.Button('Tính tuổi của bạn', key = '-BUTTON-'),
    ],
    [sg.Text(key = '-OUTPUT-')]
]

window = sg.Window('Máy tính tuổi thông minh', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-BUTTON-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            window['-OUTPUT-'].update(f'Bạn đã {input_value} tuổi rồi.')
        else:
            window['-OUTPUT-'].update(f'{input_value} là tuổi clgt???')

window.close()