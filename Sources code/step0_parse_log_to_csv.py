import re
import csv
import os

# Đường dẫn file log đầu vào
input_file = r'C:\Users\admin.DESKTOP-DOMJBUQ\Downloads\archive\_ssh-honeypotd_logs.txt'
output_file = os.path.join(os.path.dirname(input_file), 'parsed_log.csv')

# Biểu thức chính quy để phân tích log
log_pattern = re.compile(
    r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) .*?Failed password for (?P<username>\S+) from (?P<source_ip>\d{1,3}(?:\.\d{1,3}){3}) port (?P<source_port>\d+) ssh2 \(target: (?P<target_ip>\d{1,3}(?:\.\d{1,3}){3}):(?P<target_port>\d+), password: (?P<password>.*?)\)'
)

# Đọc và phân tích log
parsed_rows = []
with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        match = log_pattern.search(line)
        if match:
            parsed_rows.append(match.groupdict())

# Ghi ra file CSV
if parsed_rows:
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=parsed_rows[0].keys())
        writer.writeheader()
        writer.writerows(parsed_rows)
    print(f"Đã ghi {len(parsed_rows)} dòng vào: {output_file}")
else:
    print("Không tìm thấy dòng nào khớp mẫu log.")
