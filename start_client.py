# TCP_Chat_Project/start_client.py

from client.client_core import ChatClient

if __name__ == "__main__":
    # Điểm khởi đầu của chương trình Client
    client = ChatClient()
    client.start()