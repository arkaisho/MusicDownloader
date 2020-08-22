import PySimpleGUI as sg
import subprocess
import os
import time

sg.theme('LightGrey1')	

inputLayout = [[sg.Text('Digite a URL do site'), sg.InputText()],[sg.Text("",size=(60,1),key="STATUS")],[sg.Button('Baixar',key="BAIXAR"), sg.Button('Sair',key="SAIR")] ]
inputWindow = sg.Window('Download', inputLayout)

def execute(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line 
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)

while True:
    event, values = inputWindow.read()
    if event == sg.WIN_CLOSED or event == 'SAIR':	
        break
    if event == 'BAIXAR':
        #LOCK WINDOW
        inputWindow["STATUS"].update("Baixando ...")
        inputWindow["BAIXAR"].update(disabled=True)
        inputWindow["SAIR"].update(disabled=True)
        inputWindow.refresh()
        #DOWNLOAD
        cmd = ['youtube-dl','-xic','--yes-playlist','--audio-format','mp3','-o','Musicas/%(uploader)s/%(title)s.%(ext)s',values[0]]
        for path in execute(cmd):
            inputWindow["STATUS"].update(path)
            inputWindow.refresh()
        #result = subprocess.run(['youtube-dl','-xic','--yes-playlist','--audio-format','mp3','-o','Musicas/%(channel)s/%(title)s.%(ext)s',values[0]], stdout=subprocess.PIPE)
        #UNLOCK WINDOW
        #if(result.stdout.decode('utf-8')==""):
        #    inputWindow["STATUS"].update("Erro ao realizar o download")
        #else:
        inputWindow["STATUS"].update("Download completo")
        inputWindow["BAIXAR"].update(disabled=False)
        inputWindow["SAIR"].update(disabled=False)
inputWindow.close()
