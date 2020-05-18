#Carga de funciones creadas en el fichero Glosario_lib.py
from Glosario_lib import *
#Carga de paquete para obtener la fecha actual
from datetime import date
#Carga de paqeute para llamadas al sistema
import os

#Fichero donde se almacena las propiedades de incio sesion
properties="Properties.txt"

#Nombre del Glosario con formato Glosario_YYYYMMDD.xlsx con la fecha que se ejecuto
today = str(date.today())
today=today.replace("-","")
path= r".\Integración"+"_"+today+".xlsx"

print("eliminado registros temporales del sistema")

#Elimina todos los ficheros que almacena la salida y los scripts de Command Manager
clear_files()

print("registros temporales eliminados")

#Obtiene el nombre del origen y el susuario a partir del fichero properties
origenes,usuarios=get_properties(properties)

proyectos=[]
salidas=["salida/proyecto1","salida/proyecto2"]

for i in range(2):

    print("Se va a coger los datos del Origen "+str(i+1))
    print("Nombre de origen de datos : "+origenes[i] )
    print("Nombre de Usuario : "+usuarios[i] )
    password=input("Introduzca la contraseña del Usuario : ")

    #Peticion de la contraseña
    if(password!=""):
        password=" -p "+password

    print("obteniendo proyectos con esta configuracion")

    #LLamanda al Command Manager para obtener el listado de proyectos y almacenarlos en projects.out
    get_inicio_sesion(origenes[i],usuarios[i],password,salidas[i])

    #Abre el fichero projects.out y lee todos los projectos y lo almancena en un vector
    projects=list_projects(salidas[i]+'/projects.out')

    #Salida en pantalla de todos los proyectos que tenemos acceso
    print("Elija el numero de proyecto : ")
    for j in range(len(projects)):
        print(str(j)+" : "+projects[j])
    #Peticion del proyecto
    proyecto = int(input("Ponga el numero de proyecto con que quiera obtener el Glosario: "))

    #Filtro de inserccion de un proyecto correcto
    while(proyecto<0 or proyecto>=len(projects)):
        proyecto = int(input("Ponga correctamente el numero, debe ser entre 0 y "+str(len(projects)-1)+" : "))

    print("Creando scp temporales")
    proyectos.append(projects[proyecto])
    #Creacion de todos los scripts de obtencion de las propiedades de todos los objetos
    create_scp(projects[proyecto])

    print("Scp temporales creados")

    #Ejecucion de los Scripts usando el Command Manager y almancenadolos en sus correspondientes salidas
    get_properties_command(origenes[i],usuarios[i],password,salidas[i])

    print("Todas las caracteristicas obtenidas")
    clear_files_scripts()

print("Creando Excel")


#Lectura de las propiedades de todos los hechos, filtrados por las datos que queremos y almacenados en un dataframe "hechos"
hechos_p1=file_hechos('salida/proyecto1/hechos.out','./salida/proyecto1/detalles_hechos.out')

#Lectura de las propiedades de todos los atributos, filtrados por las datos que queremos y almacenados en un dataframe "Atributo"
Atributo_p1=file_atributos('salida/proyecto1/atributos.out','./salida/proyecto1/detalles_atributos.out')

#Lectura de las propiedades de todos las metricas, filtrados por las datos que queremos y almacenados en un dataframe "metricas"
metricas_p1=file_metricas('salida/proyecto1/metricas.out','./salida/proyecto1/detalles_metricas.out')

#Lectura de las propiedades de todos los filtros, filtrados por las datos que queremos y almacenados en un dataframe "filtros"
filtros_p1=file_filtros('salida/proyecto1/detalles_filtros.out')


#Lectura de las propiedades de todos los hechos, filtrados por las datos que queremos y almacenados en un dataframe "hechos"
hechos_p2=file_hechos('salida/proyecto2/hechos.out','./salida/proyecto2/detalles_hechos.out')

