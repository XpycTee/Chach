import socket
import ssl
import threading

connections = []
PING = 0.01

sock = ssl.wrap_socket(socket.socket(), 'certs/key_chat_server.key', 'certs/cert_chat_server.crt', True)

sock.bind(('', 7112))

sock.listen(32)


def reply_messages_to_all(sender_conn, message):
    for connection in connections:
        if connections != [] and connection != sender_conn:
            connection.send(message.encode())


def wait_message(client_sock, address, nickname):
    while True:
        try:
            msg = client_sock.recv(1024).decode()
            print(f'{nickname}: {msg}')
            reply_messages_to_all(client_sock, f'{nickname}: {msg}')
        except ConnectionResetError:
            print(f"Connection with {nickname} {address} reset")
            connections.remove(client_sock)
            reply_messages_to_all(client_sock, f'{nickname} вышел из чача')
            break


def main():
    while True:
        connection, address = sock.accept()
        connections.append(connection)
        try:
            nickname = connection.recv(1024).decode()
            connection.send("Welcome to Чач".encode())
            reply_messages_to_all(connection, f'{nickname} вошел в чач')
            print(f'{nickname} connected:', address)
            wait_msg_thread = threading.Thread(target=wait_message, args=(connection, address, nickname))
            wait_msg_thread.start()
        except ConnectionResetError:
            print(f"Connection with {nickname} reset")
            connections.remove(connection)
            reply_messages_to_all(connection, f'{nickname} вышел из чача')
        except Exception as e:
            print(e.message, e.args)
    sock.close()


main_thread = threading.Thread(target=main, args=())
main_thread.start()







