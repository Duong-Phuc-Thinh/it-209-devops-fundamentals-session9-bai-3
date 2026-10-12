# Bài 3: Viết Dockerfile đóng gói trang Web HTML tĩnh

## Giới thiệu
Dự án mẫu đóng gói một ứng dụng Web HTML tĩnh đơn giản vào Docker Image dựa trên Nginx Alpine.

## Các file trong dự án
- `index.html`: File HTML chứa nội dung `<h1>Hello Docker Session 09!</h1>`.
- `Dockerfile`: File cấu hình build image từ `nginx:alpine` và copy `index.html` vào đường dẫn mặc định của Nginx.
- `main.py`: Script Python tự động hóa việc build image, khởi chạy container, kiểm tra kết quả bằng HTTP request và dọn dẹp.

## Hướng dẫn chạy

### Cách 1: Chạy bằng lệnh Docker CLI
1. Build Docker image:
```bash
docker build -t my-html-app:v1 .
```

2. Khởi chạy container từ image:
```bash
docker run -d -p 8081:80 --name html-app my-html-app:v1
```

3. Kiểm tra trang web:
```bash
curl http://localhost:8081
```

### Cách 2: Tự động kiểm tra với Python Script
```bash
python main.py
```