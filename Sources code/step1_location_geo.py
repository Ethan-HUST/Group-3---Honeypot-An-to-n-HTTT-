import pandas as pd
import geoip2.database

# Đường dẫn tới file GeoLite2-City.mmdb
db_path = r"C:\Users\admin.DESKTOP-DOMJBUQ\Downloads\GeoLite2-City.mmdb"

# Đường dẫn tới file CSV gốc
csv_input = r"C:\Users\admin.DESKTOP-DOMJBUQ\Downloads\archive\parsed_log.csv"

# Đường dẫn tới file xuất ra
csv_output = r"C:\Users\admin.DESKTOP-DOMJBUQ\Downloads\archive\ssh_logs_with_geo.csv"

# Đọc dữ liệu gốc
df = pd.read_csv(csv_input)

# Mở file database địa lý
reader = geoip2.database.Reader(db_path)

# Hàm tra cứu thông tin địa lý từ IP
def get_geo(ip):
    try:
        response = reader.city(ip)
        country = response.country.name
        city = response.city.name or "Unknown"
        return pd.Series([country, city])
    except:
        return pd.Series(["Unknown", "Unknown"])

# Áp dụng hàm lên cột source_ip
df[['Country', 'City']] = df['source_ip'].apply(get_geo)

# Lưu file mới
df.to_csv(csv_output, index=False)

# Đóng kết nối reader
reader.close()

print("Done! File enriched đã được lưu tại:")
print(csv_output)
