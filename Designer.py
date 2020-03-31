import tkinter as tk
from tkinter import filedialog
from tkinter import *
from Building import building
from PIL import ImageTk,Image


backgroundtxt=" "
Buildingtxt=" "
texture=" "
tree=""
questionfile="myTriviaFile.txt"


bu=building()

global img,t1,t2,t3,wallnum

wallnum=1



x1=0
x2=0
y1=0
y2=0
rep=0
z=5

root = tk.Tk()  # lib kinter

root.title("Designer")
root.geometry("1024x700")  # Width x Height

canva = tk.Canvas(root, width=1024, height=650)
canva.config(bg="white")
canva.pack()
label=Label(root,text="Coordinates").place(x=350,y=655)
text_widget = Text(root,width=20,height=1)
text_widget.pack()

t1 = Image.open("tree1.png")
t1 = t1.resize((100, 100), Image.ANTIALIAS)
t1 = ImageTk.PhotoImage(t1)

t2 = Image.open("tree2.png")
t2 = t2.resize((100, 100), Image.ANTIALIAS)
t2 = ImageTk.PhotoImage(t2)

t3 = Image.open("tree3.png")
t3 = t3.resize((100, 100), Image.ANTIALIAS)
t3 = ImageTk.PhotoImage(t3)

####################################second window##############################################

top = Toplevel()#lib kinter
top.title("Map functions")
top.geometry("700x400")  # Width x Height


# XandY entry
Name = tk.Label(top, text="Name").place(x=0, y=40)
x1 = tk.Label(top, text="X1").place(x=0, y=70)
y1 = tk.Label(top, text="Y1").place(x=90, y=70)
x2 = tk.Label(top, text="X2").place(x=180, y=70)
y2 = tk.Label(top, text="Y2").place(x=270, y=70)
z = tk.Label(top, text="Height").place(x=360, y=70)

tree1 = tk.Label(top, text="X").place(x=0, y=250)
tree2 = tk.Label(top, text="Y").place(x=90, y=250)



eb = tk.Entry(top, width=20)
ex1 = tk.Entry(top, width=10)
ey1 = tk.Entry(top, width=10)
ex2 = tk.Entry(top, width=10)
ey2 = tk.Entry(top, width=10)
ez = tk.Entry(top, width=10)
tree1 = tk.Entry(top, width=10)
tree2 = tk.Entry(top, width=10)





eb.place(x=40, y=40)
ex1.place(x=20, y=70)
ey1.place(x=110, y=70)
ex2.place(x=200, y=70)
ey2.place(x=290, y=70)
ez.place(x=400, y=70)
tree1.place(x=20, y=250)
tree2.place(x=110, y=250)



text_widget1 = tk.Text(top, width=80, height=8)
text_widget1.place(x=15, y=100)


clicked= StringVar()
clicked.set("Tree 1")
drop= OptionMenu(top,clicked,"Tree 1","Tree 2","Tree 3")
drop.place(x=180, y=245)

########################################################################################################

def AddBuilding():
    global Buildingtxt,text_widget1,eb,bu,building
    Buildingtxt+=bu.SaveBuilding()
    bu.DeleteBuilding()
    #temp="Building:  "
    #Buildingclass = "%s%s\n" % (temp,str(eb.get()))
    bu.buildingname(str(eb.get()))
    text_widget1.delete("1.0", END)
def buildingpic():
    file_path = filedialog.askopenfilename()
    bu.buildingpic(file_path)
    return file_path

def RemoveBuilding():
    global bu
    bu.DeleteBuilding()


def Submit(): #submit
    global text_widget1,ex1,ex2,ey1,ey2,ez,Buildingtxt,Texture,bu,wallnum
    text_widget1.insert(INSERT, 'Wall%d:x1 = % d, y1 = % d , x2 = % d, y2 = % d, Height = % d\n' % (wallnum,int(ex1.get()), int(ey1.get()), int(ex2.get()),int(ey2.get()), int(ez.get())))
    line = canva.create_line(int(ex1.get()), int(ey1.get()), int(ex2.get()),int(ey2.get()), width=3)
    tex=Texture()
    bu.wall(int(ex1.get()), int(ey1.get()), int(ex2.get()),int(ey2.get()), int(ez.get()),tex)
    wallnum+=1

def Texture():
    global texture
    file_path = filedialog.askopenfilename()
    return file_path



def saveMap():
    global backgroundtxt,Buildingtxt,tree,questionfile
    Buildingtxt+=bu.SaveBuilding()
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    textToSave=backgroundtxt+Buildingtxt+tree+questionfile
    f.write(textToSave)
    f.close()


def bg_load(bg):
    global canva
    print(bg)
    canva.image = ImageTk.PhotoImage(file=bg)
    canva.create_image(0, 0, image=canva.image, anchor=NW)
    canva.pack()


