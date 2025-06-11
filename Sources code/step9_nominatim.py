from geopy.geocoders import Nominatim
import pandas as pd
import time

geolocator = Nominatim(user_agent="geoapiExercises")
df = pd.read_csv('C:/Users/admin.DESKTOP-DOMJBUQ/Downloads/archive/ssh_logs_with_geo.csv')

def get_lat_lon(row):
    try:
        location = geolocator.geocode(f"{row['City']}, {row['Country']}")
        if location:
            return pd.Series([location.latitude, location.longitude])
        else:
            return pd.Series([None, None])
    except:
        return pd.Series([None, None])

# Giả sử df là DataFrame có 'City' và 'Country'
df[['latitude', 'longitude']] = df.apply(get_lat_lon, axis=1)

# Để tránh bị giới hạn truy vấn của Nominatim, có thể tạm nghỉ giữa các lần gọi
time.sleep(1)
