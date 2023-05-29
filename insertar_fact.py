from model import Localidad, Vivienda, Hacinamiento
import psycopg2

ruta_vivienda = "./data/datos_tratados/hacinamiento_fact_actualizada.csv"

lista_hacinamiento = []


with open(ruta_vivienda, 'r', encoding="utf-8") as archivo:
    next(archivo, None)
    
     
    for linea in archivo:
        
        
        linea = linea.rstrip()
        separador = ","
        lista = linea.split(",")
       
        #print(lista[1])

        
        vivienda = Hacinamiento(num_personas_hogar=int(lista[1]), num_cuartos_hogar=int(lista[2]), ocupacion=float(lista[3]), cantidad_asma=int(lista[4]),
                                porcentaje_iluminacion=float(lista[5]), id_year=int(lista[6]), id_asma=int(lista[7]), id_localidad=int(lista[8]), id_casa=int(lista[9]))
            
        lista_hacinamiento.append(vivienda)
   
        

#print(lista_hacinamiento)




def insertar_data(lista) -> int:
    try:
        #i = 0
    
        with open("registros_fact.txt", "w") as archivo:
            for value in lista:
                #if i == 5:
                #    break
                insert_query = "INSERT INTO public.hacinamiento_fact(cantidad_personas, cantidad_cuartos, hacinamiento, cantidad_asma, porcentaje_luz_natural, id_year, id_asma, id_localidad, id_casa) VALUES "
                registro = insert_query + "(" + str(value.num_personas_hogar) + "," + str(value.num_cuartos_hogar) + "," + str(value.ocupacion) + "," + str(value.cantidad_asma) + "," + str(value.porcentaje_iluminacion) + "," + str(value.id_year) + "," + str(value.id_asma) + "," + str(value.id_localidad) + "," + str(value.id_casa) + ");\n"
                archivo.write(registro)
                print(registro)
                #i += 1
        return 0
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error al insertar datos", error)
        return -1

print(insertar_data(lista_hacinamiento))
