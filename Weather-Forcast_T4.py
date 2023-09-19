# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:25:39 2023

@author: DELL
"""
import requests
import tkinter as tk
from tkinter import messagebox

def get_weatherinfo():
    city = city_entry.get()
    api_key = "49f4c9e7e6f88bcd24a0286fdc250b72"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        temperature = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        message = f'Temperature is: {temperature}°C\nWeather is: {weather_desc.capitalize()}'
        messagebox.showinfo(F'Weather Forecast in {city} ', message) #Details of
    else:
        messagebox.showerror('Error Occured:', 'City is not found. Please Enter the Correct Spelling of your City.')

# Create the GUI
root = tk.Tk()
root.title('Weather Forecast by Chetan Dawani')
root.geometry("400x150")
root.config(bg="Aqua")

# Label and Entry for City Input
city_label = tk.Label(root, text='Enter City:' , font=('Arial Black', 12, ''))
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()
city_entry.pack(pady=10)

# Button for Weather Forecast
get_weatherinfo_button = tk.Button(root, text='Get Weather', command=get_weatherinfo, font=('Book Antiqua', 14, 'bold'), bg = "Lightblue")
get_weatherinfo_button.pack()
get_weatherinfo_button.pack(pady=28)

root.mainloop()