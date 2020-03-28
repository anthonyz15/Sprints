import tkinter as tk
from tkinter import filedialog
from tkinter import *
from Building import building
from PIL import ImageTk,Image


backgroundtxt=" "
Buildingtxt=" "
texture=" "

bu=building()


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

####################################second window##############################################

top = Toplevel()#lib kinter
top.title("Map functions")
top.geometry("590x270")  # Width x Height


# XandY entry
Name = tk.Label(top, text="Name").place(x=0, y=40)
x1 = tk.Label(top, text="X1").place(x=0, y=70)
y1 = tk.Label(top, text="Y1").place(x=90, y=70)
x2 = tk.Label(top, text="X2").place(x=180, y=70)
y2 = tk.Label(top, text="Y2").place(x=270, y=70)
z = tk.Label(top, text="Height").place(x=360, y=70)
eb = tk.Entry(top, width=20)
ex1 = tk.Entry(top, width=10)
ey1 = tk.Entry(top, width=10)
ex2 = tk.Entry(top, width=10)
ey2 = tk.Entry(top, width=10)
ez = tk.Entry(top, width=10)


eb.place(x=40, y=40)
ex1.place(x=20, y=70)
ey1.place(x=110, y=70)
ex2.place(x=200, y=70)
ey2.place(x=290, y=70)
ez.place(x=400, y=70)

text_widget1 = tk.Text(top, width=60, height=8)
text_widget1.place(x=15, y=100)

def AddBuilding():
    global Buildingtxt,text_widget1,eb,bu,building
    Buildingtxt+=bu.SaveBuilding()
    bu.DeleteBuilding()
    #temp="Building:  "
    #Buildingclass = "%s%s\n" % (temp,str(eb.get()))
    bu.buildingname(str(eb.get()))
    text_widget1.delete("1.0", END)

def RemoveBuilding():
    global bu
    bu.DeleteBuilding()


def Submit(): #submit
    global text_widget1,ex1,ex2,ey1,ey2,ez,Buildingtxt,Texture,bu
    text_widget1.insert(INSERT, 'x1 = % d, y1 = % d , x2 = % d, y2 = % d, Height = % d\n' % (int(ex1.get()), int(ey1.get()), int(ex2.get()),int(ey2.get()), int(ez.get())))
    line = canva.create_line(int(ex1.get()), int(ey1.get()), int(ex2.get()),int(ey2.get()), width=3)
    tex=Texture()
    bu.wall(int(ex1.get()), int(ey1.get()), int(ex2.get()),int(ey2.get()), int(ez.get()),tex)

def Texture():
    global texture
    file_path = filedialog.askopenfilename()
    return file_path



def saveMap():
    global backgroundtxt,Buildingtxt
    Buildingtxt+=bu.SaveBuilding()
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    textToSave=backgroundtxt+Buildingtxt
    f.write(textToSave)
    f.close()

def bg_load(bg):
    global canva
    canva.image = ImageTk.PhotoImage(file=bg)
    canva.create_image(0, 0, image=canva.image, anchor=NW)
    canva.pack()


def loadMap():
    global canva,Buildingtxt,backgroundtxt,bg_load,draw_theloadmap
    file_path = filedialog.askopenfilename()
    wall_draw=[]
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
    bg_load(bg)
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
    print(text_widget1.get(1,2))

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





#buttons
building = tk.Button(top, text="Add Building", command=AddBuilding, width=14).place(x=180, y=35)
submit = tk.Button(top, text ="Submit", command=Submit, width=10).place(x=470, y=70)
removebuilding = tk.Button(top, text="Remove Building", command=remove_building, width=14).place(x=290, y=35)
save = tk.Button(top, text="Save", command=saveMap, width=10).place(x=470, y=15)
edit = tk.Button(top, text="Edit", command=edit_coor, width=10).place(x=470, y=100)
load = tk.Button(root, text="load", command=loadMap, width=10).place(x=700, y=660)


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
    global x1,y1,rep,canva,texture,Buildingtxt,bu
    print('draw x = % d, y = % d' % (event.x, event.y))
    if rep>0:
        line = canva.create_line(x1, y1, event.x, event.y, width=3)
        text_widget1.insert(INSERT, 'x1 = % d, y1 = % d , x2 = % d, y2 = % d, Height = % d\n' % (x1, y1, event.x, event.y, 5))
        bu.wall(x1,y1,event.x,event.y,5,"")
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