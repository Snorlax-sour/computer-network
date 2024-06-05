import socket

def rdt_receive(sock):
    expected_seq_num = 0
    while True:
        try:
            data, address = sock.recvfrom(1024)
            seq_num, packet_data = data.split(b'|', 1)
            seq_num = int(seq_num)
            if seq_num == expected_seq_num:
                ack_packet = str(seq_num).encode()
                sock.sendto(ack_packet, address)
                if packet_data == b'END':
                    return None  # 接收结束信号
                expected_seq_num = (expected_seq_num + 1) % 2
                return packet_data
            else:
                ack_packet = str((expected_seq_num - 1) % 2).encode()
                sock.sendto(ack_packet, address)
        except socket.timeout:
            print("Timeout occurred while waiting for data. Retrying...")
            continue
        except ConnectionResetError:
            print("Connection reset by the client. Retrying...")
            continue

host = '172.19.224.1'
port = 5001  # 更改端口号
address = (host, port)

socket01 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    socket01.settimeout(5)  # 设置超时时间
    print('Socket Startup')
    socket01.bind(address) 
    print('begin write image file "moonsave.png"')
    imgFile = open('moonsave.png', 'wb+')
    while True:
        imgData = rdt_receive(socket01)
        if imgData is None:  # 处理结束信号
            break  
        imgFile.write(imgData)
    imgFile.close()
    print('image save')
finally:
    socket01.close()
    print('server close')
