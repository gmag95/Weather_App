#!/usr/bin/env python
# coding: utf-8

import tkinter as tk
import requests
import xml
import bs4

def create_window(zip):
    
    global start_frame, reset_button, window_frame
   
    api_request=requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/xml&zipCode={zip}&distance=25&API_KEY=705691D1-3DFE-41E9-B4B3-5C99418BFB3B")
    output = bs4.BeautifulSoup(api_request.text,"lxml")

    if len(zip)==0:
        my_message=tk.Label(start_frame, text="You didn't insert a zip code")
        my_message.grid(row=2, column=0, columnspan=2, padx=10, pady=(0,5))
        return
    
    elif len(output.select("datalist"))>0 and output.select("datalist")[0].getText()=="No data":
        my_message=tk.Label(start_frame, text="The zip code was not found")
        my_message.grid(row=2, column=0, columnspan=2, padx=10, pady=(0,5))
        return

    start_frame.destroy()

    values=[]
    present=[]

    for i in range(len(output.select("aqi"))):
        if output.select("parametername")[i].getText()=="O3":
            ozone=int(output.select("aqi")[i].getText())
            values.append(ozone)
            present.append("03")
        elif output.select("parametername")[i].getText()=="PM10":
            pm10=int(output.select("aqi")[i].getText())
            values.append(pm10)
            present.append("PM10")
        elif output.select("parametername")[i].getText()=="PM2.5":
            pm2=int(output.select("aqi")[i].getText())
            values.append(pm2)
            present.append("PM 2.5")

    city=output.select("reportingarea")[0].getText()

    high_value=max(values)

    for i in range(len(values)):
        if high_value==values[i]:
            condition=output.select("CategoryName")[i].getText()

    if condition=="Good":
        color="green3"
    elif condition=="Moderate":
        color="yellow2"
    elif condition=="USG":
        color="dark orange"
    elif condition=="Unhealthy":
        color="red2"
    elif condition=="Very Unhealthy":
        color="dark orchid"
    else:
        color="purple4"

    root.config(bg="white")

    window_frame=tk.Frame(root, bg=color)
    window_frame.grid(row=0, column=0)
    city_label=tk.Label(window_frame, text=f"{city} air quality:")
    city_label.config(font=("Calibri", 18, "bold"))
    city_label.config(bg=color)
    city_label.grid(padx=20)

    labels=[]

    for i in range(len(values)):
        labels.append(tk.Label(window_frame, text=f"{present[i]} level - {values[i]}"))
        labels[i].config(font=("Calibri", 15, "bold"), bg=color)
        labels[i].grid()

    reset_button=tk.Button(text="Reset", relief="sunken", borderwidth=0, command=reset)
    reset_button.grid(row=1, column=0)
    reset_button.config(bg="white", font=("Calibri", 10, "bold"))

def start_screen():

    global start_frame

    root.configure(background='SystemButtonFace')

    start_frame=tk.Frame(root)
    start_frame.grid()

    title=tk.Label(start_frame, text="Enter the US zip code you are looking for:")
    title.grid(row=0, column=0, columnspan=2, padx=10, pady=(5,0))

    entry=tk.Entry(start_frame, width=30)
    entry.grid(row=1, column=0, padx=10, pady=5)

    start_button=tk.Button(start_frame, text="Start", command= lambda : create_window(entry.get()))
    start_button.grid(row=1, column=1, padx=10, pady=5)

def reset():

    global reset_button, window_frame

    reset_button.destroy()
    window_frame.destroy()

    start_screen()



root=tk.Tk()
root.title("Weather app")

start_screen()

root.mainloop()