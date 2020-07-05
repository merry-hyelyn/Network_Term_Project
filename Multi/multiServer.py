# 2020.07.03
# 20174016 김혜린 
# 네트워크 프로그래밍 텀프로젝트
# 소켓프로그래밍 Server

import socket 
from _thread import *


# 쓰레드에서 실행되는 코드 
# 접속한 클라이언트마다 새로운 쓰레드가 생성되어 통신
def threaded(client_socket, addr): 

    items = ['물', '커피', '이온음료','고급 커피', '탄산 음료']
    stock = [3,3,3,3,3]
    price = [450, 500, 550, 700, 750]
    mo = [10, 50, 100, 500, 1000]
    total = 0
    # 연결확인 출력
    print('Connected by :', addr[0], ':', addr[1]) 
    
    # 연결이 확인되면 기본 메뉴 출력
    try:
        # 데이터가 수신되면 클라이언트에 다시 전송(에코)
        name = client_socket.recv(1024)
       
        if not name: 
            print('Disconnected by ' + addr[0],':',addr[1])
            client_socket.close() 

        print('Received from ' + addr[0],':',addr[1] ,name.decode('utf-8'))

        name = "hi " + str(name.decode('utf-8'))
        
        client_socket.send(name.encode('utf-8')) 

        
    # 연결에 오류가 생기면 소켓 닫기
    except ConnectionResetError as e:
        print('Disconnected by ' + addr[0],':',addr[1])
        client_socket.close() 

    # 이외의 상황 발생 시 소켓 닫기
    except Exception as e:
        print(e)
        client_socket.close()

    # 클라이언트가 접속을 끊을 때 까지 반복 
    while True:
        data = """
        ----------menu-----------
        1. 물
        2. 커피
        3. 이온 음료
        4. 고급 커피
        5. 탄산 음료 

        6. 음료 구매하기
        7. 현재 매출액 보기
        0. 끝내기
        -------------------------

        음료 번호(1,2,3,4,5)를 선택하면 재고 확인이 가능합니다.
        """

        client_socket.sendall(data.encode('utf-8'))
        answer = client_socket.recv(1024).decode("utf-8")
        
        if answer == "1":
            if stock[0] == 0:
                t = "현재 물은 품절입니다."
            else:
                t = "물의 가격은 "+str(price[0])+"원 이며" + "현재 "+ str(stock[0]) + "개가 남았습니다.\n"
            client_socket.sendall(t.encode('utf-8'))

        elif answer == "2":
            if stock[1] == 0:
                t = "현재 커피는 품절입니다."
            else:
                t = "커피의 가격은 "+str(price[1])+"원 이며" + "현재 "+ str(stock[1]) + "개가 남았습니다.\n"
            client_socket.sendall(t.encode('utf-8'))

        elif answer == "3":
            if stock[2] == 0:
                t = "현재 이온 음료는 품절입니다."
            else:
                t = "이온 음료의 가격은 "+str(price[2])+"원 이며" + "현재 "+ str(stock[2]) + "개가 남았습니다.\n"
            client_socket.sendall(t.encode('utf-8'))

        elif answer == "4":
            if stock[3] == 0:
                t = "현재 고급 커피는 품절입니다."
            else:
                t = "고급 커피의 가격은 "+str(price[3])+"원 이며" + "현재 "+ str(stock[3]) + "개가 남았습니다.\n"
            client_socket.sendall(t.encode('utf-8'))

        elif answer == "5":
            if stock[4] == 0:
                t = "현재 탄산 음료는 품절입니다."
            else:
                t = "탄산 음료의 가격은 "+str(price[4])+"원 이며" + "현재 "+ str(stock[4]) + "개가 남았습니다.\n"
            client_socket.sendall(t.encode('utf-8'))

        elif answer == "6":
            
            menu = """
            구매하고자 하는 음료 번호를 입력해주세요.
            음료번호를 순서대로 입력해주세요.

            ex) 물과 커피를 구매 시 12
            """
            client_socket.sendall(menu.encode('utf-8'))
            get = client_socket.recv(1024).decode("utf-8")

            money = 0
            get_item = ""

            for i in get:
                money += price[i-1]
                if get_item == "":
                    get_item += items[i-1]
                else:
                    get_item = get_item + "와 " + items[i-1]
                if stock[i-1] != 0:   
                    stock[i-1] -= 1
            
            confirm = "구매하고자 하는 음료가 " + get_item + " 맞으신가요?\n맞으면 y 틀리면 n을 입력해주세요"
            client_socket.sendall(confirm.encode('utf-8'))
            yorn = client_socket.recv(1024).decode("utf-8")

            if yorn == "y":
                total += money
                p = "가격은" + str(money) +"원 입니다\n10원 50원 100원 500원 1000원 순서로 숫자를 입력해주세요\nex) 1100원 -> 00101"
                client_socket.sendall(p.encode('utf-8'))
                m = client_socket.recv(1024).decode("utf-8")

                summ = 0 
                for i in range(5):
                    if m[i] != "0":
                        s = mo[i] * int(m[i])
                        summ += s
                
                re = summ - money
                if re == 0:
                    s = "돈을 알맞게 주셨기 때문에 거스름 돈은 없습니다."
                else:
                    s= "거스름 돈은 "+str(re)+"입니다."
                client_socket.sendall(s.encode('utf-8'))

            else:
                p = "다시 선택해주세요"
                client_socket.sendall(p.encode('utf-8'))

        else: 
            to = "현재 매출액은 "+str(total) +"원 입니다."
            client_socket.sendall(to.encode('utf-8'))
    client_socket.close() 


HOST = '127.0.0.1'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT)) 
server_socket.listen() 

print('server start')

# 클라이언트가 접속하면 accept 함수에서 새로운 소켓을 리턴
# 새로운 쓰레드에서 해당 소켓을 사용하여 통신을
while True: 
    print('wait')

    client_socket, addr = server_socket.accept() 
    start_new_thread(threaded, (client_socket, addr)) 
    
server_socket.close() 