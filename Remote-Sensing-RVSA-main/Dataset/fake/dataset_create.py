import os
import random
from PIL import Image
# 设置随机种子以确保结果可复现
random.seed(28)

# 读取数据集标注文件
gt_file_path = "./gt.txt"
with open(gt_file_path, "r") as file:
    lines = file.readlines()

# 打乱数据顺序
random.shuffle(lines)
# 计算训练集和测试集的分割点
split_point = int(0.8 * len(lines))

# 分割数据集
train_data = lines[:split_point]
valid_data = lines[split_point:]

# 指定输出文件的路径
output_dir = "./"
train_output_path = os.path.join(output_dir, "train_labels_28_0.txt")
valid_output_path = os.path.join(output_dir, "valid_labels_28_0.txt")

# 写入训练集数据
with open(train_output_path, "w") as file:
    file.writelines(train_data)

# 写入测试集数据
with open(valid_output_path, "w") as file:
    file.writelines(valid_data)

# 图片处理部分
source_dir = "./image"
target_dir = "./all_img"

# 确保目标文件夹存在
os.makedirs(target_dir, exist_ok=True)

# # 遍历source_dir中的所有文件
# for filename in os.listdir(source_dir):
#     if filename.endswith((".png", ".jpg", ".jpeg")):  # 仅处理图片文件
#         source_path = os.path.join(source_dir, filename)
#         target_filename=os.path.splitext(filename)[0]+".jpg"
#         target_path=os.path.join(target_dir,target_filename)
#         with Image.open(source_path) as img:
#             if img.mode=="RGBA":
#                 img=img.convert("RGB")
#             #resized_img = img.resize((256,256),Image.ANTIALIAS)
#             resized_img = img
#             resized_img.save(target_path,"JPEG")

# 遍历source_dir中的所有文件
# for filename in os.listdir(source_dir):
#     if filename.endswith((".png", ".jpg", ".jpeg")):  # 仅处理图片文件
#         source_path = os.path.join(source_dir, filename)
#         target_path = os.path.join(target_dir, filename)
#         with Image.open(source_path) as img:
#             if img.mode=="RGBA":
#                 img=img.convert("RGB")
#             #resized_img = img.resize((256,256),Image.ANTIALIAS)
#             resized_img = img
#             resized_img.save(target_path)
