import socket
addr=("0.0.0.0",4444) #포트번호 4444
with socket.socket() as s:	#소켓 할당
    
    s.bind(addr)	#소켓 바인딩
    s.listen()		#client의 연결요청 대기
    print("Server is started...")
    
#------------------------------------서버 개통과정--------------

    conn,addr = s.accept()	#client 연경 요청을 수락
    print("accept {}:{}".format(addr[0],addr[1]))	#연결된 client 정보 출력
    running = True
    while(running):	#무한반복
        data=conn.recv(1024)	#client가 보낸 메시지를 data에 저장
        if(data.decode() in ('quit', 'exit')):	#data decoding 결과가 finished면
            running = False	#반복문 탈출
        conn.send(data)			#data를 그대로 client에게 전송
        print(data.decode())	#보낸 데이터 읽기
    print("Server finished")	#서버 종료 알리기