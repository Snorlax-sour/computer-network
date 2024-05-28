import socket

host = '172.19.224.1'
port = 5000
address = (host, port)  

socket02 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

try:
    socket02.connect(address)  
    print('start send image')
    imgFile = open("moon.png", "rb")
    while True:
        imgData = imgFile.read(512)  
        if not imgData:
            break  
        socket02.send(imgData)
    imgFile.close()
    print('transmit end')
finally:
    socket02.close()  
    print('client close')
