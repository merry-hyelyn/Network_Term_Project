# 2020.07.03
# 20174016 김혜린 
# 네트워크 프로그래밍 텀프로젝트
# 소켓프로그래밍 client

import socket 


HOST = '127.0.0.1'
PORT = 9999

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

client_socket.connect((HOST, PORT)) 



# 키보드로 입력한 문자열을 서버로 전송하고 
# 서버에서 에코되어 돌아오는 메시지를 받으면 화면에 출력
# quit를 입력할 때 까지 반복

name = input('Enter name : ')

client_socket.send(name.encode()) 
data = client_socket.recv(1024) 
print('Received from the server :', str(data.decode('utf-8'))) 
print("자판기 이용을 시작하겠습니다.")

while True: 
    data = client_socket.recv(1024)
    print(str(data.decode('utf-8')))
    
    answer = input('Enter answer : ')
    client_socket.send(answer.encode()) 

    if answer == "0":
        break

client_socket.close() 