def loadMap():
    global canva,Buildingtxt,backgroundtxt,bg_load,draw_theloadmap,loadtree
    file_path = filedialog.askopenfilename()
    wall_draw=[]
    trees=[]
    locat=[]
    with open(file_path, "r") as ifile:
        for line in ifile:
            if line.startswith("Background:"):
                print(line[11:62])
                bg=line[11:-1]
                backgroundtxt="Background:" + bg + "\n"
            if line.startswith("Building:"):
                print(line[9:])
                building_name=line[9:]
                Buildingtxt+="Building:" +building_name
            if line.startswith("Wall:"):
                print(line[5:])
                wall=line[5:]
                wall_draw.append(wall)
                Buildingtxt+="Wall:" +wall
            if line.startswith("TreeType:"):
                print(line[9:])
                treetype=line[9:15]
                location=line[26:]
                location=location.replace(")","")
                print(treetype,location)
                trees.append(treetype)
                locat.append(location)
    bg_load(bg)
    for i in range(len(trees)):
        loadtree(trees[i],locat[i])
    draw_theloadmap(wall_draw)


def draw_theloadmap(drawwall):
    global canva
    for i in drawwall:
        print(i)
        x=i.split(",")
        x1=x[0][3:]
        y1 = x[1][4:]
        x2 = x[2][4:]
        y2 = x[3][4:]
        print(x1,y1,x2,y2)
        canva.create_line(x1,y1,x2,y2, width=3)
def edit_coor():
    global wallnum,bu
    dele=float(wallnum)
    text_widget1.delete(dele-1.0, dele)
    text_widget1.insert(INSERT, 'Wall%d:x1 = % d, y1 = % d , x2 = % d, y2 = % d, Height = % d\n' % (wallnum-1, int(ex1.get()), int(ey1.get()), int(ex2.get()), int(ey2.get()), int(ez.get())))
    tex = Texture()
    bu.editwall(wallnum, int(ex1.get()), int(ey1.get()), int(ex2.get()), int(ey2.get()), int(ez.get()),tex)
    line = canva.create_line(int(ex1.get()), int(ey1.get()), int(ex2.get()), int(ey2.get()), width=3)

def remove_building():
    global Buildingtxt,eb,backgroundtxt
    wall_draw=[]
    buildlist=Buildingtxt.split("Building:")
    Buildingtxt = ""
    buildlist.pop(0)
    for i in buildlist:
        if i.startswith(str(eb.get())):
            buildlist.pop(buildlist.index(i))
    Buildingtxt="Building:"+Buildingtxt.join(buildlist)
    if len(buildlist)==0:
        Buildingtxt=""
    draw=Buildingtxt.split("\n")
    for line in draw:
        if line.startswith("Wall:"):
            print(line[5:])
            wall = line[5:]
            wall_draw.append(wall)
    bg_load(backgroundtxt[11:-1])
    draw_theloadmap(wall_draw)

def Addtree():
    global tree,tree1,tree2,canva,root,clicked
    x=int(tree1.get())
    y=int(tree2.get())
    tree+= "TreeType:" + str(clicked.get())+", location(%d,%d)"%(x,y) + "\n"
    if clicked.get() == "Tree 1":
        canva.create_image(x, y, image=t1,anchor='nw')
        canva.pack()
    if clicked.get() == "Tree 2":
        canva.create_image(x, y, image=t2,anchor='nw')
        canva.pack()
    if clicked.get() == "Tree 3":
        canva.create_image(x, y, image=t3,anchor='nw')
        canva.pack()
def loadtree(treetype,location):
    global tree,tree1,tree2,canva,root
    locat=location.split(",")
    x=int(locat[0])
    y=int(locat[1])
    tree+= "TreeType:" + treetype+", location(%d,%d)"%(x,y) + "\n"
    if treetype == "Tree 1":
        canva.create_image(x, y, image=t1,anchor='nw')
        canva.pack()
    if treetype == "Tree 2":
        canva.create_image(x, y, image=t2,anchor='nw')
        canva.pack()
    if treetype == "Tree 3":
        canva.create_image(x, y, image=t3,anchor='nw')
        canva.pack()


#buttons



building = tk.Button(top, text="Add Building", command=AddBuilding, width=14).place(x=180, y=35)
submit = tk.Button(top, text ="Submit", command=Submit, width=10).place(x=470, y=70)
removebuilding = tk.Button(top, text="Remove Building", command=remove_building, width=14).place(x=290, y=35)
buildingpic = tk.Button(top, text="BuildingPic", command=buildingpic, width=14).place(x=400, y=35)
save = tk.Button(top, text="Save Map", command=saveMap, width=10).place(x=600, y=320)
edit = tk.Button(top, text="Edit last wall", command=edit_coor, width=10).place(x=560, y=70)
load = tk.Button(root, text="load", command=loadMap, width=10).place(x=700, y=660)
addtree = tk.Button(top, text="Add tree", command=Addtree, width=10).place(x=260, y=245)


