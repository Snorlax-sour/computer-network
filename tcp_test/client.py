import socket

host = 'Your ip'
port = 5555
address = (host, port)

socket02 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


socket02.connect(address)

print('start send image')
imgFile = open("Bea.png", "rb")
while True:
    imgData = imgFile.readline(512)
    if not imgData:
        break
    socket02.send(imgData)
imgFile.close()
print('transmit end')

socket02.close()
print('client close')