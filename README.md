# 🛡️ Phân tích hành vi tấn công mạng từ Cowrie Honeypot

**Học phần**: An toàn hệ thống thông tin (MI4260)  
**Đại học**: Đại học Bách Khoa Hà Nội  
**Giảng viên hướng dẫn**: PGS. TS. Nguyễn Đình Hân  
**Nhóm thực hiện**: Nhóm 3
  👥 Thành viên nhóm
Họ và Tên	MSSV	Vai trò chính
Nguyễn Trung Kiên (Trưởng nhóm)	20227180;
Vũ Lương Duy	20227226;
Lê Ngọc Trung Kiên	20227236.

**Năm học**: 2024–2025

---

## 📌 Mô tả đề tài

Dự án này sử dụng Honeypot Cowrie để thu thập các hành vi tấn công SSH từ thực tế, sau đó phân tích chúng bằng các kỹ thuật thống kê, trực quan hóa và học máy. Quá trình phân tích bao gồm tiền xử lý log, enrich dữ liệu địa lý, phân cụm IP bất thường bằng DBSCAN và trực quan hóa bằng Python/Flask/Dash.

---

## 🧪 Yêu cầu môi trường

Python >= 3.8

# Thư viện cần thiết
---
pip install -r requirements.txt
---bash

---
🧰 Hướng dẫn chạy
Phân tích dữ liệu tấn công
Tiền xử lý:

Chạy step0_parse_log_to_csv.py để chuyển log Cowrie sang CSV.

Chạy step1_location_geo.py để enrich dữ liệu với GeoIP.

Chạy step2_preprocessing.py để chuẩn hóa timestamp và kiểm tra IP.

Phân tích thống kê và trực quan:

step4_plot_geo.py: thống kê quốc gia tấn công.

step5_botnet_detection.py: phát hiện IP đáng ngờ.

step6_password_count.py: phân tích mật khẩu bị thử.

step7_time_series.py: biểu đồ theo chuỗi thời gian.

Phân cụm DBSCAN:

step8_dbscan.py: phát hiện botnet hoặc hành vi bất thường.

Trực quan hóa địa lý nâng cao:

step9_nominatim.py: định vị theo tên thành phố + quốc gia.

Dashboard (Dash/Plotly):

step10_dashboard.py: khởi chạy dashboard trực quan.
