# CÁC BƯỚC CÀI ĐẶT MongoDB(v4.4) TRÊN MÁY ẢO

### 1. Dùng lệnh: ```sudo apt-get install gnupg curl``` để cấu hình thư viện cần thiết
### 2. Copy dòng dưới để import key cho MongoDB:
```python
curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-4.4.gpg \
   --dearmor
```
### 3. Tạo tệp (cây thư mục) chứa MongoDB:
```python
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-4.4.gpg ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
```
### 4. Update những gì vừa cấu hình ở trên
```python
sudo apt-get update
```
### 5. Cài đặt MongoDB:
```python
sudo apt-get install -y mongodb-org
```
### 6. Dùng các lệnh này để ngăn không cho MongoDB tự động update:
```python
echo "mongodb-org hold" | sudo dpkg --set-selections
```
```python
echo "mongodb-org-server hold" | sudo dpkg --set-selections
```
```python
echo "mongodb-org-shell hold" | sudo dpkg --set-selections
```
```python
echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
```
```python
echo "mongodb-org-tools hold" | sudo dpkg --set-selections
```
### 7. Cho phép máy ảo chạy MongoDB trên port 27017 và kiểm tra cài đặt
```python
sudo systemctl start mongod
```
* Nếu báo lỗi thì chạy lệnh này ```sudo systemctl daemon-reload``` rồi chạy lại lệnh trên
### 8. Xác minh MongoDB đã được bật
```python
sudo systemctl status mongod
```
* Nếu có chữ nào màu xanh lá nổi bật lên thì là oke
* Nếu có 2 chữ xanh lá nổi bật thì là chưa ```Enable```
### 9. Cấp phép cho MongoDB chạy trên port 27017
```python
sudo systemctl enable mongod
```
* MongoDB này sẽ chiếm port 27017 nên là nếu muốn đẩy dữ liệu vào MongoDB trên Docker thì LÀM ƠN ĐÓNG CÁI MongoDB này lại
### 10. Nào không cần sử dụng nữa thì đóng nó lại:
```python
sudo systemctl stop mongod
```
# Lưu Ý: trong quá trình cài đặt MongoDB nếu gặp lỗi 
## LỖI ```libssl>1.1``` 
### 1. Dùng lệnh này để lấy file cài đặt libssl(1.1):
```python
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.0g-2ubuntu4_amd64.deb
```
### 2. Cài đặt libssl(1.1):
```python
sudo dpkg -i libssl1.1_1.1.0g-2ubuntu4_amd64.deb
```
### [làm xong thì quay lại bước 5](https://github.com/0934125933/PTDL/blob/main/InstallMongoDB.md#5-c%C3%A0i-%C4%91%E1%BA%B7t-mongodb)
# Tại sao lại dùng bản 4.4
## NHƯ ĐÃ NÓI: "MÁY CÙI" không sài được bản cao cấp
