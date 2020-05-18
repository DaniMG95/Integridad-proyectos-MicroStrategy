#Carga de paquete pandas, permite trabajar con dataframes
import pandas as pd
#Carga de paquete os, encargado de llamadas al sistema
import os

###############################################   file_atributos       ###########################################################
###### parametros :
######             principal : Fichero que contiene los detalles principales de los atributos
######             detalles : Fichero que contiene todas las propiedades de los atributos
###### Funcionalidad : Obtener un dataframe con todas las propiedades filtradas de los atributos
######                 'Nombre',"Nuevo Nombre",'Ruta','Nueva Ruta','Representacion','Tabla de origen','Expresion','Descripción'
###### return : dataframe
###################################################################################################################################

def file_atributos(principal,detalles):
    nombre=[]
    ruta=[]
    representacion=[]
    expresion=[]
    descripcion=[]
    tabla=[]

    file = open(principal, "r")
    for line in file:
        if("Nombre =" in line):
            nombre.append(line.replace("Nombre = ","").rstrip("\n\r"))
        elif("Ruta =" in line):
            ruta.append(line.replace("Ruta = ","").rstrip("\n\r"))

    cnt=-1
    nombre_f=[]
    ruta_f=[]
    descripcion_f=[]

    file = open(detalles, "r")
    for line in file:
        if("Descripción =" in line):
            descripcion.append(line.replace("Descripción = ","").rstrip("\n\r"))

    file = open(detalles, "r")
    for line in file:
        if("Nombre =" in line):
            cnt=cnt+1
        elif("Representación de atributo =" in line):
            representacion.append(line.replace("\tRepresentación de atributo = ","").rstrip("\n\r"))
            nombre_f.append(nombre[cnt])
            ruta_f.append(ruta[cnt])
            descripcion_f.append(descripcion[cnt])



    nombre_final=[]
    ruta_final=[]
    descripcion_final=[]
    representacion_final=[]
    cnt=-1
    Nuevo_nombre=[]
    Nueva_ruta=[]

    file = open(detalles, "r")
    for line in file:
        if("Representación de atributo =" in line):
            cnt=cnt+1
        elif("Expresión =" in line):
            expresion_=line.replace("\t\tExpresión = ","").rstrip("\n\r")
        elif("Tabla de origen =" in line):
            tabla.append(line.replace("\t\t\tTabla de origen = ","").rstrip("\n\r"))
            expresion.append(expresion_)
            nombre_final.append(nombre_f[cnt])
            ruta_final.append(ruta_f[cnt])
            representacion_final.append(representacion[cnt])
            descripcion_final.append(descripcion_f[cnt])
            Nuevo_nombre.append("")
            Nueva_ruta.append("")





    data = {'Nombre':nombre_final,'Ruta':ruta_final,'Representacion':representacion_final,'Tabla':tabla,'Expresión':expresion}

    df = pd.DataFrame(data)
    return df



###############################################   file_filtros       ###########################################################
###### parametros :
######             principal : Fichero que contiene los detalles principales de los filtros
###### Funcionalidad : Obtener un dataframe con todas las propiedades filtradas de los filtros
######                 'Nombre',"Expresion","Descripcion"
###### return : dataframe
###################################################################################################################################



def file_filtros(principal):
    nombre=[]
    expresion=[]
    descripcion=[]


    file = open(principal, "r")
    for line in file:
        if("Nombre =" in line):
            nombre.append(line.replace("Nombre = ","").rstrip("\n\r"))
        elif("Expresión =" in line):
            expresion.append(line.replace("Expresión = ","").rstrip("\n\r"))
        elif("Descripción =" in line):
            descripcion.append(line.replace("Descripción = ","").rstrip("\n\r"))

    data = {'Nombre':nombre,'Expresión':expresion}

    df = pd.DataFrame(data)
    return df


###############################################       file_hechos       ###########################################################
###### parametros :
######             principal : Fichero que contiene los detalles principales de los hechos
######             detalles : Fichero que contiene todas las propiedades de los hechos
###### Funcionalidad : Obtener un dataframe con todas las propiedades filtradas de los hechos
######                 'Nombre',"Nuevo Nombre",'Ruta','Nueva Ruta','Expresión',"Tabla de origen","Descripción"
###### return : dataframe
###################################################################################################################################



