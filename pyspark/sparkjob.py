from pyspark.sql import SparkSession
import psycopg2
from pymongo import MongoClient
import os
import mysql.connector
import pandas as pd

# SparkSession.active()
# Kết nối mongoDB
# mongo_client = MongoClient('mongodb://localhost:27017/')
# mongo_db = mongo_client['dbjobcrawler']
# mongo_collection = mongo_db['tbljob']
# # Lấy dữ liệu
# data=list(mongo_collection.find())
# df = pd.DataFrame(data)
# print(df['job_name'].head())
# # Xử lý dữ liệu
# df[['name','code']] = df['job_name'].str.extract(r'(.+)\(Mã: (.+)\)')
# # Hiển thị kết quả
# print(df['code'])


# from pyspark.sql import SparkSession
# from pyspark.sql.functions import regexp_extract

# spark = SparkSession.builder.appName("ExtractJobInfo").getOrCreate()

# # Giả sử df là DataFrame chứa dữ liệu của bạn
# df = spark.read \
#     .format("mongodb") \
#     .option("") \
#     .load()

# # Tách tên công việc và mã công việc
# df = df.withColumn("Tên công việc", regexp_extract("Column2", r'(.+)\(Mã: (.+)\)', 1))
# df = df.withColumn("Mã công việc", regexp_extract("Column2", r'(.+)\(Mã: (.+)\)', 2))

# df.show()

#
from pyspark.sql import SparkSession

# Cấu hình SparkSession
spark = SparkSession.builder \
    .appName("Jobcrawler") \
    .config("spark.mongodb.read.connection.uri", "mongodb://127.0.0.1/dbjobcrawler.tbljob?readPreference=primaryPreferred") \
    .config("spark.mongodb.write.connection.uri", "mongodb://127.0.0.1/dbjobcrawler.tbljob") \
    .getOrCreate()
# Đọc dữ liệu từ MongoDB
df = spark.read.format("mongodb").load()
df2 = list(df)
df = pd.DataFrame(df2)
# Hiển thị dữ liệu
df.head()
# Xử lý dữ liệu
from pyspark.sql.functions import regexp_extract

# Tách mã công việc ra khỏi tên công việc
extracted_df = df.withColumn(="JobName", regexp_extract("job_name", r'(.+)\(Mã: (.+)\)', 1)) \
                 .withColumn("JobCode", regexp_extract("job_name", r'(.+)\(Mã: (.+)\)', 2))

# Hiển thị kết quả
print(extracted_df.head())



