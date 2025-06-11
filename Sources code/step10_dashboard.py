import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('C:/Users/admin.DESKTOP-DOMJBUQ/Downloads/archive/ssh_logs_with_geo.csv', parse_dates=['timestamp'])

# Tạo các trường cần thiết
df['date'] = df['timestamp'].dt.date
df['date_hour'] = df['timestamp'].dt.floor('h')

st.title("Dashboard Giám sát Honeypot")

# Biểu đồ theo ngày
daily_attacks = df.groupby('date').size().reset_index(name='attack_count')
fig1 = px.line(daily_attacks, x='date', y='attack_count',
               title='Số lượng tấn công theo ngày')
st.plotly_chart(fig1)

# Biểu đồ theo giờ
hourly_attacks = df.groupby('date_hour').size().reset_index(name='attack_count')
fig2 = px.line(hourly_attacks, x='date_hour', y='attack_count',
               title='Số lượng tấn công theo giờ')
st.plotly_chart(fig2)

# Thêm bảng thống kê IP tấn công nhiều nhất
top_ips = df['source_ip'].value_counts().reset_index()
top_ips.columns = ['IP', 'Số lần tấn công']
st.subheader("Top IP tấn công nhiều nhất")
st.dataframe(top_ips.head(10))
