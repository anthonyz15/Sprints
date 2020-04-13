
class building:
    wallstr = []
    building_name=""
    buildingpicture=""
    questions=[]


    def buildingname(self,name):
        temp ="Building:%s" %(name)
        self.building_name+=temp

    def wall(self,x1,y1,x2,y2,height,texture):
        temp= 'Wall:x1=%d, y1=%d, x2=%d, y2=%d, Height=%d, Texture: %s \n'% (x1,y1,x2,y2,height,texture)
        self.wallstr.append(temp)
        print(*self.wallstr)
    def editwall(self,wallnum,x1,y1,x2,y2,height,texture):
        print(wallnum)
        self.wallstr[wallnum-2]='Wall:x1=%d, y1=%d, x2=%d, y2=%d, Height=%d, Texture: %s \n'% (x1,y1,x2,y2,height,texture)
        return self.wallstr

    def question(self,question):
        q=question.split("\n")
        temp= 'Question: %s\n Right: %s \n Wrong: %s \n Wrong: %s \n Wrong: %s \n'% (q[0],q[1],q[2],q[3],q[4])
        self.questions.append(temp)
        print(*self.questions)

    def SaveBuilding(self):
        temp=""
        temp=self.building_name+ "\n" +self.buildingpicture+ "\n" + temp.join(self.wallstr)
        return temp

    def QuestionBuilding(self):
        temp=""
        temp=self.building_name+ "\n" + temp.join(self.questions)
        return temp

    def buildingpic(self,file):
        temp = "BuildingImage:%s" % (file)
        self.buildingpicture+=temp

    def DeleteBuilding(self):
        self.building_name=""
        self.wallstr=[]
        self.buildingpicture = ""
        self.questions=[]

'''
Nombre: buildingname
Objectivo: Añadir a un edificio su nombre
Precondiciones: Presionar el botón de crear edificio en el interfaz de usuario
Postcondiciones: Se le atribuye el nombre escrito al edificio.
Argumentos: name => el nombre a proveer
Autor: Jean Merced
Fecha: 4 de marzo de 2020
###
Nombre: wall
Objetivo:  Añadir una pared a un edificio en específico.
Precondiciones: Dibujar la pared en el interfaz de usuario
Postcondiciones: Se le añade la pared al edificio
Argumentos: x1,x2 => coordenadas en el plano X
            y1,y2 => coordenadas en el plano Y
            height => altura de la pared
            texture => imágen asociada a la textura de las paredes
Autor: Jean Merced
Fecha: 4 de marzo de 2020
###
Nombre: editwall
Objectivo: Editar una pared de un edificio
Precondiciones: Se presiona el botón de someter cambios en el interfaz de usuario
Postcondiciones: Se hacen los cambios necesarios a la pared
Argumentos: x1,x2 => coordenadas en el plano X
            y1,y2 => coordenadas en el plano Y
            height => altura de la pared
            texture => imágen asociada a la textura de las paredes
Autor: Enrique Marrero
Fecha: 28 de marzo de 2020
###
Nombre: Question
Objetivo: Añadir una pregunta a la lista de preguntas del edificio
Precondiciones: Presionar el botón de añadir una pregunta
Postcondiciones: Se añade una pregunta a la lista de preguntas del edificio
Argumentos: question => una lista que contiene la pregunta, contestación correcta
                        y tres contestaciones incorrectas
Autor: Enrique Marrero
Fecha: 9 de abril de 2020
###
Nombre: SaveBuilding
Objectivo: Guardar los atributos del edificio a un archivo
Precondiciones: Presionar el botón de guardar edificio en el interfaz de usuario
Postcondiciones: Se escriben los atributos adjuntos a un edificio
Autor: Anthony Cuevas
Fecha: 4 de marzo de 2020
###
Nombre: QuestionBuilding
Objetivo: Proveer el nombre del edificio con la lista de preguntas
Precondiciones: Se desea archivar información sobre el edificio
Postcondiciones: Se coloca el nombre del edificio, luego pregunta y finalmente 
                 resupuestas. Cada cosa en una línea aparte
Autor: Irving Lazu
Fecha: 10 de abril de 2020
###
Nombre: buildingpic
Objectivo: Añadir una imagen al edificio
Precondiciones: Presionar el botón de añadir imagen en el interfaz de usuario
Postcondiciones: Se le atribuye la imagen al edificio.
Argumentos: file => el archivo de la imagen
Autor: Anthony Cuevas
Fecha: 4 de marzo de 2020
###
Nombre: DeleteBuilding
Objectivo: Elimina un edificio
Precondiciones: Presionar el botón de eliminar edificio en el interfaz de usuario
Postcondiciones: Se elimina el edificio, borrando los atributos que éste contiene
Autor: Irving Lazu
Fecha: 4 de marzo de 2020
'''
