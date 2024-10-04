# Các bước để chạy container khi clone Repo này về

1. Sau khi clone về để chạy được thì nhớ dùng cmd trong VScode chứ đừng có dùng Powershell
2. Trong cmd nhập lệnh: docker network create <đặt tên network> để tạo sẵn 1 cái địa chỉ network cho mình
* mỗi lần kết nối mạng khác là sẽ có cái IP khác nên phải tạo lại chứ ko phải là sài lại cái cũ đâu nhá
3. Dùng lệnh: docker run -d -p 27017:27017 --name mymongodb mongo để chạy ngầm cái container mymongodb này
* dùng để LƯU DỮ LIỆU sau khi cào.. KO CHẠY là lúc cào nó BÁO LỖI VỚI DELAY SML ráng chịu
* Nếu chạy lệnh này trên máy ảo thì nhớ thêm --network <tên network vừa tạo> vào trong câu lệnh đưa ip mạng về cùng 1 địa chỉ
4. Dùng lệnh: docker build -t <đặt tên image> để lưu tất cả file code trên Repo này vào trong image
* sau này muốn dùng thì cứ gọi tên image thôi
5. Để chạy container cào website thì dùng lệnh: docker container run -e host=mymongodb --network <tên network vừa tạo> --name <đặt tên cho container> <tên image cần dùng>
* GHI CHÚ: -e đặt giá trị cho biến host là cái container mymongodb đang chạy ngầm , --network là đặt cổng mạng cho container , --name để đặt tên cho container
6. Sau khi code chạy xong (finished) thì dùng lệnh: docker exec -it mymongodb mongosh để kiểm tra dữ liệu nếu muốn
*** HẾT ***