#Lectura de las propiedades de todos los atributos, filtrados por las datos que queremos y almacenados en un dataframe "Atributo"
Atributo_p2=file_atributos('salida/proyecto2/atributos.out','./salida/proyecto2/detalles_atributos.out')

#Lectura de las propiedades de todos las metricas, filtrados por las datos que queremos y almacenados en un dataframe "metricas"
metricas_p2=file_metricas('salida/proyecto2/metricas.out','./salida/proyecto2/detalles_metricas.out')

#Lectura de las propiedades de todos los filtros, filtrados por las datos que queremos y almacenados en un dataframe "filtros"
filtros_p2=file_filtros('salida/proyecto2/detalles_filtros.out')


Atributo=integracion(Atributo_p1,Atributo_p2,"origen1_"+proyectos[0],"origen2_"+proyectos[1],"Atributos")
metricas=integracion(metricas_p1,metricas_p1,"origen1_"+proyectos[0],"origen2_"+proyectos[1],"Indicadores")
hechos=integracion(hechos_p1,hechos_p2,"origen1_"+proyectos[0],"origen2_"+proyectos[1],"Hechos")
filtros=integracion(filtros_p1,filtros_p2,"origen1_"+proyectos[0],"origen2_"+proyectos[1],"Filtro")


#Formato del dataframe "hechos" para que las columnas 'Nombre', 'Ruta', 'Expresión', 'Tabla de origen' esten en color gris
hechos_style=hechos.style.applymap(highlight_cols_grey,subset=pd.IndexSlice[:, hechos.columns[:-3]])
#Formato del dataframe "hechos" para que las columnas 'Descripción','Nuevo Nombre','Nueva Ruta' en color amarillo
hechos_style=hechos_style.applymap(highlight_cols_orange, subset=pd.IndexSlice[:, hechos.columns[-3:-1]])
hechos_style=hechos_style.applymap(highlight_cols_yelllow, subset=pd.IndexSlice[:, hechos.columns[-1]])


#Formato del dataframe "Atributo" para que las columnas 'Nombre', 'Ruta', 'Representacion', 'Tabla de origen', 'Expresion' esten en color gris
Atributo_style=Atributo.style.applymap(highlight_cols_grey, subset=pd.IndexSlice[:, Atributo.columns[:-4]])
#Formato del dataframe "Atributo" para que las columnas 'Descripción','Nuevo Nombre','Nueva Ruta' esten en color amarillo
Atributo_style=Atributo_style.applymap(highlight_cols_orange, subset=pd.IndexSlice[:, Atributo.columns[-4:-1]])
Atributo_style=Atributo_style.applymap(highlight_cols_yelllow, subset=pd.IndexSlice[:, Atributo.columns[-1]])


#Formato del dataframe "metricas" para que las columnas 'Nombre', 'Ruta', 'Fórmula', 'Condición', 'Transformación', 'Expresión' esten en color gris
metricas_style=metricas.style.applymap(highlight_cols_grey, subset=pd.IndexSlice[:,metricas.columns[:-5]])
#Formato del dataframe "metricas" para que las columnas 'Descripción','Nuevo Nombre','Nueva Ruta' esten en color amarillo
metricas_style=metricas_style.applymap(highlight_cols_orange, subset=pd.IndexSlice[:, metricas.columns[-5:-1]])
metricas_style=metricas_style.applymap(highlight_cols_yelllow, subset=pd.IndexSlice[:, metricas.columns[-1]])

#Formato del dataframe "filtros" para que las columnas 'Nombre Filtro', 'Expresión' esten en color gris
filtros_style=filtros.style.applymap(highlight_cols_grey, subset=pd.IndexSlice[:, filtros.columns[:-2]])
#Formato del dataframe "filtros" para que las columnas 'Descripción' esten en color amarillo
filtros_style=filtros_style.applymap(highlight_cols_orange, subset=pd.IndexSlice[:, filtros.columns[-2:-1]])
filtros_style=filtros_style.applymap(highlight_cols_yelllow, subset=pd.IndexSlice[:, filtros.columns[-1]])

