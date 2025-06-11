import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc file đã tiền xử lý
file_path = r"C:\Users\admin.DESKTOP-DOMJBUQ\Downloads\archive\ssh_logs_cleaned.csv"
df = pd.read_csv(file_path, parse_dates=['timestamp'])

# Đếm số lần mỗi IP xuất hiện
ip_counts = df['source_ip'].value_counts()
print("\nTop IP tấn công nhiều nhất:")
print(ip_counts.head(10))

# Gán nhãn các IP có hơn N lần tấn công là 'bot'
threshold = 2  # có thể tăng lên nếu dữ liệu lớn hơn
df['bot'] = df['source_ip'].apply(lambda x: 'Bot' if ip_counts[x] > threshold else 'Normal')

# Vẽ biểu đồ số lần tấn công theo thời gian
plt.figure(figsize=(12, 6))
df.set_index('timestamp').resample('1T').size().plot()
plt.title('Số lượng tấn công mỗi phút')
plt.xlabel('Thời gian')
plt.ylabel('Số lần tấn công')
plt.tight_layout()
plt.grid(True)
plt.show()

# Chỉ lấy Top 10 IP tấn công nhiều nhất
top_ips = ip_counts.head(10)  # <-- thêm dòng này

# Vẽ lại biểu đồ
plt.figure(figsize=(10, 5))
sns.barplot(x=top_ips.index, y=top_ips.values)
plt.title('Top 10 IP tấn công nhiều nhất')
plt.ylabel('Số lần tấn công')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

top_n = 10
top_ips = ip_counts.nlargest(top_n)
other_count = ip_counts.iloc[top_n:].sum()

# Tạo DataFrame mới cho biểu đồ
plot_data = top_ips.copy()
plot_data['Other'] = other_count

# Vẽ biểu đồ tròn
plt.figure(figsize=(8, 8))
plot_data.plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Tỷ lệ tấn công từ Top 10 IP và phần còn lại')
plt.ylabel('')
plt.tight_layout()
plt.show()

