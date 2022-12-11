import customtkinter
from tkinter import *
import random

import config.config as config

customtkinter.set_appearance_mode("light")
window = customtkinter.CTk()
window.geometry("1280x720")
window.title("DinoGame")
window.minsize(500, 500)

mainbox = customtkinter.CTkFrame(master=window, width= 1024, height=config.tabuleiroy)
mainbox.place(relx=0.5, rely=0.5, anchor=CENTER)

botoes = customtkinter.CTkLabel(master=mainbox, text="Botões\n\nW - Cima\nA - Esquerda\nS - Direita\nD - Baixo\nR - Restart")
botoes.place(x=94, y=20)

instrucoes = customtkinter.CTkLabel(master=mainbox, text="Instruções\n\n*Capture os verdes\n*Fuja do vermelho\n*Conclua o jogo\ncom 100 pontos")
instrucoes.place(x=838, y=160)

objetivo = customtkinter.CTkLabel(master=mainbox, text="Missões\n\nFaça 10 pontos\nFaça 20 pontos\nFaça 30 pontos\nFaça 50 pontos\nFaça 100 pontos")
objetivo.place(x=850, y=20)

box = customtkinter.CTkFrame(master=mainbox, width=config.tabuleirox, height=config.tabuleiroy)
box.place(relx=0.5, rely=0.5, anchor=CENTER)

label = customtkinter.CTkLabel(master=box, text="Score: 0")
label.place(x=20, y=20)

fruta = Frame(master=box, width=config.playerwidth, height=config.playerheight, background=config.fcolor)
fruta.place(x=100 ,y=100)

player = customtkinter.CTkFrame(master=box, width=config.playerwidth, height=config.playerheight)
player._set_appearance_mode("dark")
player.place(x=50 ,y=50)

inimigo = Frame(master=box, width=config.playerwidth, height=config.playerheight, background=config.icolor)
inimigo.place(x=config.tabuleirox + (inimigo.winfo_x() * 2))

def key_pressed(e):
    if config.pause == False:
        if player.winfo_x() > 0:
            if e.char == "a" or e.char == "A":
                player.place(x=player.winfo_x() - config.playerspeed)
                posiçãoupdate()

        if player.winfo_x() < config.tabuleirox - config.playerwidth:
            if e.char == "d" or e.char == "D":
                player.place(x=player.winfo_x() + config.playerspeed)
                posiçãoupdate()

        if player.winfo_y() > 0:
            if e.char == "w" or e.char == "W":
                player.place(y=player.winfo_y() - config.playerspeed)
                posiçãoupdate()

        if player.winfo_y() < config.tabuleiroy - config.playerheight:
            if e.char == "s" or e.char == "S":
                player.place(y=player.winfo_y() + config.playerspeed)
                posiçãoupdate()

    if e.char == "r" or e.char == "R":
        config.pause = False
        config.score = 0
        label.configure(text="Score: " + str(config.score))
        inimigo.place(x=config.tabuleirox + (inimigo.winfo_x() * 2))

window.bind("<Key>",key_pressed)

def posiçãoupdate():
    if player.winfo_x() == fruta.winfo_x() and player.winfo_y() == fruta.winfo_y():
        config.score += 1
        frutaupdate()
        label.configure(text="Score: " + str(config.score))

    inimigoMove()
    fimjogo()

def frutaupdate():
    novaposicaox = random.randint(0, (config.tabuleirox/config.frutaheight)-1)
    novaposicaoy = random.randint(0, (config.tabuleirox/config.frutaheight)-1)
    fruta.place(x = novaposicaox * config.frutawidth, y=novaposicaoy * config.frutawidth)

def inimigoMove():
    move = random.randint(1, 4)

    if move == 1:
        if int(inimigo.winfo_x()) < int(player.winfo_x()):
            inimigoleft = inimigo.winfo_x() + config.inimigowidth
            inimigo.place(x=inimigoleft)

        if int(inimigo.winfo_x()) > int(player.winfo_x()):
            inimigoleft = inimigo.winfo_x() - config.inimigowidth
            inimigo.place(x=inimigoleft)

        if int(inimigo.winfo_y()) < int(player.winfo_y()):
            inimigoleft = inimigo.winfo_y() + config.inimigowidth
            inimigo.place(y=inimigoleft)

        if int(inimigo.winfo_y()) > int(player.winfo_y()):
            inimigoleft = inimigo.winfo_y() - config.inimigowidth
            inimigo.place(y=inimigoleft)

def fimjogo():
    if inimigo.winfo_x() == player.winfo_x() and inimigo.winfo_y() == player.winfo_y():
        label.configure(text="Score: " + str(config.score) + "\nFim de jogo")
        config.pause = True

window.mainloop()