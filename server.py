import socket, cv2, pickle,struct,imutils
ser_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
server_ip = "0.0.0.0"
print('SERVER IP:',server_ip)
port_no= 9999
socket_address = (server_ip,port_no)

# To bind the socket with IP and port
ser_socket.bind((socket_address))

# Socket Listen
ser_socket.listen(5)
print("SERVER LISTENING AT :",socket_address)

# Socket Accept
while True:
    client_socket,address = ser_socket.accept()
    print('friend connection found at :',address)
    if client_socket:
        vid = cv2.VideoCapture(0)
    
        while(vid.isOpened()):
            img,frame = vid.read()
            frame = imutils.resize(frame,width=320)
            a = pickle.dumps(frame)
            message = struct.pack("Q",len(a))+a
            client_socket.sendall(message)
            cv2.imshow('SERVER VIDEO',frame)
            if cv2.waitKey(10)==13:
                client_socket.close()
                cv2.destroyAllWindows()
                vid.release()
                break
