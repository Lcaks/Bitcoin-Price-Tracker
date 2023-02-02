from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

import requests
import json

co0 = "#444466"  # Preta / black
co1 = "#feffff"  # branca / white 
co2 = "#6f9fbd"  # azul / blue

fundo = "#f5c96c" #background

janela = Tk()
janela.title('Bitcoin Price')
janela.geometry('320x350')
janela.iconbitmap('image/bitcoin.ico')
janela.resizable(width=False, height=False)
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_cima = Frame(janela, width=320, height=50, bg=co1, pady=0, padx=0, relief='flat') 
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=320, height=300, bg=fundo, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=2, column=0, sticky=NW)

def info():
    api_link = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,BRL'

    response = requests.get(api_link)

    dados = response.json()

    valor_usd = float(dados['USD'])
    valor_formatado_usd = '${:,.3f}'.format(valor_usd)

    valor_brl = float(dados['BRL'])
    valor_formatado_brl = 'R${:,.3f}'.format(valor_brl)

    l_p_usd['text'] = valor_formatado_usd
    l_p_brl['text'] = valor_formatado_brl

    frame_baixo.after(5000, info)

imagem = Image.open('image/bit.png')
imagem = imagem.resize((30,30), Image.LANCZOS)
imagem = ImageTk.PhotoImage(imagem)

l_icon = Label(frame_cima, image=imagem, compound=LEFT, bg=co1,relief=FLAT)
l_icon.place(x=10, y=10)

l_nome = Label(frame_cima, text="BITCOIN PRICE TRACKER", bg=co1, fg=co2, relief=FLAT, anchor='center', font=('Arial 15'))
l_nome.place(x=55, y=12)

l_p_usd = Label(frame_baixo, text='', bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 25'))
l_p_usd.place(x=67, y=50)

l_p_brl = Label(frame_baixo, text='', bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 15'))
l_p_brl.place(x=87, y=110)

info()

janela.mainloop()
