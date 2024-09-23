from pymongo import MongoClient
import psycopg2

def create_table(pg_cursor):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS courses (
        coursename TEXT PRIMARY KEY,
        lecturer TEXT,
        intro TEXT,
        describe TEXT,
        votenumber INTEGER,
        rating NUMERIC,
        newfee text,
        oldfee text,
        lessonnum INTEGER
    );
    """
    pg_cursor.execute(create_table_query)

# Kết nối tới MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['dbmycrawler']
mongo_collection = mongo_db['tblunitop']

# Kết nối tới PostgreSQL
pg_conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='123456',
    host='localhost',
    port='5432'
)
pg_cursor = pg_conn.cursor()

try:
    # Tạo bảng nếu chưa tồn tại
    create_table(pg_cursor)

    # Truy xuất dữ liệu từ MongoDB
    documents = mongo_collection.find()

    # Chèn dữ liệu vào PostgreSQL
    for document in documents:
        # Chuyển đổi document sang định dạng phù hợp
        # Giả sử document có các trường: coursename, lecturer, intro, describe, votenumber, rating, newfee, oldfee, lessonnum
        pg_cursor.execute(
            """
            INSERT INTO courses (coursename, lecturer, intro, describe, votenumber, rating, newfee, oldfee, lessonnum)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                document['coursename'],
                document['lecturer'],
                document['intro'],
                document['describe'],
                document['votenumber'],
                document['rating'],
                document['newfee'],
                document['oldfee'],
                document['lessonnum']
            )
        )
    pg_conn.commit()
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
finally:
    # Đóng kết nối
    pg_cursor.close()
    pg_conn.close()
    mongo_client.close()
