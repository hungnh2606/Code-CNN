import os
import shutil
from sklearn.model_selection import train_test_split

# Đường dẫn thư mục chứa ảnh
image_dir = "D:\Code Pytorch\Data\Animal"
output_dir = "D:\Code Pytorch\Data\Animal"

# Lấy danh sách ảnh
images = []
labels = []

for class_name in os.listdir(image_dir):
    class_path = os.path.join(image_dir, class_name)
    if os.path.isdir(class_path):
        for img_name in os.listdir(class_path):
            images.append(os.path.join(class_path, img_name))
            labels.append(class_name)

# Chia dữ liệu
train_images, test_images, train_labels, test_labels = train_test_split(
    images, labels, test_size=0.2, random_state=42, stratify=labels
)

# Hàm lưu ảnh vào thư mục mới
def save_images(image_list, label_list, folder):
    for img_path, label in zip(image_list, label_list):
        dest_folder = os.path.join(output_dir, folder, label)
        os.makedirs(dest_folder, exist_ok=True)
        shutil.copy(img_path, dest_folder)

# Lưu ảnh vào thư mục train và test
save_images(train_images, train_labels, "train")
save_images(test_images, test_labels, "test")
