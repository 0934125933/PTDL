from pyspark.sql import SparkSession
import psycopg2
import pymongo
import os
import mysql.connector
# Kết nối tới MongoDB
mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
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

# Cấu hình SparkSession với MongoDB
spark = SparkSession.builder \
    .appName("MongoDB_PySpark") \
    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/database.collection") \
    .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/database.collection") \
    .getOrCreate()

df = spark.read.format("com.mongodb.spark.sql.DefaultSource").load()

# Hiển thị dữ liệu
df.head()