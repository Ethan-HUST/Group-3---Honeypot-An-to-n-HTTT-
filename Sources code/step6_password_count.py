import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
df = pd.read_csv('C:/Users/admin.DESKTOP-DOMJBUQ/Downloads/archive/ssh_logs_with_geo.csv')

# Đếm số lần mỗi mật khẩu xuất hiện
password_counts = df['password'].value_counts().head(10)  # Lấy top 10 mật khẩu phổ biến nhất

# Vẽ biểu đồ
plt.figure(figsize=(10, 6))
password_counts.plot(kind='bar', color='orange', edgecolor='black')

plt.title('Top 10 mật khẩu bị thử nhiều nhất')
plt.xlabel('Mật khẩu')
plt.ylabel('Số lần bị thử')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
