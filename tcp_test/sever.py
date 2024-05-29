import socket

host = socket.gethostbyname(socket.gethostname())
port = 5555

address = (host, port)

socket01 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket01.bind(address)
socket01.listen(1)

print('Socket Startup')

conn, addr = socket01.accept()  

print('Connected by', addr)

print('begin write image file "Beasave.png"')
imgFile = open('Beasave.png', 'wb+')
while True:
    imgData = conn.recv(512)
    if not imgData:
        break
    imgFile.write(imgData)
imgFile.close()
print('image save')

conn.close()
socket01.close()
print('server close')
