# TCP_Chat_Project/server/ban_manager.py

import os
from config import BANS_FILE

def ensure_ban_file_exists():
    """Đảm bảo file bans.txt luôn tồn tại để tránh lỗi I/O."""
    if not os.path.exists(BANS_FILE):
        open(BANS_FILE, 'w').close()

def is_banned(username):
    """
    Kiểm tra xem một username có trong danh sách cấm hay không.
    Trả về True nếu bị cấm, False nếu không.
    """
    ensure_ban_file_exists()
    with open(BANS_FILE, 'r') as f:
        bans = [line.strip() for line in f.readlines()]
        return username in bans

def ban_user(username):
    """
    Thêm một username vào danh sách cấm.
    Chỉ thêm nếu người dùng chưa có trong danh sách.
    """
    ensure_ban_file_exists()
    if not is_banned(username):
        with open(BANS_FILE, 'a') as f:
            f.write(f"{username}\n")