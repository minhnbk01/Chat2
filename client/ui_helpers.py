# TCP_Chat_Project/client/ui_helpers.py

def print_help_menu(is_admin=False):
    """In ra menu các lệnh có thể sử dụng."""
    print("\n--- CÁC LỆNH HỖ TRỢ ---")
    print("/list          - Xem danh sách người dùng online")
    print("/msg <tên> <nd> - Gửi tin nhắn riêng cho một người")
    print("/all <nd>      - Gửi tin nhắn cho tất cả mọi người")
    print("/quit          - Thoát chương trình")
    
    if is_admin:
        print("\n--- Lệnh Admin ---")
        print("/kick <tên>    - Đuổi một người dùng khỏi phòng chat")
        print("/ban <tên>     - Cấm một người dùng vĩnh viễn")
        
    print("-----------------------\n")

def print_incoming_message(msg):
    """
    In tin nhắn đến mà không làm xáo trộn dòng lệnh người dùng đang gõ.
    Kỹ thuật: \r (về đầu dòng) -> in đè tin nhắn -> in lại dấu nhắc '>> '.
    """
    print(f"\r{msg}\n>> ", end="", flush=True)