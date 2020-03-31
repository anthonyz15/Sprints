import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk,Image
import time

Buildinglist={}
data=[]
hitbox=[]

xbox=[]
ybox=[]

global player,player1

root = tk.Tk()  # lib kinter

root.title("Game")
root.geometry("1024x700")  # Width x Height

canva = tk.Canvas(root, width=1024, height=650)
canva.config(bg="grey")
canva.pack()
root.update()

player1 = Image.open("Player.png")
player1 = player1.resize((75, 75), Image.ANTIALIAS)
player1 = ImageTk.PhotoImage(player1)


def loadMap():
    global canva,bg_load,draw_theloadmap,Buildinglist,player
    file_path = filedialog.askopenfilename()
    with open(file_path, "r") as ifile:
        for line in ifile:
            if line.startswith("Background:"):
                bg=line[11:-1]
        data=open(file_path, "r").read()
        data=data.split("Building:")
        data.pop(0)
        Buildinglist=data


    bg_load(bg,"Player.png")
    player = canva.create_image(100,100,image=player1,anchor='sw')
    canva.move(player, 150, 550)

def min_max(drawwall):
    global canva,xbox,ybox
    xmax=0
    ymax=0
    xmin = 0
    ymin = 0
    for i in drawwall:
        x=i.split(",")
        x1=x[0][3:]
        y1 = x[1][4:]
        x2 = x[2][4:]
        y2 = x[3][4:]
        line=canva.create_line(x1,y1,x2,y2, width=3,state='hidden')
        print(canva.coords(line))
        pos=canva.coords(line)
        if pos[0]>xmax or xmax==0:
            xmax=pos[0]
        if pos[0]<xmin or xmin==0:
            xmin=pos[0]
        if pos[2]>xmax or xmax==0:
            xmax=pos[2]
        if pos[2]<xmin or xmin==0:
            xmin=pos[2]
        if pos[1]>ymax or ymax==0:
            ymax=pos[1]
        if pos[1]<ymin or ymin==0:
            ymin=pos[1]
        if pos[3]>ymax or ymax==0:
            ymax=pos[3]
        if pos[3]<ymin or ymin==0:
            ymin=pos[3]
    xbox.append(str(xmin)+","+str(xmax))
    ybox.append(str(ymin)+ "," +str(ymax))
    print(xbox)
    print(ybox)

def draw_theloadmap(drawwall):
    global canva
    for i in drawwall:
        x=i.split(",")
        x1=x[0][3:]
        y1 = x[1][4:]
        x2 = x[2][4:]
        y2 = x[3][4:]
        line=canva.create_line(x1,y1,x2,y2, width=3)



def Building_cut(building):
    wall_draw=[]
    draw = building.split("\n")
    for line in draw:
        if line.startswith("Wall:"):
            print(line[5:])
            wall = line[5:]
            wall_draw.append(wall)
    return wall_draw

def bg_load(bg,player):
    global canva
    #canva2 = ImageTk.PhotoImage(file=player)
    #canva.create_image(100, 100, image=canva2, anchor=NW)
    canva.image = ImageTk.PhotoImage(file=bg)
    canva.create_image(0,0, image=canva.image, anchor=NW)
    canva.pack()

def leftkey(event):
    global canva,player,root,time,starts,end,xbox,ybox,data,draw_theloadmap
    loop=len(xbox)
    print("left")
    canva.move(player, -5, 0)
    pos=canva.coords(player)
    print(pos)
    if pos[0]<=0:
        canva.move(player, 5, 0)
    for i in range(loop):
        x=xbox[i].split(",")
        y=ybox[i].split(",")
        if float(x[0])<=pos[0]<=float(x[1]) and (float(y[0])<=pos[1]<=float(y[1])+70):
            canva.move(player, 5, 0)
            draw_theloadmap(data[i])
    root.update_idletasks()
    root.update()
    time.sleep(0.01)

def rightkey(event):
    global canva, player,root,time,xbox,ybox,data,draw_theloadmap
    loop = len(xbox)
    print("right")
    canva.move(player, 5, 0)
    pos = canva.coords(player)
    print(pos)
    if pos[0] >= 950:
        canva.move(player, -5, 0)
    for i in range(loop):
        x = xbox[i].split(",")
        y = ybox[i].split(",")
        if float(x[0])-60 <= pos[0] <= float(x[1]) and (float(y[0]) <= pos[1] <= float(y[1])+70):
            canva.move(player, -5, 0)
            draw_theloadmap(data[i])
    root.update_idletasks()
    root.update()
    time.sleep(0.01)
    
