import os
import random

# 设置随机种子以确保重复运行脚本时得到相同的结果
random.seed(28)

# 指定数据集的根目录
dataset_root = './all_img'
classes = os.listdir(dataset_root)  # 获取所有类别的文件夹名称
classes.sort()  # 确保顺序一致性

# 收集所有图片路径及其类别
all_images = []
for class_id, class_name in enumerate(classes):
    class_dir = os.path.join(dataset_root, class_name)
    images = os.listdir(class_dir)
    for image in images:
        all_images.append((os.path.join(class_name, image), class_id))

# 打乱数据集
random.shuffle(all_images)

# 按照8:2的比例划分数据集
split_point = int(len(all_images) * 0.8)
train_images = all_images[:split_point]
valid_images = all_images[split_point:]

# 保存到文件
def save_to_file(images, file_path):
    with open(file_path, 'w') as file:
        for image_path, class_id in images:
            file.write(f"{image_path} {class_id}\n")

save_to_file(train_images, 'train_labels_28_0.txt')
save_to_file(valid_images, 'valid_labels_28_0.txt')

print("数据集划分完成。")
