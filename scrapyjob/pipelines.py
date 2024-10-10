# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
# from scrapy.exceptions import DropItem 
import csv
from scrapy.exceptions import DropItem 
import pymongo
import mysql.connector
import psycopg2
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, col, when
from sqlalchemy import create_engine
import pandas as pd


class JsonDBJobPipeline:

    def open_spider(self, spider):
        self.file = open('jsondatavieclam.json', 'a', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        return item
    
class CSVDBJobPipeline:
    def process_item(self, item, spider):
        with open('job_data.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['courseUrl', 'job_name', 'name_company', 'upadte_date', 'rank','amount','age','level',
                          'experience','salary','headquarters','technical_requirements']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')

            # Kiểm tra nếu file CSV chưa có header thì ghi header
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow(item)

        return item
    
class MongoDBJobPipeline:
    def __init__(self):
        # Connection String
        # econnect = str(os.environ['host'])
        # self.client = pymongo.MongoClient('mongodb://'+econnect+':27017/')
        # self.client = pymongo.MongoClient('mongodb://'mymongodb':27017/')
        self.client = pymongo.MongoClient('mongodb://localhost:27017')
        self.db = self.client['dbjobcrawler'] #Create Database      
        pass
    
    def process_item(self, item, spider):
        
        collection =self.db['tbljob'] #Create Collection or Table
        try:
            collection.insert_one(dict(item))
            return item
        except Exception as e:
            raise DropItem(f"Error inserting item: {e}")       
        pass

class PySparkPipeLine:
    def __init__(self):
        # Kết nối tới MongoDB
        # econnect2 = str(os.environ['host'])
        # client = pymongo.MongoClient('mongodb://'+econnect2+':27017/')
        self.client = pymongo.MongoClient('mongodb://localhost:27017') 
        self.db = self.client['dbjobcrawler']  # Thay 'dbjobcrawler' bằng tên database của bạn
        self.collection = self.db['tbljob']  # Thay 'tbljob' bằng tên collection của bạn

        # Lấy dữ liệu từ MongoDB
        data = list(self.collection.find())
        df = pd.DataFrame(data)

        # Xử lý dữ liệu bằng python
        # Sử dụng str.extract để tách tên công việc và mã công việc
        df['Tên công việc'] = df['job_name'].str.extract(r'^(.*?)\s*\(Mã:')
        df['Mã công việc'] = df['job_name'].str.extract(r'\(Mã:(.*?)\)')

        # Loại bỏ cột job_name nếu không cần nữa
        df = df.drop(columns=['job_name'])

        #Lưu
        df.to_csv('du_lieu_lam_sach.csv', index=False, encoding='utf-8-sig')
#         # Xử lý dữ liệu (các bước xử lý tương tự như trên)
#         # 1. Tách tên công việc với mã công việc ở cột 'job_name'
#         df['MaCV'] = df['job_name'].str.extract(r'\((.*?)\)', expand=False)  # Tách mã công việc
#         df['jobname_cleaned'] = df['job_name'].str.replace(r'\(.*\)', '', regex=True).str.strip()

#         # 2. Chuẩn hóa cột Tuổi về các khoảng xác định
#         def age_range(age):
#             if 'dưới' in age.lower():
#                 return '0-25'
#             elif 'trên' in age.lower():
#                 return '35+'
#             elif '25 đến 35' in age or '25-35' in age:
#                 return '25-35'
#             else:
#                 return age  # giữ nguyên nếu không khớp

#         df['age_range'] = df['age'].apply(age_range)

#         # 3. Chuẩn hóa cột Yêu cầu kinh nghiệm
#         df['experience_cleaned'] = df['experience'].str.replace(r'[^\d]', '', regex=True)

#         # 4. Chuẩn hóa cột Lương (Thoả thuận -> 0)
#         df['salary_cleaned'] = df['salary'].apply(lambda x: '0' if 'thoả thuận' in x.lower() else x)
#         df['salary_cleaned'] = df['salary_cleaned'].str.replace(r'[^\d]', '', regex=True)

#         # 5. Bỏ chữ "Ngày cập nhật" khỏi cột Ngày cập nhật
#         df['updated_date_cleaned'] = df['upadte_date'].str.replace('Ngày cập nhật', '').str.strip()

#         # 6. Xóa các cột không cần thiết
#         df_cleaned = df.drop(columns=['Application_deadline', 'welfare', 'describe', 
#                                     'headquarters', 'industry', 'amount', 'courseUrl'])

        # Kết nối tới PostgreSQL
        # pg_conn = psycopg2.connect(
        #     dbname='postgres',
        #     user='postgres',
        #     password='123456',
        #     host='postgres-db',
        #     port='5432'
        # )
        # pg_cursor = pg_conn.cursor()

        # # Ghi dữ liệu đã xử lý vào PostgreSQL
        # pg_cursor.execute(
        #     """
        #     CREATE TABLE IF NOT EXISTS jobs (
        #         job_name TEXT PRIMARY KEY,
        #         name_company TEXT,
        #         rank TEXT,
        #         describe TEXT
        #     );
        #     """
        # )
        # pg_cursor.execute(
        #     """
        #     INSERT INTO jobs (job_name, name_company, rank, describe)
        #     VALUES (%s, %s, %s, %s)
        #     """,
        #     (
        #         df['job_name'],
        #         df['name_company'],
        #         df['rank'],
        #         df['describe']
        #     )
        # )

#         print("Dữ liệu đã được lưu vào PostgreSQL thành công!")

        pass