#Ejemplo (Marcelo)
import requests
from pprint import pprint

API_KEY="595695c3"
URL= "http://www.omdbapi.com/?apikey="
titulo= "The Matrix"
busqueda = URL + API_KEY + "&t=" + titulo

respuesta= requests.get(busqueda)
dic_peli= respuesta.json()
pprint(dic_peli)
print(dic_peli["Year"])






#EJ. 1 Consultar el API de OMDB y obtener el nombre del director 
# de Fight Club 
# EJ2. Crear una funcion que reciba como argumento el 
# titulo de una pelicula y retorne los actores de esa pelicula


import requests
from pprint import pprint

API_KEY="595695c3"
URL= "http://www.omdbapi.com/?apikey="
titulo= "Fight Club"
busqueda = URL + API_KEY + "&t=" + titulo

respuesta= requests.get(busqueda)
dic_peli= respuesta.json()
pprint(dic_peli["Director"])


#Ejercicio 3
import requests
from pprint import pprint
API_KEY="595695c3"

def actores (nombre_pelicula):
    URL= "http://www.omdbapi.com/?apikey="
    titulo= "Fight Club"
    busqueda = URL + API_KEY + "&t=" + titulo
    respuesta_http= requests.get(busqueda)
    dic_peli= respuesta_http.json()
    pprint(dic_peli["Actors"])
actores ("Fight Club")















