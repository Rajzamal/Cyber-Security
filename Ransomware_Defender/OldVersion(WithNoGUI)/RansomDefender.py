import hashlib
import os

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
            os.system('cmd /k "mem"')
            break
    else:
        print("File not found")
        os.system('cmd /k "mem"')
        break