def upkey(event):
    global canva, player,root,time,xbox,ybox,data,draw_theloadmap
    loop = len(xbox)
    print("up")
    canva.move(player, 0, -5)
    pos = canva.coords(player)
    print(pos)
    if pos[1] <= 80:
        canva.move(player, 0, 5)
    for i in range(loop):
        x = xbox[i].split(",")
        y = ybox[i].split(",")
        if float(x[0])-60 <= pos[0] <= float(x[1]) and (float(y[0]) <= pos[1] <= float(y[1])+70):
            canva.move(player, 0, 5)
            draw_theloadmap(data[i])
    root.update_idletasks()
    root.update()
    time.sleep(0.01)
    
def downkey(event):
    global canva, player,root,time,xbox,ybox,data,draw_theloadmap
    loop = len(xbox)
    print("down")
    canva.move(player, 0, 5)
    pos = canva.coords(player)
    print(pos)
    if pos[1] >= 650:
        canva.move(player, 0, -5)
    for i in range(loop):
        x = xbox[i].split(",")
        y = ybox[i].split(",")
        if float(x[0])-60 <= pos[0] <= float(x[1]) and (float(y[0]) <= pos[1] <= float(y[1])):
            canva.move(player, 0, -5)
            draw_theloadmap(data[i])
    root.update_idletasks()
    root.update()
    time.sleep(0.01)
    
#map load
loadMap()
for i in Buildinglist:
     data.append(Building_cut(Buildinglist[Buildinglist.index(i)]))
     min_max(data[Buildinglist.index(i)])


root.bind('<Left>', leftkey)
root.bind('<Right>', rightkey)
root.bind('<Up>', upkey)
root.bind('<Down>', downkey)

root.mainloop()

'''

Nombre: loadMap

Objectivo: Seleccionar un archivo que contenga un mapa y cargarlo para poder jugar.

Precondiciones: Se presiona el botón de 'load'.

Postcondiciones: Se cargará un mapa para jugar.

Argumentos: N/A

Autor: Anthony Cuevas

Fecha: 27 de marzo de 2020

###

Nombre: min_max

Objectivo: Función para determinar las coordenadas maximas y minimas de una pared.

Precondiciones: Se va a dibujar un edificio.

Postcondiciones: Se determina los valores maximos y minimos de la pared.

Argumentos: drawwall => pared de un edificio a ser dibujado

Autor: Jean Merced

Fecha: 27 de marzo de 2020

###

Nombre: draw_theloadmap

Objectivo: Dibujar las líneas en la pantalla que representan las paredes del
edificio cuando se carga un mapa existente.

Precondiciones: Se cargará un mapa.

Postcondiciones: Se dibuja en pantalla las líneas que representa las paredes.

Argumentos: drawwall => arreglo de paredes, contiene las coordenadas de los
extremos de las paredes.

Autor: Anthony Cuevas

Fecha: 27 de marzo de 2020

###

Nombre: Building_cut

Objectivo: Extraer información sobre las paredes de un edificio.

Precondiciones: Se tiene información sobre edificios.

Postcondiciones: Se guarda la información de las paredes en un arreglo.

Argumentos: building => edificio cuya información de paredes va a ser extraída.

Autor: Irving Lazu

Fecha: 28 de marzo de 2020

###

Nombre: bg_load

Objectivo: Función interna para cargar la imagen de fondo correspondiente al mapa que 
se pretende cargar.

Precondiciones: Se cargará un mapa.

Postcondiciones: El mapa que se cargará tendrá la imagen de fondo correspondiente.

Argumentos: bg => la ruta del archivo de la imagen de fondo.

Autor: Anthony Cuevas

Fecha: 7 de marzo de 2020

###

Nombre: leftkey

Objectivo: Mover el jugador hacia la izquierda en el mapa.

Precondiciones: Se presiona la tecla de 'izquierda'.

Postcondiciones: La imagen del jugador se desplaza hacia la izquierda en el mapa.

Argumentos: event => la tecla de 'izquierda' fue presionada

Autor: Irving Lazu

Fecha: 28 de marzo de 2020

###

Nombre: rightkey

Objectivo: Mover el jugador hacia la derecha en el mapa.

Precondiciones: Se presiona la tecla de 'derecha'.

Postcondiciones: La imagen del jugador se desplaza hacia la derecha en el mapa.

Argumentos: event => la tecla de 'derecha' fue presionada

Autor: Irving Lazu

Fecha: 28 de marzo de 2020

###

Nombre: upkey

Objectivo: Mover el jugador hacia arriba en el mapa.

Precondiciones: Se presiona la tecla de 'arriba'.

Postcondiciones: La imagen del jugador se desplaza hacia arriba en el mapa.

Argumentos: event => la tecla de 'arriba' fue presionada

Autor: Enrique Marrero

Fecha: 28 de marzo de 2020

###

Nombre: downkey

Objectivo: Mover el jugador hacia abajo en el mapa.

Precondiciones: Se presiona la tecla de 'abajo'.

Postcondiciones: La imagen del jugador se desplaza hacia abajo en el mapa.

Argumentos: event => la tecla de 'abajo' fue presionada

Autor: Enrique Marrero

Fecha: 28 de marzo de 2020

'''
