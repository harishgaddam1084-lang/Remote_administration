# Remote Administration and File Transfer Demo

This project demonstrates TCP socket programming and client-server communication using Python. It consists of a **Host** program that listens for incoming connections and a **Controller** program that connects to the Host. Once connected, the Controller can navigate directories and transfer files over the network.

The project was created for educational purposes to explore concepts such as socket programming, remote command execution, and file transfer mechanisms.

---

# Setup Instructions

## 1. Install Python

Download and install Python 3 from:

https://www.python.org/downloads/

Verify the installation:

```bash
python --version
```

or

```bash
python3 --version
```

---

## 2. Download the Project

### Using Git

```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
```

### Or

Download the ZIP file from GitHub and extract it.

---

## 3. Install Requirements

All required modules are included with Python's standard library.

No additional packages are required.

If a `requirements.txt` file is provided, install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 4. Configure the Programs (Optional)

Open both files and set the desired IP address and port number.

Example:

```python
HOST = "192.168.x.x"
PORT = 9993
```

Ensure both the Host and Controller programs use the same IP address and port.

---

## 5. Start the Host Program

Open a terminal and run:

```bash
python host.py
```

The Host will wait for an incoming connection.

---

## 6. Start the Controller Program

Open another terminal and run:

```bash
python controller.py
```

---

## 7. Using the Program

### Command Mode

At the prompt, enter:

```text
cmd
```

Available commands:

List directories:

```text
ls
```

Change directory:

```text
cd directory_name
```

---

### File Transfer Mode

At the prompt, enter:

```text
ftp
```

Then enter the file name to transfer.

---

## 8. Exit

Press:

```text
Ctrl + C
```

to stop the program.

---

## Requirements

* Python 3.x

---

## Project Structure

```text
project/
│
├── host.py
├── controller.py
├── requirements.txt
└── README.md
```

---

## Disclaimer

This project is intended solely for educational purposes and should only be used in authorized environments. The author is not responsible for any misuse of this software.
