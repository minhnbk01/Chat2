# TCP_Chat_Project/start_server.py

from server.server_core import ChatServer

if __name__ == "__main__":
    # Điểm khởi đầu của chương trình Server
    server = ChatServer()
    server.start()