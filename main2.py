
from tkinter import *
from tkinter import ttk 
import pytz
import pycountry_convert
from PIL import Image, ImageTk


# biblioteca para Criar GUIs simples e funcionais com tkinter.
# Usar widgets básicos e temáticos para criar janelas interativas.
# Melhorar a aparência da interface com widgets do ttk.

#importações
import requests
from datetime import datetime
import json

import pytz
import pycountry_convert as pc 



#################cores ###############
cor0 = "#444466"  # Preta
cor1 = "#feffff"  # branca
cor2 = "#6f9fbd"  # azul

fundo_dia="#6cc4cc"
fundo_noite="#778899"
fundo_tarde = "#bfb86d"

fundo = fundo_dia

# Janela principal
janela = Tk()
janela.title("")
janela.geometry("320x350")
janela.configure(bg=fundo)

#Linha Separadora
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)


#criando frames
frame_top = Frame(janela, width=320, height=50, bg=cor1,pady=0, padx=0)
frame_top.grid(row=1, column=0)

frame_corpo = Frame(janela, width=320, height=300, bg=fundo ,pady= 12, padx=0)
frame_corpo.grid(row=2, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use("clam")

#Função que retorna as informaões
def informacao():
    
    chave = "e069c7ba0bd563cca4907242a77ba4ee"
    cidade = e_local.get()
    api_link = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(cidade, chave)

    #chamada do api usando request
    r = requests.get(api_link)

    #Convertendo os dados presentes na variavel r em dicionario
    dados = r.json()
    print(dados)

    # Informações para app de clima zona, país e hora
    pais_codigo = dados["sys"]["country"]

    # Zona
    zona_fuso = pytz.country_timezones[pais_codigo]

    # #País
    pais = pytz.country_names[pais_codigo]
    print(pais)

    #data
    zona = pytz.timezone(zona_fuso[0])
    zona_horas = datetime.now(zona)
    zona_horas = zona_horas.strftime("%d %m %Y | %H:%M:%S")



    # tempo 
    tempo = dados["main"]["temp"]
    humidade = dados["main"]["humidity"]
    descricao = dados["weather"][0]["description"]


    #Alterçãoes de informações
    def pais_para_continente(i):
        pais_alpha = pc.country_name_to_country_alpha2(i)
        pais_continent_codigo = pc.country_alpha2_to_continent_code(pais_alpha)
        pais_continente_nome = pc.convert_continent_code_to_continent_name(pais_continent_codigo)

        return pais_continente_nome 

    continente = pais_para_continente(pais)

#passando informacoes nas labels
    l_cidade["text"] =  cidade + ' - ' + pais + " / " + continente 
    data["text"] =  zona_horas
    umidade["text"] = umidade 

# Frame top
e_local = Entry(frame_top, width=16, justify="left", font=("", 14), highlightthickness=1, relief="solid")
e_local.place(x=15, y=10)
b_ver= Button(frame_top, command=informacao, text="Check seu clima", bg=cor1, fg=cor2, font=("Ivy 9 bold"), highlightthickness=1, relief="raised", overrelief=RIDGE)
b_ver.place(x=200, y=10)

# Frame corpo
l_cidade = Label(frame_corpo, text="", anchor="center", bg=fundo, fg=cor1, font=("Arial 14"))
l_cidade.place(x=10, y=4)

data = Label(frame_corpo, text="", anchor="center", bg=fundo, fg=cor1, font=("Arial 10"))
data.place(x=10, y=54)

umidade = Label(frame_corpo, text="", anchor="center", bg=fundo, fg=cor1, font=("Arial 45"))
umidade.place(x=10, y=100)

h_porcentagem = Label(frame_corpo, text="%", anchor="center", bg=fundo, fg=cor1, font=("Arial 10 bold"))
h_porcentagem.place(x=85, y=110)

h_nome = Label(frame_corpo, text="Umidade", anchor="center", bg=fundo, fg=cor1, font=("Arial 8"))
h_nome.place(x=85, y=140)


#icons imagem

imagem = Image.open("D:/Curso Python/projetos/icons/sol.png")
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)

icons = Label(frame_corpo, image=imagem,  bg=fundo)
icons.place(x=160, y=50)

descricao = Label(frame_corpo, text="Ensolarado ", anchor="center", bg=fundo, fg=cor1, font=("Arial 10"))
descricao.place(x=170, y=190)

imagem = Image.open("./icons/nuvem noite.png")
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)

icons = Label(frame_corpo, image=imagem,  bg=fundo)
icons.place(x=160, y=50)
descricao = Label(frame_corpo, text="Nublado", anchor="center", bg=fundo, fg=cor1, font=("Arial 10"))
descricao.place(x=170, y=190)


imagem = Image.open("D:/Curso Python/projetos/icons/lua.png")
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)

icons = Label(frame_corpo, image=imagem,  bg=fundo)
icons.place(x=160, y=50)
descricao = Label(frame_corpo, text="text", anchor="center", bg=fundo, fg=cor1, font=("Arial 10"))
descricao.place(x=170, y=190)

imagem = Image.open("D:/Curso Python/projetos/icons/nuvem dia.png")
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)



#Mantém a janela aberta até o usuário fechá-la manualmente
janela.mainloop()

