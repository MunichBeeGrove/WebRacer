import socket

def start_server():
    host = ''
    port = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f'Server listening on port {port}...')

    number_of_calls = 0

    while True:
        client_socket, client_address = server_socket.accept()
        request = client_socket.recv(1024).decode('utf-8')
        print(request)

        number_of_calls +=1
        response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nHello World!'

        with open('MinimalisticRefresh.html', 'r') as file:
            data = file.read().replace('\n', '')
        response += data    
#        response += '\n Number of calls:'
#        response += str(number_of_calls)
        client_socket.sendall(response.encode('utf-8'))
        client_socket.close()

if __name__ == '__main__':
    start_server()