def file_hechos(principal,detalles):
    nombre=[]
    ruta=[]
    expresion=[]
    tabla=[]
    descripcion=[]

    file = open(principal, "r")
    for line in file:
        if("Nombre =" in line):
            nombre.append(line.replace("Nombre = ","").rstrip("\n\r"))
        elif("Ruta =" in line):
            ruta.append(line.replace("Ruta = ","").rstrip("\n\r"))

    file = open(detalles, "r")
    for line in file:
        if("Expresión =" in line):
            expresion.append(line.replace("	Expresión = ","").rstrip("\n\r"))
        elif("Descripción =" in line):
            descripcion.append(line.replace("Descripción = ","").rstrip("\n\r"))

    cnt=-1
    nombre_final=[]
    ruta_final=[]
    expresion_final=[]
    descripcion_final=[]
    Nuevo_nombre=[]
    Nueva_ruta=[]

    file = open(detalles, "r")
    for line in file:
        if("Nombre =" in line):
            cnt=cnt+1
        if("Tabla de origen =" in line):
            tabla.append(line.replace("		Tabla de origen = ","").rstrip("\n\r"))
            nombre_final.append(nombre[cnt])
            ruta_final.append(ruta[cnt])
            expresion_final.append(expresion[cnt])
            descripcion_final.append(descripcion[cnt])
            Nuevo_nombre.append("")
            Nueva_ruta.append("")

    data = {'Nombre':nombre_final,'Ruta':ruta_final,'Expresión':expresion_final,"Tabla":tabla}

    df = pd.DataFrame(data)

    return df


###############################################       file_metricas       ###########################################################
###### parametros :
######             principal : Fichero que contiene los detalles principales de las metricas
######             detalles : Fichero que contiene todas las propiedades de las metricas
###### Funcionalidad : Obtener un dataframe con todas las propiedades filtradas de las metricas
######                 'Nombre',"Nuevo Nombre",'Ruta','Nueva Ruta','Fórmula','Condición',"Transformación","Expresión","Descripción"
###### return : dataframe
#####################################################################################################################################

def file_metricas(principal,detalles):


    nombre=[]
    ruta=[]
    formula=[]
    condicion=[]
    transformacion=[]
    expresion=[]
    descripcion=[]
    Nuevo_nombre=[]
    Nueva_ruta=[]

    file = open(principal, "r")
    for line in file:
        if("Nombre =" in line):
            nombre.append(line.replace("Nombre = ","").rstrip("\n\r"))
            Nuevo_nombre.append("")
            Nueva_ruta.append("")
        elif("Ruta =" in line):
            ruta.append(line.replace("Ruta = ","").rstrip("\n\r"))

    file = open(detalles, "r")
    for line in file:
        if("Fórmula =" in line):
            formula.append(line.replace("Fórmula = ","").rstrip("\n\r"))
        elif("Condición = " in line):
            condicion.append(line.replace("Condición = ","").rstrip("\n\r"))
        elif("Transformación = " in line):
            transformacion.append(line.replace("Transformación = ","").rstrip("\n\r"))
        elif("Expresión = " in line):
            expresion.append(line.replace("Expresión = ","").rstrip("\n\r"))
        elif("Descripción = " in line):
            descripcion.append(line.replace("Descripción = ","").rstrip("\n\r"))




    data = {'Nombre':nombre,'Ruta':ruta,'Fórmula':formula, 'Condición':condicion,"Transformación":transformacion,"Expresión":expresion}

    df = pd.DataFrame(data)



    return df


###############################################       list_projects       ###########################################################
###### parametros :
######             principal: Fichero que contiene todos los proyectos
###### Funcionalidad : Leer el fichero y crear una lista con todos los proyectos que se pueden crear el Glosario
###### return : Lista
#####################################################################################################################################

def list_projects(principal):
    list=[]
    file = open(principal, "r")
    for line in file:
        if("Nombre =" in line):
            list.append(line.replace("Nombre = ","").rstrip("\n\r"))
    return list


