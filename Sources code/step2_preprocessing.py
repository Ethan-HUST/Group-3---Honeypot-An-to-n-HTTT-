import pandas as pd

# Đường dẫn file CSV
file_path = r"C:\Users\admin.DESKTOP-DOMJBUQ\Downloads\archive\ssh_logs_with_geo.csv"

# Đọc dữ liệu
df = pd.read_csv(file_path)

# Chuyển timestamp thành datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

# Xoá các dòng không chuyển được thành thời gian (timestamp bị lỗi)
df = df.dropna(subset=['timestamp'])

# Xoá các dòng có IP không hợp lệ (nếu cần)
import ipaddress

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except:
        return False

df = df[df['source_ip'].apply(is_valid_ip)]

# Reset lại index
df = df.reset_index(drop=True)

# Lưu ra file mới
output_path = r"C:\Users\admin.DESKTOP-DOMJBUQ\Downloads\archive\ssh_logs_cleaned.csv"
df.to_csv(output_path, index=False)

print("Đã xử lý xong và lưu file cleaned!")