############################################################################################


def choose_bg():
    global canva,backgroundtxt
    file_path = filedialog.askopenfilename()
    backgroundtxt="Background:"+ file_path + "\n"
    canva.image=ImageTk.PhotoImage(file=file_path)
    canva.create_image(0,0,image=canva.image,anchor=NW)
    canva.pack()



def pressed1(event):
    global text_widget
    text_widget.delete('1.0',END)
    text_widget.insert(INSERT, 'x = % d, y = % d ' % (event.x, event.y))




## function to be called when button-1 is double clocked
def double_click(event):
    global x1,y1,rep,canva,texture,Buildingtxt,bu,wallnum
    print('draw x = % d, y = % d' % (event.x, event.y))
    if rep>0:
        line = canva.create_line(x1, y1, event.x, event.y, width=3)
        text_widget1.insert(INSERT,'Wall%d:x1 = % d, y1 = % d , x2 = % d, y2 = % d, Height = % d\n' % (wallnum,x1, y1, event.x, event.y, 5))
        tex = Texture()
        bu.wall(x1,y1,event.x,event.y,5,tex)
        wallnum+=1
        rep=0
    else:
        rep=rep+1
        x1=event.x
        y1=event.y




B = Button(root, text ="Choose Background", command=choose_bg).place(x=160,y=660)

# these lines are binding mouse
# buttons with the Frame widget
canva.bind('<Button-1>', pressed1)
canva.bind('<Double 1>', double_click)


root.mainloop()


'''
Nombre: saveMap
Objectivo: Guardar el mapa con un nombre y en formato .txt de forma que se pueda hacer 
referencia posteriormente al mismo y que pueda leer su contenido con cualquier editor 
de texto.
Precondiciones: El botón de 'save' fue presionado.
Postcondiciones: Se crea un archivo en formato .txt que contiene la información que
describe el mapa.
Argumentos: N/A
Autor: Anthony Cuevas
Fecha: 7 de marzo de 2020
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
Nombre: loadMap
Objectivo: Seleccionar un archivo que contenga un mapa y cargarlo para poder jugar.
Precondiciones: Se presiona el botón de 'load'.
Postcondiciones: Se cargará un mapa para jugar.
Argumentos: N/A
Autor: Anthony Cuevas
Fecha: 7 de marzo de 2020
###
Nombre: draw_theloadmap
Objectivo: Dibujar las líneas en la pantalla que representan las paredes del
edificio cuando se carga un mapa existente.
Precondiciones: Se cargará un mapa.
Postcondiciones: Se dibuja en pantalla las líneas que representa las paredes.
Argumentos: drawwall => arreglo de paredes, contiene las coordenadas de los
extremos de las paredes.
Autor: Anthony Cuevas
Fecha: 7 de marzo de 2020
###
Nombre: edit_coor
Objectivo: Editar las coordenadas de los extremos de la pared seleccionada.
Precondiciones: Se selecciona un extremo de una pared.
Postcondiciones: Las coordenadas del extremo de la pared se atualizan.
Argumentos: N/A
Autor: Irving Lazu
Fecha: 30 de marzo de 2020
###
Nombre: remove_building
Objectivo: Eliminar edificios que ya había creado, de forma que pueda hacer 
modificaciones en los mapas existentes.
Precondiciones: Se presiona botón de 'Remove Building'.
Postcondiciones: El edificio se eliminará del mapa.
Argumentos: N/A
Autor: Irving Lazu
Fecha: 4 de marzo de 2020
###
Nombre: Addtree
Objectivo: Colocar imágenes de árboles en el mapa seleccionando, uno de entre tres tipos de árboles.
Precondiciones: Se presiona botón 'Add Tree'.
Postcondiciones: Se cargará la imagen del árbol correspondiente en el punto seleccionado.
Argumentos: N/A
Autor: Enrique Marrero
Fecha: 30 de marzo de 2020
###
Nombre: choose_bg
Objectivo: Seleccionar una imagen de forma que pueda asignarla como fondo
para un mapa.
Precondiciones: Se presiona el botón 'Choose Background'.
Postcondiciones: Se cargará la imagen de fondo en el mapa.
Argumentos: N/A
Autor: Jean Merced
Fecha: 4 de marzo de 2020
###
Nombre: double_click
Objectivo: Dibujar las líneas en la pantalla, de forma que pueda establecer las 
coordenadas para los extremos de las paredes de los edificios.
Precondiciones: Hacer doble clic en la pantalla en los puntos que quiere definir como
los extremos de la pared.
Postcondiciones: Se dibuja en pantalla una línea que representa una pared.
Argumentos: event => el ratón fue presionado.
Autor: Enrique Marrero
Fecha: 4 de marzo de 2020
'''

