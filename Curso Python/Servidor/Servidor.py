import socket
import subprocess

credentials = ["root: 1234567", "junior: 123", "admin: admin"]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 333)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(server_address)
sock.listen(5)

while True:
    connection , cliet_address = sock.accept()
    print("[*] New connection from {0}:{1}".format(*cliet_address))
    try:
        connection.send(b"Username: ")
        username = connection.recv(32).strip().decode('utf-8')
        connection.send(b"Password: ")
        password = connection.recv(32).strip().decode('utf-8')

        if "{0}:{1}".format(username, password) in credentials:
            connection.send(b"\nWelcome to socket server panel. \n")
        
            while True:
                connection.send(b"$ ")
                data = connection.recv(1024).strip().decode('utf-8')
                if data == "exit":
                    break
                if data == "shell":
                    while True:
                        connection.send(b"SHELL: ")
                        datapoint = connection.recv(2048)
                        proc = subprocess.Popen(datapoint, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        stdout_value = b'\n' + proc.stdout.read() + proc.stderr.read() + b'\n'
                        connection.send(stdout_value)
