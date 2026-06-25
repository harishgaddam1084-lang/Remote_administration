import socket
import instructions as ins
c = socket.socket()
c.connect(("localhost", 9993))
print("To exit the program, Enter 'exit' at 'Enter the command type' input")
print("For help, Enter 'help' at 'Enter tue command type'input")
while True:

    command_type = input("Enter the command type : ").strip().lower()

    c.sendall(command_type.encode())
    if command_type.strip().lower() == "exit":
    	print("exiting...")
    	c.close()
    	break
    elif command_type.strip().lower() == "help":
    	ins.help()

    elif command_type.strip().lower()== "cmd":

        command = input("Enter command : ")
        c.sendall(command.encode())

        output = c.recv(1024)
        print(output.decode())

    elif command_type.strip().lower() == "ftp":

        file_name = input("Enter the file name : ")
        c.sendall(file_name.strip().encode())

        output = c.recv(1024)

        if output == b"file not found":
            print("File not found. Give the correct file name.")
            continue

        file_size = int(output)
        received = 0

        with open(file_name, "wb") as file:

            while received < file_size:

                data = c.recv(1024)
                file.write(data)
                received += len(data)

        print(file_name + " file received")

    else:
        print("Invalid command type")