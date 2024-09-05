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
            fieldnames = ['courseUrl', 'job_name', 'name_company', 'upadte_date', 'rank','industry','amount','age','level',
                          'experience','salary','headquarters','Application_deadline','technical_requirements','welfare',
                          'describe']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')

            # Kiểm tra nếu file CSV chưa có header thì ghi header
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow(item)

        return item
    
class MongoDBJobPipeline:
    def __init__(self):
        #Connection String
        self.client = pymongo.MongoClient('mongodb://localhost:27017')
        self.db = self.client['dbmycrawler'] #Database      
        pass
    
    def process_item(self, item, spider):
        
        collection =self.db['tbljob'] #Table
        try:
            collection.insert_one(dict(item))
            return item
        except Exception as e:
            raise DropItem(f"Error inserting item: {e}")       
        pass
