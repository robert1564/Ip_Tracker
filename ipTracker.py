import tkinter as tk
import tkintermapview
import requests
import ipaddress

from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

def ipFinder(outputMsg, inputValue):
    try:
        ipAddress = inputValue.get()
        ipaddress.ip_address(ipAddress)
        response = requests.get(f'https://ipapi.co/{ipAddress}/json/').json()
        ip_version = response.get("version")
        city = response.get("city")
        region = response.get("region")
        country = response.get("country_name")
        postlcode = response.get("postal")
        continent = response.get("continent_code")
        lat = response.get("latitude")
        lng = response.get("longitude")
        outputMsg.config(text= "Informations for " + inputValue.get() + ":" + "\n" +
                                ("<--------------->") + "\n" 
                                "Ip Version" + " : " + str(ip_version) + "\n"
                                "City" + " : " + str(city) + "\n"
                                "Region" + " : " + str(region) + "\n"
                                "Country" + " : " + str(country) + "\n"
                                "Postal Code" + " : " + str(postlcode) + "\n"
                                "Continent" + " : " + str(continent) + "\n"
                                "Latitude" + " : " + str(lat) + "\n" +
                                "Longitude" + " : " + str(lng) + "\n" +
                                ("<--------------->") + "\n")

        # tkintermapview to fullfield my_label with exact location of Ip address using lat and lng
        map_widget.set_position(lat, lng)
        # set_marker to set the marker on my map to see the Ip location
        map_widget.set_marker(lat, lng, text= "Ip Location")
        map_widget.grid()

        my_slider.config(value=18)

        my_label.grid(row=2, columnspan=4, column=2, padx=30, sticky="e")
    except:
        outputMsg.config(text="Please Enter Correct IP")

def clear(outputMsg, my_label):
    outputMsg.config(text="")
    my_label.grid_forget()

def slide(e):
    map_widget.set_zoom(my_slider.get())

Tk = tk.Tk()
Tk.geometry("600x300")

# Label for Author
authorLabel = tk.Label(Tk, text="Chill Coding with Robert", background="white", foreground="black")
authorLabel.place(relx= 1.0, rely=0.0, anchor='ne')

inputString = tk.StringVar()

# Label for Entry
ipLabel = tk.Label(Tk, text="Enter Ip: ", background="#28334A", foreground="#F65058")
ipLabel.grid(row=0, pady=10, sticky="ne")

# Input Entry for Ip
input_entry = tk.Entry(Tk, textvariable=inputString)
input_entry.grid(row=0, column=1, pady=10, sticky="ne")

# Label for parseing the API info
outputMsg = tk.Label(Tk, background="#28334A", foreground="#F65058")
outputMsg.grid(row=2, columnspan=4, column=0, padx=30, sticky="w")

# Define LabelFrame to show the map on my app
my_label = tk.LabelFrame(Tk)
map_widget = tkintermapview.TkinterMapView(my_label, width=350, height=200, corner_radius=2)

# Button for Search Ip
button = tk.Button(Tk, text="Check IP", command=lambda : ipFinder(outputMsg, inputString))
button.grid(row=3, columnspan=4, column=0, padx=250, pady=10, sticky="w")

# Button for Clear
button2 = tk.Button(Tk, text="Clear", command=lambda : clear(outputMsg, my_label))
button2.grid(row=3, columnspan=5, column=1, padx=250, pady=10, sticky="e")

# Slider for Zoom
my_slider = ttk.Scale(Tk, from_=4, to=20, orient=HORIZONTAL, command=slide, value=18, length=150)
my_slider.grid(row=3, column=2, padx=30, pady=10, sticky="e")

Tk.title("IP ADDRESS TRACKER")
Tk.configure(background="#28334A")
Tk.rowconfigure(0, weight=1)
Tk.columnconfigure(0, weight=1)
Tk.rowconfigure(2, weight=1)
Tk.columnconfigure(2, weight=1)
Tk.mainloop()