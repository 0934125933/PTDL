import pandas as pd
from sqlalchemy import create_engine

# Đường dẫn đến file CSV
file_path = 'scrapyjob/scrapyjob/spiders/du_lieu_lam_sach.csv'

# Đọc dữ liệu từ file CSV
data = pd.read_csv(file_path)

# Chuyển đổi định dạng ngày tháng với định dạng cụ thể
data['upadte_date'] = pd.to_datetime(data['upadte_date'], format='%d/%m/%Y', errors='coerce')

# Kết nối đến PostgreSQL và ghi dữ liệu vào bảng
try:
    # Các thông tin kết nối
    dbname = 'postgres'  # Tên cơ sở dữ liệu
    user = 'postgres'    # Tên người dùng
    password = '12345'   # Mật khẩu
    host = 'localhost'    # Địa chỉ máy chủ
    port = '5432'        # Cổng

    # Tạo engine kết nối đến PostgreSQL
    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}')
    
    # Ghi dữ liệu vào bảng
    data.to_sql('ten_bang', engine, if_exists='replace', index=False)
    print("\nDữ liệu đã được ghi vào bảng thành công.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
