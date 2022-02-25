import socket
addr=("127.0.0.1",4444)

with socket.socket() as s:	#소켓 생성
    s.connect(addr)		#소켓 연결 요청
    while(1):		#무한 반복
        str1=input("echo: ")	#사용자에게 입력받음
        if(str1 in ('exit', 'quit')):	#finished가 입력되면
            s.send(str1.encode())	#메시지 encoding해서 전송
            s.close()			#소켓 닫음
            break
        s.send(str1.encode())	#메시지 encoding 후 전송
        data=s.recv(1024)		#server로부터 받은 메시지 data에 저장
        print(data.decode())    #data decoding후 출력

    print("program finish")