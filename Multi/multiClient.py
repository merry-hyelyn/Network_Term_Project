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

name = input('Enter name : ')

client_socket.send(name.encode('utf-8')) 
return_name = client_socket.recv(1024) 
print('Received from the server :', str(return_name.decode('utf-8'))) 
print("자판기 이용을 시작하겠습니다.")

# 자판기 종료 버튼 누를 때까지 계속
while True: 
    # 자판기화면 출력 및 선택한 메뉴에 대한 명령 실행 결과 출력
    data = client_socket.recv(1024)
    print(str(data.decode('utf-8')))
    
    # 자판기 메뉴를 선택한 번호를 서버로 전송
    answer = input('Enter answer : ')
    client_socket.send(answer.encode('utf-8')) 

    if answer == "0":
        print("자판기 이용을 종료합니다.")
        break

client_socket.close() 