conda env export > environment.yml

tạo môi trường theo file environment.yml
conda env create -p .\env -f environment.yml

kích hoạt
conda activate env

cập nhật theo đường dẫn
conda env update -p [đường_dẫn] --file environment.yml

cập nhật theo tên
conda env update --name [name] --file environment.yml

xóa gói ko cần
conda env update -f environment.yml --prune


---------------------------------------------------------------------------------------
my_flask_app/                                                                          |
│                                                                                      |
├── app/                                                                               |                                                                                              
│   ├── __init__.py            # Khởi tạo ứng dụng Flask                               |
│   ├── routes.py              # Định nghĩa các route                                  |
│   ├── models.py              # Định nghĩa các mô hình (ORM)                          |
│   ├── forms.py               # Định nghĩa các form (nếu cần)                         |
│   ├── static/                # Thư mục chứa các tệp tĩnh (CSS, JS, hình ảnh)         |
│   └── templates/             # Thư mục chứa các mẫu HTML                             |
│       ├── layout.html        # Mẫu bố cục chung                                      |
│       └── index.html         # Mẫu trang chính                                       |
│                                                                                      |
├── instance/                  # Thư mục chứa cấu hình riêng cho môi trường            |
│   └── config.py              # Cấu hình ứng dụng                                     |
|                                                                                      |
├── database                   #Thư mục database (sqlite)                              |
|   └──data.db                                                                         |
├── tests/                     # Thư mục chứa các bài kiểm tra                         |
│   └── test_basic.py          # Bài kiểm tra cơ bản                                   |
│                                                                                      |
├── environment.yml            # File cấu hình môi trường (nếu sử dụng conda)          |
|                                                                                      |
├── .gitignore                 # File để loại bỏ các tệp không cần thiết khỏi Git      |
├── config.py                  # Cấu hình chung cho ứng dụng                           |
└── run.py                     # Tệp để chạy ứng dụng                                  |
---------------------------------------------------------------------------------------
