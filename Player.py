import threading
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import time
import random
import webbrowser

Buildinglist={}
data=[]
hitbox=[]
BuildingRemaining=None

xbox=[]
ybox=[]
xcen=[None] * 5
ycen=[None] * 5

global player,questionfile,player1,t1,t2,t3,clicked1,clicked2,clicked3,clicked4,bpicture,bpic,back,top,repeat,correct1,correct2,correct3,correct4,map3d,vrml

picnum=0

playerleft=[None]*3
selectplayerleft=0
playerright=[None]*3
selectplayerright=0
playerdown=[None]*3
selectplayerdown=0
playerup=[None]*3
selectplayerup=0
repeat=[]
toplevel=False

img=[None]*10
root = tk.Tk()  # lib kinter

root.title("Game")
root.geometry("1366x700")  # Width x Height

canva = tk.Canvas(root, width=1366, height=650)
canva.config(bg="grey")
canva.pack()
root.update()


t1 = Image.open("tree1.png")
t1 = t1.resize((100, 100), Image.ANTIALIAS)
t1 = ImageTk.PhotoImage(t1)

t2 = Image.open("tree2.png")
t2 = t2.resize((100, 100), Image.ANTIALIAS)
t2 = ImageTk.PhotoImage(t2)

t3 = Image.open("tree3.png")
t3 = t3.resize((100, 100), Image.ANTIALIAS)
t3 = ImageTk.PhotoImage(t3)

Remaining = tk.Label(root, text="Building Remaining").place(x=30, y=660)

text_widget = tk.Text(root, width=10,height=1)
text_widget.place(x=150, y=660)
clicked= StringVar()
clicked.set("Player 1")
drop= OptionMenu(root,clicked,"Player 1","Player 2","Player 3")
drop.place(x=450, y=655)


def playersel(p):
    global  player1,playerleft,playerright,playerup,playerdown,player
    player1 = Image.open("sprites/"+p+"027.png")
    player1 = player1.resize((75, 75), Image.ANTIALIAS)
    player1 = ImageTk.PhotoImage(player1)
    player = canva.create_image(100, 100, image=player1, anchor='sw')
    canva.move(player, 10, 520)

    playerleft[0] = Image.open("sprites/"+p+"010.png")
    playerleft[0] = playerleft[0].resize((75, 75), Image.ANTIALIAS)
    playerleft[0] = ImageTk.PhotoImage(playerleft[0])

    playerleft[1] = Image.open("sprites/"+p+"009.png")
    playerleft[1] = playerleft[1].resize((75, 75), Image.ANTIALIAS)
    playerleft[1] = ImageTk.PhotoImage(playerleft[1])

    playerleft[2] = Image.open("sprites/"+p+"011.png")
    playerleft[2] = playerleft[2].resize((75, 75), Image.ANTIALIAS)
    playerleft[2] = ImageTk.PhotoImage(playerleft[2])

    playerright[0] = Image.open("sprites/"+p+"028.png")
    playerright[0] = playerright[0].resize((75, 75), Image.ANTIALIAS)
    playerright[0] = ImageTk.PhotoImage(playerright[0])

    playerright[1] = Image.open("sprites/"+p+"027.png")
    playerright[1] = playerright[1].resize((75, 75), Image.ANTIALIAS)
    playerright[1] = ImageTk.PhotoImage(playerright[1])

    playerright[2] = Image.open("sprites/"+p+"029.png")
    playerright[2] = playerright[2].resize((75, 75), Image.ANTIALIAS)
    playerright[2] = ImageTk.PhotoImage(playerright[2])

    playerdown[0] = Image.open("sprites/"+p+"018.png")
    playerdown[0] = playerdown[0].resize((75, 75), Image.ANTIALIAS)
    playerdown[0] = ImageTk.PhotoImage(playerdown[0])

    playerdown[1] = Image.open("sprites/"+p+"020.png")
    playerdown[1] = playerdown[1].resize((75, 75), Image.ANTIALIAS)
    playerdown[1] = ImageTk.PhotoImage(playerdown[1])

    playerdown[2] = Image.open("sprites/"+p+"024.png")
    playerdown[2] = playerdown[2].resize((75, 75), Image.ANTIALIAS)
    playerdown[2] = ImageTk.PhotoImage(playerdown[2])

    playerup[0] = Image.open("sprites/"+p+"000.png")
    playerup[0] = playerup[0].resize((75, 75), Image.ANTIALIAS)
    playerup[0] = ImageTk.PhotoImage(playerup[0])

    playerup[1] = Image.open("sprites/"+p+"002.png")
    playerup[1] = playerup[1].resize((75, 75), Image.ANTIALIAS)
    playerup[1] = ImageTk.PhotoImage(playerup[1])

    playerup[2] = Image.open("sprites/"+p+"006.png")
    playerup[2] = playerup[2].resize((75, 75), Image.ANTIALIAS)
    playerup[2] = ImageTk.PhotoImage(playerup[2])

