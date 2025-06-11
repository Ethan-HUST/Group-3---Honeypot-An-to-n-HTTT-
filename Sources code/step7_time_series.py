import pandas as pd
import plotly.express as px

df = pd.read_csv('C:/Users/admin.DESKTOP-DOMJBUQ/Downloads/archive/ssh_logs_with_geo.csv')

# Chuyển 'timestamp' sang datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Tạo cột ngày (không lấy giờ phút)
df['date'] = df['timestamp'].dt.date

# Đếm số cuộc tấn công theo ngày
daily_attacks = df.groupby('date').size().reset_index(name='attack_count')

# Vẽ biểu đồ time series
fig = px.line(daily_attacks, x='date', y='attack_count', title='Số cuộc tấn công theo ngày')
fig.show()