print("Formateando Excel")

#Creacion del excel a partir de los anteriores dataframes
writer = pd.ExcelWriter(path, engine='xlsxwriter')
Atributo_style.to_excel(writer, 'Atributos', index=False)
metricas_style.to_excel(writer, 'Indicadores', index=False)
hechos_style.to_excel(writer, 'Hechos', index=False)
filtros_style.to_excel(writer, 'Filtros', index=False)

#Mofidicacion de la pagina Atributos para poner el ancho de las columnas en funcion de la maxima longitud de contenido en la celda
workbook = writer.book
worksheet = writer.sheets['Atributos']
for i in range(len(Atributo.columns)):
    worksheet.set_column(chr(ord('A')+i)+':'+chr(ord('A')+i+1), Atributo[Atributo.columns[i]].map(len).max()+10)


#Mofidicacion de la pagina Indicadores para poner el ancho de las columnas en funcion de la maxima longitud de contenido en la celda
workbook = writer.book
worksheet = writer.sheets['Indicadores']
for i in range(len(metricas.columns)):
    worksheet.set_column(chr(ord('A')+i)+':'+chr(ord('A')+i+1), metricas[metricas.columns[i]].map(len).max()+10)


#Mofidicacion de la pagina Hechos para poner el ancho de las columnas en funcion de la maxima longitud de contenido en la celda
workbook = writer.book
worksheet = writer.sheets['Hechos']
for i in range(len(hechos.columns)):
    worksheet.set_column(chr(ord('A')+i)+':'+chr(ord('A')+i+1), hechos[hechos.columns[i]].map(len).max()+10)


#Mofidicacion de la pagina Filtros para poner el ancho de las columnas en funcion de la maxima longitud de contenido en la celda
workbook = writer.book
worksheet = writer.sheets['Filtros']
for i in range(len(filtros.columns)):
    worksheet.set_column(chr(ord('A')+i)+':'+chr(ord('A')+i+1), filtros[filtros.columns[i]].map(len).max()+10)


#Guardar el Excel y almacenar toda la información en el.
writer.save()
print("Integridad realizado con exito")


eleccion=input("Ponga Y/N si quiere exportar los dos proyectos en csv : ")

if(eleccion.lower()=="y"):
    print("Exportando el primer proyecto a csv")
    hechos_p1.to_csv("csv/"+"origen1_"+proyectos[0]+"_Hechos_"+today+".csv",index = None, header=True,encoding='utf-8-sig')
    filtros_p1.to_csv("csv/"+"origen1_"+proyectos[0]+"_Filtros_"+today+".csv",index = None, header=True,encoding='utf-8-sig')
    metricas_p1.to_csv("csv/"+"origen1_"+proyectos[0]+"_Metricas_"+today+".csv",index = None, header=True,encoding='utf-8-sig')
    Atributo_p1.to_csv("csv/"+"origen1_"+proyectos[0]+"_Atributos_"+today+".csv",index = None, header=True,encoding='utf-8-sig')
    print("csv realizados con exito")

    print("Exportando el segundo proyecto a csv")
    hechos_p2.to_csv("csv/"+"origen2_"+proyectos[1]+"_Hechos_"+today+".csv",index = None, header=True,encoding='utf-8-sig')
    filtros_p2.to_csv("csv/"+"origen2_"+proyectos[1]+"_Filtros_"+today+".csv",index = None, header=True,encoding='utf-8-sig')
    metricas_p2.to_csv("csv/"+"origen2_"+proyectos[1]+"_Metricas_"+today+".csv",index = None, header=True,encoding='utf-8-sig')
    Atributo_p2.to_csv("csv/"+"origen2_"+proyectos[1]+"_Atributos_"+today+".csv",index = None, header=True,encoding='utf-8-sig')
    print("csv realizados con exito")
    print("Los csv se han almacenado en la carpeta csv")
else:
    print("No se exportaran los proyectos a csv")


