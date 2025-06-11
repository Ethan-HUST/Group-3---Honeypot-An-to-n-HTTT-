import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN

# 1. Đọc dữ liệu từ file CSV
df = pd.read_csv('C:/Users/admin.DESKTOP-DOMJBUQ/Downloads/archive/ssh_logs_with_geo.csv')

# 2. Chuyển cột timestamp sang kiểu datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# 3. Tính thống kê cho mỗi IP nguồn
ip_stats = df.groupby('source_ip').agg(
    attack_count=('timestamp', 'count'),
    first_attack=('timestamp', 'min')
).reset_index()

# 4. Chuyển thời điểm tấn công đầu tiên thành số giây timestamp UNIX
ip_stats['first_attack'] = pd.to_datetime(ip_stats['first_attack'])
ip_stats['first_attack_ts'] = ip_stats['first_attack'].view('int64') // 10**9  # nanoseconds -> seconds

# 5. Chuẩn bị dữ liệu đầu vào cho DBSCAN: 2 chiều [attack_count, first_attack_ts]
X = ip_stats[['attack_count', 'first_attack_ts']].values

# 6. Áp dụng DBSCAN để phân nhóm (tùy chỉnh tham số eps và min_samples theo dữ liệu)
db = DBSCAN(eps=0.5, min_samples=3)
ip_stats['cluster'] = db.fit_predict(X)

# 7. Hiển thị kết quả
print(ip_stats[['source_ip', 'attack_count', 'first_attack', 'cluster']].sort_values(by='cluster'))
