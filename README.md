conda env export > environment.yml

tạo môi trường theo file environment.yml
conda env create -f environment.yml

kích hoạt
conda activate env

cập nhật theo đường dẫn
conda env update -p [đường_dẫn] --file environment.yml

cập nhật theo tên
conda env update --name [name] --file environment.yml

xóa gói ko cần
conda env update -f environment.yml --prune