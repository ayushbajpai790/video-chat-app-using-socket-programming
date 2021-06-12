# CLient Side program
import socket,cv2, pickle,struct
import sys

# create socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_ip = '192.168.56.1' # paste your server ip address here
port = 9999
client_socket.connect((server_ip,port)) 
data = b""
payload_size = struct.calcsize("Q") # to calculate payload size
while True:
    while len(data) < payload_size:
        packet = client_socket.recv(4*1024) # 4K
        if not packet: 
            cv2.destroyAllWindows()
            sys.exit("meeting ended by friend ")

        data+=packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q",packed_msg_size)[0]

    while len(data) < msg_size:
        data += client_socket.recv(4*1024)
    frame_data = data[:msg_size]
    data  = data[msg_size:]
    client_frame = pickle.loads(frame_data)
    cv2.imshow("Client VIDEO",client_frame)
    if cv2.waitKey(10)==13:
        cv2.destroyAllWindows()
        client_socket.close()
        break
