from model import Localidad, Vivienda
import psycopg2

ruta_vivienda = "./data/datos_tratados/vivienda_dim.csv"

lista_vivienda = []


with open(ruta_vivienda, 'r', encoding="utf-8") as archivo:
    next(archivo, None)
    
    for linea in archivo:
        
        linea = linea.rstrip()
        separador = ","
        lista = linea.split(",")
       
        #print(lista[1])

        
        vivienda = Vivienda(id_vivienda=int(float(lista[1])), id_casa=int(lista[2]))
            
        lista_vivienda.append(vivienda)
        

#print(lista_vivienda)




# Establecer la conexión
conn = psycopg2.connect(
    host="dpg-chq070ik728ivvqbkdog-a.oregon-postgres.render.com",
    database="db_asma",
    user="root",
    password="cOYOkQFWSQ4KtEBo5hGheF9cyr60DRv5"
)



def insertar_data(lista) -> int:
    try:
        #i = 0
    
        with open("registros.txt", "w") as archivo:
            for value in lista:
                #if i == 5:
                #    break
                insert_query = "INSERT INTO public.vivienda_dim(id_vivienda, id_casa) VALUES "
                registro = insert_query + "(" + str(value.id_vivienda) + "," + str(value.id_casa) + ");\n"
                archivo.write(registro)
                print(registro)
                #i += 1
        return 0
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error al insertar datos", error)
        return -1

print(insertar_data(lista_vivienda))