def loadMap():
    global canva,bg_load,draw_theloadmap,Buildinglist,player,loadtree,BuildingRemaining,text_widget,questionfile,vrml
    trees = []
    locat = []
    bg=" "
    file_path = filedialog.askopenfilename()
    vrmlname = file_path.split("/")
    vrmlname = vrmlname[len(vrmlname) - 1]
    vrml=vrmlname[:-4]
    print(vrml)
    with open(file_path, "r") as ifile:
        for line in ifile:
            if line.startswith("Background:"):
                bg=line[11:-1]
            if line.startswith("TreeType:"):
                print(line[9:])
                treetype=line[9:15]
                location=line[26:]
                location=location.replace(")","")
                print(treetype,location)
                trees.append(treetype)
                locat.append(location)
            if line.startswith("QuestionsFile:"):
                questionfile=line[14:]
        data=open(file_path, "r").read()
        data=data.split("Building:")
        data.pop(0)
        Buildinglist=data
    if bg == " ":
        pass
    else:
        bg_load(bg)
    for i in range(len(trees)):
        loadtree(trees[i],locat[i])
    BuildingRemaining=len(Buildinglist)
    text_widget.insert(INSERT, '%d\n' % (BuildingRemaining))
def loadtree(treetype,location):
    global tree1,tree2,canva,root
    locat=location.split(",")
    x=int(locat[0])
    y=int(locat[1])
    if treetype == "Tree 1":
        canva.create_image(x, y, image=t1,anchor='nw')
        canva.pack()
    if treetype == "Tree 2":
        canva.create_image(x, y, image=t2,anchor='nw')
        canva.pack()
    if treetype == "Tree 3":
        canva.create_image(x, y, image=t3,anchor='nw')
        canva.pack()

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
        if pos[1]<xmin or ymin==0:
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

def bg_load(bg):
    global canva,img
    img[0] = Image.open(bg)
    img[0] = img[0].resize((1366, 700), Image.ANTIALIAS)
    img[0] = ImageTk.PhotoImage(img[0])
    back=canva.create_image(0, 0, image=img[0], anchor=NW)
    canva.tag_lower(back)
    canva.pack()
def Map3D():
    global webbrowser,vrml
    print("3D")
    webbrowser.open(vrml+".wrl")

def bpic_load(bpic):
    global canva,bpicture,back,BuildingRemaining,xcen,ycen,picnum,Map3D
    xCenter = (float(xcen[0]) + float(xcen[1])) / 2.0
    yCenter = (float(ycen[0]) + float(ycen[1])) / 2.0
    print(xCenter,yCenter)
    print(len(bpicture))
    bpicture[picnum] = Image.open(bpic)
    bpicture[picnum] = bpicture[picnum].resize((100, 100))
    bpicture[picnum] = ImageTk.PhotoImage(bpicture[picnum])
    back=canva.create_image(xCenter,yCenter, image=bpicture[picnum], anchor=NW)
    canva.move(back,-50,-50)
    canva.pack()
    BuildingRemaining-=1
    picnum+=1
    text_widget.delete("1.0", END)
    text_widget.insert(INSERT, '%d\n' % (BuildingRemaining))
    if BuildingRemaining==0:
        map3d = tk.Button(root, text="Map in 3D", command=Map3D, width=10).place(x=600, y=660)




