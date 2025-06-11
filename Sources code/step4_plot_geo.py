import pandas as pd
import plotly.express as px

# Đọc lại file đã có thông tin geo
df = pd.read_csv('C:/Users/admin.DESKTOP-DOMJBUQ/Downloads/archive/ssh_logs_with_geo.csv')

# Vẽ bản đồ: đếm số lần tấn công theo quốc gia
country_counts = df['Country'].value_counts().reset_index()
country_counts.columns = ['Country', 'Attack Count']

# Vẽ bản đồ thế giới
fig = px.choropleth(
    country_counts,
    locations='Country',
    locationmode='country names',
    color='Attack Count',
    color_continuous_scale='Reds',
    title='Phân bố tấn công theo quốc gia'
)
fig.show()