###############################################       clear_files       ###########################################################
###### parametros : None
###### Funcionalidad : Eliminar todos los ficheros que almancenan la salida y los scripts del command manager
###### return : None
#####################################################################################################################################

def clear_files():
    lista=['logs/fail.out','logs/success.out'"scripts/scp/atributos.scp","scripts/scp/detalles_atributos.scp","scripts/scp/detalles_filtros.scp"
           ,"scripts/scp/detalles_hechos.scp","scripts/scp/detalles_metricas.scp","scripts/scp/folders.scp","scripts/scp/hechos.scp"
           ,"scripts/scp/metricas.scp","scripts/scp/metricas.scp"]
    for r, d, f in os.walk('./salida'):
        for file in f:
            lista.append('./salida/proyecto1/'+file)
            lista.append('./salida/proyecto2/'+file)
    for r, d, f in os.walk('./csv'):
        for file in f:
            lista.append('./csv/'+file)
    for file in lista:
        if(os.path.isfile(file)):
            os.remove(file)

###############################################       clear_files       ###########################################################
###### parametros : None
###### Funcionalidad : Eliminar todos los ficheros que almancenan la salida y los scripts del command manager
###### return : None
#####################################################################################################################################

def clear_files_scripts():
    lista=["scripts/scp/atributos.scp","scripts/scp/detalles_atributos.scp","scripts/scp/detalles_filtros.scp"
           ,"scripts/scp/detalles_hechos.scp","scripts/scp/detalles_metricas.scp","scripts/scp/folders.scp","scripts/scp/hechos.scp"
           ,"scripts/scp/metricas.scp","scripts/scp/metricas.scp"]
    for file in lista:
        if(os.path.isfile(file)):
            os.remove(file)




###############################################       create_scp       ###########################################################
###### parametros :
######             projects: El nombre del proyecto al que se quiere crear el Glosario
###### Funcionalidad : Crear todos los scripts de Command Manager que son necesarios para crear el Glosario
###### return : None
#####################################################################################################################################

def create_scp(project):
    file1 = open("scripts/scp/atributos.scp","w")
    file1.write("LIST ALL ATTRIBUTES FOR PROJECT '"+project+"';\n")
    file1.close()

    file1 = open("scripts/scp/detalles_atributos.scp","w")
    file1.write("EXECUTE PROCEDURE List_All_Properties_Attributes("+'"'+project+'"'+");\n")
    file1.close()

    file1 = open("scripts/scp/detalles_filtros.scp","w")
    file1.write("EXECUTE PROCEDURE List_all_properties_filters("+'"'+project+'"'+");\n")
    file1.close()

    file1 = open("scripts/scp/detalles_hechos.scp","w")
    file1.write("EXECUTE PROCEDURE List_All_Properties_Facts("+'"'+project+'"'+");\n")
    file1.close()

    file1 = open("scripts/scp/detalles_metricas.scp","w")
    file1.write("EXECUTE PROCEDURE List_All_Metrics_Properties("+'"'+project+'"'+");\n")
    file1.close()

    file1 = open("scripts/scp/folders.scp","w")
    file1.write("EXECUTE PROCEDURE List_all_folders('\\',"+'"'+project+'"'+");\n")
    file1.close()

    file1 = open("scripts/scp/hechos.scp","w")
    file1.write("LIST ALL FACTS FOR PROJECT '"+project+"';\n")
    file1.close()

    file1 = open("scripts/scp/metricas.scp","w")
    file1.write("LIST ALL METRICS FOR PROJECT '"+project+"';\n")
    file1.close()

###############################################       get_properties_command       ###########################################################
###### parametros :
######             origen: El nombre del origen de conexion
######             usuario: El nombre del usuario con el que quiere conectar
######             password: La contraseña del usuario
###### Funcionalidad : Llamar a los scripts del Command
###### return : None
##############################################################################################################################################

