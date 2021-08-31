import hashlib
import os
from tkinter import * 
from tkinter import messagebox
import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("knownoutlander@gmail.com","Test@7250#")

root = Tk()
root.title("Ransom Defender")
root.geometry("700x450")

bg = PhotoImage(file= "C:/Users/Knownoutlander/Desktop/mem freeze/robo.png")
my_label =Label(root,image=bg)
my_label.place(x=0,y=0,relheight=1,relwidth=1)

def startprocess():
    root.wm_state('iconic')
    file = "C:/Users/Knownoutlander/Desktop/Flag_1/flag_1.txt" # Location of the file (can be set a different way)
    BLOCK_SIZE = 65536 # The size of each read from the file
    print("We are checking!!")
    while True:
        if os.path.exists(file):
            file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
            with open(file, 'rb') as f: # Open the file to read it's bytes
                fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
                while len(fb) > 0: # While there is still data being read from the file
                    file_hash.update(fb) # Update the hash
                    fb = f.read(BLOCK_SIZE) # Read the next block from the file
            hashed = file_hash.hexdigest()
            #print(hashed) # Get the hexadecimal digest of the hash
            if(hashed !="da9540cc7ed58f38f7f83648027ad420f4b0d1bf26478758cbd856a7ef7ab1b8"):
                
                print("Ransomeware Detected detach Your Hard drive")
                server.sendmail("knownoutlander@gmail.com","rajzamal123@gmail.com","Detach your hard drive Ransomware detected")
                server.quit()
                os.system('start cmd /c "taskmgr"') 
                os.system('start cmd /c "mem"')
                os.system('cmd /k "shutdown /s"')
                messagebox.showwarning( "Alert", "Detach your hard drive Ransomware detected")
                break
        else:
            print("Ransomeware Detected detach Your Hard drive")
            server.sendmail("knownoutlander@gmail.com","rajzamal123@gmail.com","Detach your hard drive Ransomware detected")
            server.quit()
            os.system('start cmd /c "taskmgr"') 
            os.system('start cmd /c "mem"')
            os.system('cmd /k "shutdown /s"')
            messagebox.showwarning( "Alert", "Detach your hard drive Ransomware detected")
            break


B1 = Button(root, text ="START", command = startprocess,padx=100)
B2 = Button(root, text ="EXIT", command = root.destroy,padx=50)
B1.pack(side=TOP)
B2.pack(side=BOTTOM)  
root.mainloop() 
