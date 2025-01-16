from PySimpleGUI import PySimpleGUI as sg
sg.theme('Reddit')
layout = [
    [sg.Text('Painel Login')],
    [sg.Text('Username:'),sg.Input(key='Username')],
    [sg.Text('Senha:'),sg.Input(key='Senha',password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
window = sg.Window('Login painel',layout)
while True:
    Events, values = window.read()