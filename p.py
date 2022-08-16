import requests
import tkinter as tk


m = input('enter the name of music: ')

window = tk.Tk()
window.title('google')

def music():
    url = "https://shazam.p.rapidapi.com/search"

    querystring = {"term":"{}","locale":"en-US","offset":"0","limit":"5".format(m)}

    headers = {
	    "X-RapidAPI-Key": "a8fda380femsh9ce422460c182f3p1d80a5jsn77c64e2ebc2a",
	    "X-RapidAPI-Host": "shazam.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    text = tk.Text()
    text.pack()
    text.insert('1.0', response.text)
music()

button = tk.Button(text='click me',  fg='white', bg='red', 
                    command=music)
button.pack()

window.mainloop()