def questions(question):
    global submit,clicked1,clicked2,clicked3,clicked4,Buildinglist,bpic,top,random,correct1,correct2,correct3,correct4
    data = open(questionfile, "r").read()
    data = data.split("Building:")
    data.pop(0)
    que=[]
    q=""
    r=""
    w=[]
    bpic=Buildinglist[question].split('\n')
    data=data[question].split('Question')
    data.pop(0)
    print(data)
    for line in bpic:
        if line.startswith("BuildingImage:"):
            bpic = line[14:]
            print(bpic)
    for qu in data:
        d = qu.split('\n')
        for line in d:
            if line.startswith(":"):
                print(line[1:])
                q = line[1:]
            if line.startswith("Right:"):
                r=line
                print(r)
            if line.startswith("Wrong:"):
                w.append(line)
                print(w)
        temp=q+'\n'+r+'\n'+w[0]+'\n'+w[1]+'\n'+w[2]+'\n'
        #w=[]
        que.append(temp)
        print(temp)
    top = Toplevel()  # lib kinter
    top.title("Pregunta")
    top.geometry("600x650")
    text_widget1 = tk.Text(top, width=50, height=7)
    text_widget1.place(x=15, y=50)
    text_widget2 = tk.Text(top, width=50, height=7)
    text_widget2.place(x=15, y=200)
    text_widget3 = tk.Text(top, width=50, height=7)
    text_widget3.place(x=15, y=350)
    text_widget4 = tk.Text(top, width=50, height=7)
    text_widget4.place(x=15, y=500)

    q1=random.choice(que)
    q1=q1.split('\n')
    q2=random.choice(que)
    q2 = q2.split('\n')
    q3=random.choice(que)
    q3 = q3.split('\n')
    q4=random.choice(que)
    q4 = q4.split('\n')
    ## listas para que sea random##

    list1 = []
    while len(list1)!=4:
        r = random.randint(1, 4)
        if r not in list1: list1.append(r)
    for i in list1:
        if i==1: correct1=list1.index(i)+1

    list2 = []
    while len(list2) != 4:
        r = random.randint(1, 4)
        if r not in list2: list2.append(r)
    for i in list2:
        if i == 1: correct2 = list2.index(i) + 1

    list3 = []
    while len(list3) != 4:
        r = random.randint(1, 4)
        if r not in list3: list3.append(r)
    for i in list3:
        if i == 1: correct3 = list3.index(i) + 1

    list4 = []
    while len(list4) != 4:
        r = random.randint(1, 4)
        if r not in list4: list4.append(r)
    for i in list4:
        if i == 1: correct4 = list4.index(i) + 1
    ########################################################

    text_widget1.insert(INSERT,"Question:%s \n 1:%s \n 2:%s \n 3:%s \n 4:%s" % (q1[0],q1[list1[0]][6:],q1[list1[1]][6:],q1[list1[2]][6:],q1[list1[3]][6:]))
    text_widget2.insert(INSERT, "Question:%s \n 1:%s \n 2:%s \n 3:%s \n 4:%s" % (q2[0],q2[list2[0]][6:],q2[list2[1]][6:],q2[list2[2]][6:],q2[list2[3]][6:]))
    text_widget3.insert(INSERT, "Question:%s \n 1:%s \n 2:%s \n 3:%s \n 4:%s" % (q3[0],q3[list3[0]][6:],q3[list3[1]][6:],q3[list3[2]][6:],q3[list3[3]][6:]))
    text_widget4.insert(INSERT, "Question:%s \n 1:%s \n 2:%s \n 3:%s \n 4:%s" % (q4[0],q4[list4[0]][6:],q4[list4[1]][6:],q4[list4[2]][6:],q4[list4[3]][6:]))

    clicked1 = StringVar()
    clicked1.set("Option 1")
    drop1 = OptionMenu(top, clicked1, "Option 1", "Option 2", "Option 3", "Option 4")
    drop1.place(x=460, y=60)

    clicked2 = StringVar()
    clicked2.set("Option 1")
    drop2 = OptionMenu(top, clicked2, "Option 1", "Option 2", "Option 3", "Option 4")
    drop2.place(x=460, y=210)

    clicked3 = StringVar()
    clicked3.set("Option 1")
    drop3 = OptionMenu(top, clicked3, "Option 1", "Option 2", "Option 3", "Option 4")
    drop3.place(x=460, y=360)

    clicked4 = StringVar()
    clicked4.set("Option 1")
    drop4 = OptionMenu(top, clicked4, "Option 1", "Option 2", "Option 3", "Option 4")
    drop4.place(x=460, y=510)

    time.sleep(1)
    tk.Button(top, text="Submit", command=submit, width=10).place(x=500, y=610)

def askoption(i):
    global messagebox
    rep=False
    for n in repeat:
        if n==i:
            rep=True
    if rep==True:
        pass
    else:
        repeat.append(i)
        result=messagebox.askquestion("Answer the quiz?")
        if result == 'yes':
            questions(i)
        elif result == 'no':
            repeat.pop()


def submit():
    global canva,bpic,bpic_load,top,messagebox
    print("submit")
    print(correct1)
    print(correct2)
    print(correct3)
    print(correct4)
    count=0
    if clicked1.get() == "Option "+str(correct1):
        count+=1
    if clicked2.get() == "Option "+str(correct2):
        count += 1
    if clicked3.get() == "Option "+str(correct3):
        count += 1
    if clicked4.get() == "Option "+str(correct4):
        count += 1
    if count>=3:
        bpic_load(bpic)
        top.destroy()
    else:
        messagebox.showinfo("Wrong anwser")
        repeat.pop()

