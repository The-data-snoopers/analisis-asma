from model import Localidad, Vivienda
import psycopg2

ruta_localidad= "./data/datos_tratados/localidad_dim.csv"


ruta_vivienda = "./data/datos_tratados/vivienda_dim.csv"

lista_localidades = []

lista_vivienda = []



with open(ruta_localidad, 'r', encoding="utf-8") as archivo:
    next(archivo, None)
    
    for linea in archivo:
        
        linea = linea.rstrip()
        separador = ","
        lista = linea.split(",")
       
        #print(lista[1])

        
        localidad = Localidad(localidad=str(lista[1]), id_localidad=int(lista[2]))
            
        lista_localidades.append(localidad)
        

print(lista_localidades)




# Establecer la conexión
conn = psycopg2.connect(
    host="dpg-chq070ik728ivvqbkdog-a.oregon-postgres.render.com",
    database="db_asma",
    user="root",
    password="cOYOkQFWSQ4KtEBo5hGheF9cyr60DRv5"
)



def insertar_data(lista) -> int:

    try: 
        # Crear un cursor
        cursor = conn.cursor()

        for value in lista:
            print(value.localidad)
            
            # Ejecutar una inserción
            insert_query = "INSERT INTO public.localidad_dim(localidad, id_localidad) VALUES (%s, %s)"
            data = (value.localidad, value.id_localidad)
            cursor.execute(insert_query, data)

        # Confirmar la transacción
        conn.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
        return 0
    except (Exception, psycopg2.DatabaseError) as error:

        print("Error al insertar datos", error)
        return -1


print(insertar_data(lista_localidades))
