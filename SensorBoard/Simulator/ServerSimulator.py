#README: This server starts on the local IP (not loopback but the real IP) 
#and based on the string that is received it responds acordingly
#Usage: ServerSimulator {PORT}
#Usage example: cmd.exe > python ServerSimulator.py 1234


import socket
import sys
#commands:
getSensorData = str("GetSensorData")
setOutput = str("SetOutput")

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

host_name = socket.gethostname() 
host_ip = socket.gethostbyname(host_name)

try:
    if len(sys.argv) > 1:
        PORT=int(sys.argv[1])
        print("Setting Port=", str(PORT))
    else:
        print("Port not given. Using the default 65432")    
except Exception as e:
    print("Invalid port value. Using the default 65432")
    print(str(e))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #s.bind((HOST, PORT))
    print('Starting server @', host_ip)
    s.bind((host_ip, PORT))
    s.listen()    
    conn, addr = s.accept()    
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(str(data))
            if getSensorData in str(data):
                print("Reading sensor data")
                conn.sendall(b'Temperature=26, Humidity=50, AQI=5')
            elif setOutput in str(data):
                print("Setting outputs")
                conn.sendall(b'Ok')
            else:
                conn.sendall(data)