def leftkey(event):
    global canva,player,root,time,starts,end,xbox,ybox,data,draw_theloadmap,xcen,ycen,playerleft,selectplayerleft
    loop=len(xbox)
    characterpos = canva.coords(player)
    canva.delete(player)
    player = canva.create_image(characterpos[0],characterpos[1],image=playerleft[selectplayerleft],anchor='sw')
    selectplayerleft+=1
    if selectplayerleft>2:
        selectplayerleft=0
    canva.move(player, -5, 0)
    pos=canva.coords(player)
    print(pos)
    if pos[0]<=-25:
        canva.move(player, 5, 0)
    for i in range(loop):
        x=xbox[i].split(",")
        y=ybox[i].split(",")
        if float(x[0])<=pos[0]<=float(x[1]) and (float(y[0])<=pos[1]<=float(y[1])+70):
            canva.move(player, 5, 0)
            xcen[0] = x[0]
            ycen[0] = y[0]
            xcen[1] = x[1]
            ycen[1] = y[1]
            draw_theloadmap(data[i])
            askoption(i)
    root.update_idletasks()
    root.update()
    time.sleep(0.04)


def rightkey(event):
    global canva, player,root,time,xbox,ybox,data,draw_theloadmap,xcen,ycen,playerright,selectplayerright
    loop = len(xbox)
    print("right")
    characterpos = canva.coords(player)
    canva.delete(player)
    player = canva.create_image(characterpos[0], characterpos[1], image=playerright[selectplayerright], anchor='sw')
    selectplayerright += 1
    if selectplayerright > 2:
        selectplayerright = 0
    canva.move(player, 5, 0)
    pos = canva.coords(player)
    print(pos)
    if pos[0] >= 1310:
        canva.move(player, -5, 0)
    for i in range(loop):
        x = xbox[i].split(",")
        y = ybox[i].split(",")
        if float(x[0])-60 <= pos[0] <= float(x[1]) and (float(y[0]) <= pos[1] <= float(y[1])+70):
            canva.move(player, -5, 0)
            xcen[0] = x[0]
            ycen[0] = y[0]
            xcen[1] = x[1]
            ycen[1] = y[1]
            draw_theloadmap(data[i])
            askoption(i)
    root.update_idletasks()
    root.update()
    time.sleep(0.04)
def upkey(event):
    global canva, player,root,time,xbox,ybox,data,draw_theloadmap,questions,xcen,ycen,playerup,selectplayerup,askoption
    loop = len(xbox)
    characterpos = canva.coords(player)
    canva.delete(player)
    player = canva.create_image(characterpos[0], characterpos[1], image=playerup[selectplayerup], anchor='sw')
    selectplayerup += 1
    if selectplayerup > 2:
        selectplayerup = 0
    canva.move(player, 0, -5)
    print("up")
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
            xcen[0] = x[0]
            ycen[0] = y[0]
            xcen[1] = x[1]
            ycen[1] = y[1]
            askoption(i)

    root.update_idletasks()
    root.update()
    time.sleep(0.04)
def downkey(event):
    global canva, player,root,time,xbox,ybox,data,draw_theloadmap,xcen,ycen,playerdown,selectplayerdown
    loop = len(xbox)
    characterpos = canva.coords(player)
    canva.delete(player)
    player = canva.create_image(characterpos[0], characterpos[1], image=playerdown[selectplayerdown], anchor='sw')
    selectplayerdown += 1
    if selectplayerdown > 2:
        selectplayerdown = 0
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
            xcen[0] = x[0]
            ycen[0] = y[0]
            xcen[1] = x[1]
            ycen[1] = y[1]
            draw_theloadmap(data[i])
            askoption(i)
    root.update_idletasks()
    root.update()
    time.sleep(0.04)
    print("down")
def Selected():
    global root,clicked,playersel
    if clicked.get() == "Player 1":
        playersel("mage")
    if clicked.get() == "Player 2":
        playersel("b")
    if clicked.get() == "Player 3":
        playersel("tile")




#map load
playersel("mage")
loadMap()
for i in Buildinglist:
     data.append(Building_cut(Buildinglist[Buildinglist.index(i)]))
     min_max(data[Buildinglist.index(i)])

bpicture=[None]*len(data)*4

selectplayer = tk.Button(root, text="Select Player", command=Selected, width=10).place(x=360, y=660)

map3d = tk.Button(root, text="Map in 3D", command=Map3D, width=10).place_forget()


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