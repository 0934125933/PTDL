# Các bước để chạy container khi clone Repo này về
## TRÊN MÁY CHÍNH
### 1. Sau khi clone về để chạy được thì nhớ dùng cmd trong VScode chứ đừng có dùng Powershell
### 2. Trong cmd nhập lệnh: ```Docker network create <đặt tên network>``` để tạo sẵn 1 cái địa chỉ network cho mình
* mỗi lần kết nối mạng khác là sẽ có cái IP khác nên phải tạo lại chứ ko phải là sài lại cái cũ đâu nhá
### 3. Dùng lệnh: ```docker run -d -p 27017:27017 --name mymongodb mongo``` để chạy ngầm cái container mymongodb này
* dùng để LƯU DỮ LIỆU sau khi cào.. KO CHẠY là lúc cào nó BÁO LỖI VỚI DELAY SML ráng chịu
* Nếu chạy lệnh này trên máy ảo thì nhớ thêm --network <tên network vừa tạo> vào trong câu lệnh đưa ip mạng về cùng 1 địa chỉ
### 4. Dùng lệnh: ```docker build -t <đặt tên image>``` để lưu tất cả file code trên Repo này vào trong image
* sau này muốn dùng thì cứ gọi tên image thôi
### 5. Để chạy container cào website thì dùng lệnh: ```docker container run -e host=mymongodb --network <tên network vừa tạo> --name <đặt tên cho container> <tên image cần dùng>```
* GHI CHÚ: -e đặt giá trị cho biến host là cái container mymongodb đang chạy ngầm , ```--network``` là đặt cổng mạng cho container , ```--name``` để đặt tên cho container
### 6. Sau khi code chạy xong (finished) thì dùng lệnh: ```docker exec -it mymongodb mongosh``` để kiểm tra dữ liệu nếu muốn
```python
# THỨ TỰ CÁC LỆNH#

# Đặt tên network
docker network create <đặt tên network>

# Chạy ngầm container MongoDB
docker run -d -p 27017:27017 --name mymongodb mongo

# Build code của mình thành Image
docker build -t <đặt tên image> .

# Khởi chạy Container
docker container run -e host=mymongodb --network <tên network vừa tạo> --name <đặt tên cho container> <tên image cần dùng>
```

## TRÊN MÁY ẢO

### 1. Ngoài việc CLONE cái Respository này về, sau khi dùng lệnh 'docker build -t <đặt tên image> .' xong thì ...
### 2. Dùng lệnh ```Docker tag <tên image> <tên tài khoản dockerhub>/<đặt tên repository>``` để tạo một cái tag định danh cho Repository
* Lệnh này dùng để phân biệt và cấp phép cho cái image này được phép push lên Dockerhub
* Ngoài ra có thể thêm ```:<đặt tên tagname/tên nhánh>``` để phân biệt sự thay đổi giữa các lần push image lên Hub (nếu không ghi thì mặc định là latest)
### 3. Sau khi đã đặt tag xong thì dùng lệnh ```Docker push <tài khoản Dockerhub>/<tên Repo vừa tạo><:tagname nếu có tạo>``` để đẩy cái image này lên Dockerhub online

* Khuyến khích là nên dùng SSH trên CMD để thực hiện từ bước này vì nó tiện dễ copy paste
* Lệnh dùng để kết nối với máy ảo bằng CMD: ```ssh <tên máy ảo>@<ip máy ảo>``` Nếu không biết IP thì vào máy ảo dùng lệnh ifconfig rồi xem IP nào đúng là kết nối được.
# *Lưu ý là phải tải được net-tools,openssh với Docker thì mới xem IP với dùng lệnh Docker được nha*
### BONUS link cài MongoDB trên máy ảo: [tại đây](https://www.mongodb.com/docs/v4.4/tutorial/install-mongodb-on-ubuntu/)
### VÀO MÁY ẢO RỒI THÌ NHỚ DÙM LÀ BẮT ĐẦU DÒNG LỆNH PHẢI CÓ ```sudo``` ĐỂ NÓ CẤP QUYỀN ADMIN

* Không biết tải Docker thì xem file [upgradesystem](https://github.com/0934125933/PTLDSource/blob/main/upgradesystem) của Mr.Nam
4. Push xong rồi thì vào máy ảo pull về thôi: ```Docker pull <tên tài khoản>/<tên Repo><:tên tagname nếu có>```
* Nó y chang lúc pull image trên Docker máy chính á, khác cái là mình không dùng tên bình thường được
5. Pull rồi thì làm y chang như **CÁC BƯỚC Ở TRÊN MÁY CHÍNH**.
* Lưu ý ở đây là khi thực hiện lệnh ```docker run -d -p 27017:27017 --name mymongodb mongo``` thì
* đổi cái mongo thành mongo:4.0 vì cái mongo phiên bản cao cấp **KHÔNG HỖ TRỢ MÁY CÙI BẮP**
* thêm --network <tên network vừa tạo> **NHƯ ĐÃ NHẮC Ở TRÊN**

# HẾT
