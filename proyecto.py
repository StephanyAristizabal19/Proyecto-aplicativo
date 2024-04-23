import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import requests


API_KEY = "3dc16e924fe5d0f038703fa200f95998"


def get_weather_data(ciudades):
    datos_ciudades = []  
    
    for ciudad in ciudades:
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            response.raise_for_status()
            
        
            datos = response.json()
            temperatura_actual = datos['main']['temp']
            sensacion_termica = datos['main']['feels_like']
            temp_maxima = datos['main']['temp_max']
            temp_minima = datos['main']['temp_min']
            humedad = datos['main']['humidity']
            
            datos_ciudades.append((ciudad, temperatura_actual, sensacion_termica, temp_maxima, temp_minima, humedad))
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error de Conexión", f"No se pudo obtener los datos para la ciudad {ciudad}. Error: {str(e)}")
    
    return datos_ciudades


root = tk.Tk()
root.title("Consulta de Clima")
root.geometry("400x150")


ciudad_label = tk.Label(root, text="Ingrese el nombre de la ciudad:", font=("Arial", 13))
ciudad_label.pack()
ciudad_entry = tk.Entry(root, font=("Arial", 13))
ciudad_entry.pack()

obtener_clima_button = tk.Button(root, text="Obtener Clima", font=("Arial", 13), bg="green", fg="white", command=lambda: show_weather_data(ciudad_entry.get()))
obtener_clima_button.pack(pady=10)


root.mainloop()