import PySimpleGUI as sg
#layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key= 'usuario',size=(20,1))],
    [sg.Text('Senha') , sg.Input(key='senha' , password_char= '*',size=(20,1) )],
    [sg.Checkbox('Salvar login?')],
    [sg.Button('Entrar')]
]
#janela
janela = sg.Window('Login',layout)
#ler eventos
while True:
   eventos, valores = janela.read()
   if eventos == sg.WINDOW_CLOSED:
       break
   if eventos == 'Entrar':
       if valores['usuario'] == 'Gabriela' and valores['senha'] == '123456':
           print('Bem Vinda')