def get_properties_command(origen,usuario,password,salida):

    os.system("cmdmgr -n "+origen+" -u "+usuario+password+" -f scripts/scp/atributos.scp -or "+salida+"/atributos.out -of logs/fail.out -os logs/success.out")
    os.system("cmdmgr -n "+origen+" -u "+usuario+password+" -f scripts/scp/detalles_atributos.scp -or "+salida+"/detalles_atributos.out -of logs/fail.out -os logs/success.out")
    print("Obteniendo caracteristicas de las metricas")
    os.system("cmdmgr -n "+origen+" -u "+usuario+password+" -f scripts/scp/metricas.scp -or "+salida+"/metricas.out -of logs/fail.out -os logs/success.out")
    os.system("cmdmgr -n "+origen+" -u "+usuario+password+" -f scripts/scp/detalles_metricas.scp -or "+salida+"/detalles_metricas.out -of logs/fail.out -os logs/success.out")
    print("Obteniendo caracteristicas de los hechos")
    os.system("cmdmgr -n "+origen+" -u "+usuario+password+" -f scripts/scp/hechos.scp -or "+salida+"/hechos.out -of logs/fail.out -os logs/success.out")
    os.system("cmdmgr -n "+origen+" -u "+usuario+password+" -f scripts/scp/detalles_hechos.scp -or "+salida+"/detalles_hechos.out -of logs/fail.out -os logs/success.out")
    print("Obteniendo caracteristicas de los filtros")
    os.system("cmdmgr -n "+origen+" -u "+usuario+password+" -f scripts/scp/detalles_filtros.scp -or "+salida+"/detalles_filtros.out -of logs/fail.out -os logs/success.out")


###############################################       get_properties      ###########################################################
###### parametros :
######             properties : Fichero properties
###### Funcionalidad : Se encarga de leer el fichero properties y obtener el usuario y el origen
###### return : origen,usuario
#####################################################################################################################################

def get_properties(properties):
    file = open(properties, "r")
    for line in file:
        if("Origen1" in line):
            origen1=line.replace("Origen1 :","").rstrip("\n\r")
            origen1=(origen1.lstrip()).rstrip()
        elif("Origen2" in line):
            origen2=line.replace("Origen2 :","").rstrip("\n\r")
            origen2=(origen2.lstrip()).rstrip()
        elif("Usuario1" in line):
            usuario1=line.replace("Usuario1 :","").rstrip("\n\r")
            usuario1=(usuario1.lstrip()).rstrip()
        elif("Usuario2" in line):
            usuario2=line.replace("Usuario2 :","").rstrip("\n\r")
            usuario2=(usuario2.lstrip()).rstrip()
    origenes=[origen1,origen2]
    usuarios=[usuario1,usuario2]
    return origenes,usuarios

###############################################       get_inicio_sesion      ########################################################
###### parametros :
######             origen: El nombre del origen de conexion
######             usuario: El nombre del usuario con el que quiere conectar
######             password: La contraseña del usuario
###### Funcionalidad : Se encarga de ver si los parametros son los correctos para iniciar sesion y obtener la lista de proyectos
###### return : None
#####################################################################################################################################

def get_inicio_sesion(origen,usuario,password,salida):

    os.system("cmdmgr -n "+origen+" -u "+usuario+password+" -f scripts/scp/list_projects.scp -or "+salida+"/projects.out -of logs/fail.out -os logs/success.out")
    file = open("logs/fail.out", "r")
    error=False
    for f in file:
        if("CEST" in f):
            print(f[f.index("CEST")+4:])
            error=True
    if(error):
        sys.exit()
    file.close()


###############################################       mask_coporativo      ###########################################################
###### parametros :
######             df : dataframe que se va a filtrar
######             string : directorio que se quiere mantener en el dataframe
###### Funcionalidad : Se encarga de filtrar el dataframe obteniendo las filas que esten en el directorio string
###### return : list booleana de las filas que cumplen los requisitos
#####################################################################################################################################

def mask_coporativo(df,string):
    aux=df['Ruta'].tolist()
    mask=[]

    for i in aux:
        mask.append(string in i)
    return mask

###############################################       highlight_cols_grey      ###########################################################
###### parametros :
######             s : dataframe que se va pintar
###### Funcionalidad : Se encarga de pintar las celdas en color gris
###### return : style de color gris
#####################################################################################################################################

def highlight_cols_grey(s):
    color = '#C2C2BF'
    return 'background-color: %s' % color

