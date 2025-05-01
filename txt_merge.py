# import os
#
# # 获取文件夹中所有的 txt 文件
# folder_path = 'E:\\PycharmProjects\\yolov8_tracking-master\\runs\\track\\exp22\\labels'  # 替换为你的文件夹路径
# txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]
#
# # 合并文件内容
# output_file = 'E:\\PycharmProjects\\yolov8_tracking-master\\runs\\track\\exp22\\labels\\merged_file.txt'  # 合并后的文件名
# with open(output_file, 'w') as outfile:
#     for txt_file in txt_files:
#         file_path = os.path.join(folder_path, txt_file)
#         with open(file_path, 'r') as infile:
#             outfile.write(infile.read())
#             outfile.write('\n')  # 可根据需要添加分隔符
#
print('文件合并完成。')
input_file = r'E:\PycharmProjects\yolov8_tracking-master\runs\track\exp29\labels\easy-21.txt'  # 输入文件名
output_file = r'E:\PycharmProjects\yolov8_tracking-master\runs\track\exp29\labels\easy-21_deeporsort.txt'  # 输出文件名

with open(input_file, 'r') as file:
    lines = file.readlines()

new_lines = [line.replace(' ', ',') for line in lines]

with open(output_file, 'w') as file:
    file.writelines(new_lines)
