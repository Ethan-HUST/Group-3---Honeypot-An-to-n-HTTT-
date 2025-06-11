import pandas as pd

# Đường dẫn tuyệt đối đến file CSV
file_path = r"C:\Users\admin.DESKTOP-DOMJBUQ\Downloads\archive\ssh_logs_with_geo.csv"

# Đọc file CSV
df = pd.read_csv(file_path)

# In ra 5 dòng đầu tiên để kiểm tra
print(df.head())
