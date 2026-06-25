import socket
import os
import subprocess

s = socket.socket()
s.bind(("localhost", 9993))
s.listen(3)
print("waiting")
c, addr = s.accept()
print("connected")

def commands():
    print("command mode")
    command = c.recv(1024).decode()
    print(command)
    
    if command[0:2].strip().lower() == "cd":
        message1 = command
        os.chdir(message1[2:].strip())
        verification = "succesfully dir changed "
        c.sendall(verification.encode())

    elif command.strip().lower()== "ls":
        message2 = command.strip().lower()
        output = subprocess.run(message2, capture_output=True)
        print("listed all directories")
        output1 = output.stdout
        c.sendall(output1)
        print("sent all directories")


    else:
        error = "invalid command"
        c.sendall(error.encode())


def file_transfer():
    print("ftp mode")
    file_name = c.recv(1024)
    filename = file_name.decode()
    
    
        
               

    try:
        size = os.path.getsize(filename)
        c.sendall(str(size).encode().ljust(16))
        with open(filename, "rb") as file:
            data = file.read()

        c.sendall(data)
        print(filename+" file is sent")

    except FileNotFoundError:
        print("file not found")
        c.sendall(b"file not found")

    if file_name.decode().strip() == "exit":
        pass


while True:
    type = c.recv(1024).decode()
    if type.strip().lower() == "exit":
    	print("closing the connection...")
    	c.close()
    	print("re-running the client connection")
    	print("waiting for connections")
    	c,addr = s.accept()
    	print("connected")
    if type.strip().lower() == "cmd":
    	commands()

    elif type.strip().lower() == "ftp":
        file_transfer()
        
#This program does work.it is real and updated one.it supports the file transfer(all types of files)