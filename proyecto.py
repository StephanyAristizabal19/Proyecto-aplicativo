import tkinter as tk
from tkinter import messagebox

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