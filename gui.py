from tkinter import *
import socket
 
window = Tk()
 
window.title("Checkport")
 
window.geometry('350x200')

#Dia chi ip
label_adress = Label(window, text="Address", width=10)
label_adress.grid(column=0, row=0, sticky="n")
 
adress = Entry(window,width=20)
adress.grid(column=1, row=0, sticky="n")
#===========================

#Port
label_port = Label(window, text="Port", width=10)
label_port.grid(column=0, row=1)
 
port = Entry(window,width=20)
port.grid(column=1, row=1)
#===========================

result = Label(window, text="", width=20)
result.grid(column=0, row=3)

def checkport(adress,port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex((adress,port))
	if result == 0:
		return "Port is open"
	else:
		return "Port is not open"
	sock.close()
def clicked():
 
    res_add = adress.get()
    # result_address.configure(text= res_add)

    res_p = int(port.get())
    # result_port.configure(text= res_p)
    result.configure(text= checkport(res_add,res_p))

#Button Scan
btn = Button(window, text="Scan", command=clicked)
btn.grid(column=1, row=2)


 
 
window.mainloop()