###############################################       highlight_cols_yelllow      ###########################################################
###### parametros :
######             s : dataframe que se va pintar
###### Funcionalidad : Se encarga de pintar las celdas en color amarillo
###### return : style de color amarillo
#####################################################################################################################################

def highlight_cols_yelllow(val):
    color = '#EEEE11' if val == 'KO' else 'transparent'
    return 'background-color: %s' % color

###############################################       highlight_cols_orange      ###########################################################
###### parametros :
######             s : dataframe que se va pintar
###### Funcionalidad : Se encarga de pintar las celdas en color naranja
###### return : style de color naranja
#####################################################################################################################################

def highlight_cols_orange(s):
    color = '#EDAC00'
    return 'background-color: %s' % color

###############################################       integracion      ###########################################################
###### parametros :
######             df1 : dataframe
######             df2 : dataframe
######             nombre_proyecto1 : string
######             nombre_proyecto2 : sring
######             tipo : string
###### Funcionalidad : Se encarga de buscar la integridad entre dos proyectos y crear un dataframe resultante de esta integridad
###### return : dataframe
#####################################################################################################################################

def integracion(df1,df2,nombre_proyecto1,nombre_proyecto2,tipo):

    final=df1.copy()



    if(tipo=="Filtro"):
        columnas_final=["Nombre"]
        for i in range(1,len(df1.columns)):
            columnas_final.append(df1.columns[i]+"_"+nombre_proyecto1)
        final.columns=columnas_final
        columnas_proyecto1=[name+"_"+nombre_proyecto1 for name in df1.columns[1:]]
        columnas_proyecto2=[name+"_"+nombre_proyecto2 for name in df2.columns[1:]]
        columnas_revisar=["Nombre","Expresión"]
        columnas_revisar_final=["Nombre",final.columns[1]]
        indice_aux=2
    else:
        columnas_final=["Nombre"]
        columnas_final.append("Ruta")
        for i in range(2,len(df1.columns)):
            columnas_final.append(df1.columns[i]+"_"+nombre_proyecto1)
        final.columns=columnas_final
        columnas_proyecto1=[name+"_"+nombre_proyecto1 for name in df1.columns[2:]]
        columnas_proyecto2=[name+"_"+nombre_proyecto2 for name in df2.columns[2:]]
        columnas_revisar=[name for name in df2.columns if name!="Ruta"]
        columnas_revisar_final=["Nombre"]
        indice_aux=3
        for i in range(2,len(df2.columns)):
            columnas_revisar_final.append(final.columns[i])


    for i in range(len(columnas_proyecto2)):
        final[columnas_proyecto2[i]]=""

    final["Resultado"]=""


    for i in range(final.shape[0]):
        nombre=df2.copy()
        aux=pd.DataFrame([[""]*len(df2.columns)], columns=df2.columns)
        for j in range(len(columnas_revisar)):
            nombre=nombre[nombre[columnas_revisar[j]]==final.loc[i][columnas_revisar_final[j]]]
            if(nombre.shape[0]!=0):
                aux=nombre.copy()
            else:
                nombre=aux
        k=indice_aux
        aux=aux.reset_index()
        for column in columnas_proyecto2:
            final.loc[i][column]=aux.loc[0][k]
            k=k+1
        error=False
        for j in range(len(columnas_proyecto1)):
            if(final.loc[i][columnas_proyecto1[j]]!=final.loc[i][columnas_proyecto2[j]]):
                error=True
        if(error):
            final.loc[i]["Resultado"]="KO"
        else:
            final.loc[i]["Resultado"]="OK"




    for i in range(df2.shape[0]):
        if(not any(df1["Nombre"]==df2.loc[i][0])):
            if(tipo=="Filtro"):
                final.loc[final.shape[0]]=[df2.loc[i][0],"",df2.loc[i][1],"KO"]
            else:
                insertar=[df2.loc[i][0],df2.loc[i][1]]
                for j in range(len(columnas_proyecto1)):
                    insertar.append("")
                for j in range(1,len(columnas_revisar)):
                    insertar.append(df2.loc[i][columnas_revisar[j]])
                insertar.append("KO")
                final.loc[final.shape[0]]=insertar

    return final