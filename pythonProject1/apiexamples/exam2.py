from tkinter import *
import requests
root=Tk()
root.title('weather')
root.geometry('400x400')
Cityname=StringVar()
Latitude=StringVar()
Longitude=StringVar()
def submit():
    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=3b38f7256941d04dc249f965f535ca29&q='
    city1 = Cityname.get()
    url = api_address + city1
    json_data = requests.get(url).json()
    format_add2 = json_data['coord']['lon']
    format_add3 = json_data['coord']['lat']


    print(format_add2, format_add3)
    Latitude.set(format_add2)
    Longitude.set(format_add3)


Label(root,text='city name').grid(row=0,column=0)
Entry(root,textvariable=Cityname).grid(row=0,column=1)
Label(root,text='latitude').grid(row=1,column=0)
Entry(root,textvariable=Latitude).grid(row=1,column=1)
Label(root,text='longitude').grid(row=2,column=0)
Entry(root,textvariable=Longitude).grid(row=2,column=1)
Button(root,text='submit',command=submit).grid(row=0,column=2)
root.mainloop()

