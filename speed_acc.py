# import pandas as pd
# import math
#
# # 读取包含物体信息的文本文件
# txt_file = 'runs/track/exp20/labels/merged_file.txt'  # 替换为你的 txt 文件路径
#
# # 读取文本文件并解析物体信息
# data = pd.read_csv(txt_file, sep=' ', header=None)
# data.columns = ['frame', 'id', 'x', 'y', 'w', 'h', '0', '0', '-1']
#
# # 计算速度和加速度
# data['velocity'] = data.groupby('id')['x'].diff()
# data['acceleration'] = data.groupby('id')['velocity'].diff()
#
# # 绘制速度和加速度图表
# import matplotlib.pyplot as plt
#
# plt.figure(figsize=(12, 6))
# plt.subplot(2, 1, 1)
# for obj_id, obj_data in data.groupby('id'):
#     plt.plot(obj_data['frame'], obj_data['velocity'], label=f'fry {obj_id}')
# plt.xlabel('Frame')
# plt.ylabel('Velocity')
# plt.legend()
#
# plt.subplot(2, 1, 2)
# for obj_id, obj_data in data.groupby('id'):
#     plt.plot(obj_data['frame'], obj_data['acceleration'], label=f'Object {obj_id}')
# plt.xlabel('Frame')
# plt.ylabel('Acceleration')
# plt.legend()
#
# plt.tight_layout()
# plt.show()
#
# # 保存计算结果到 xlsx 文件
# xlsx_file = 'result.xlsx'  # 保存结果的 xlsx 文件路径
# data.to_excel(xlsx_file, index=False)
#
# print('计算结果已保存到 xlsx 文件中。')
# import numpy as np
# import matplotlib.pyplot as plt
# import colorcet as cc
#
# def calculate_velocity_acceleration(txt_file):
#     data = {}
#     with open(txt_file, 'r') as f:
#         lines = f.readlines()
#         for line in lines:
#             frame, object_id, x1, y1, w, h, _, _, _ = map(int, line.strip().split())
#             x_center = x1 + w / 2
#             y_center = y1 + h / 2
#             if object_id in data:
#                 data[object_id].append([frame, x_center, y_center])
#             else:
#                 data[object_id] = [[frame, x_center, y_center]]
#
#     velocity = {}
#     acceleration = {}
#     for object_id, object_data in data.items():
#         frames = np.array([d[0] for d in object_data])
#         x = np.array([d[1] for d in object_data])
#         y = np.array([d[2] for d in object_data])
#
#         vx = np.gradient(x, frames)
#         vy = np.gradient(y, frames)
#         velocity[object_id] = np.sqrt(vx**2 + vy**2)
#
#         ax = np.gradient(vx, frames)
#         ay = np.gradient(vy, frames)
#         acceleration[object_id] = np.sqrt(ax**2 + ay**2)
#
#     return velocity, acceleration
#
# def plot_velocity_acceleration(velocity, acceleration):
#     colors = cc.glasbey  # 使用科研配色方案
#
#     plt.figure(figsize=(10, 5))
#     plt.subplot(121)
#     for object_id, v in velocity.items():
#         plt.plot(v, color=colors[object_id % len(colors)])
#     plt.xlabel('Frame')
#     plt.ylabel('Velocity')
#     plt.title('Object Velocity')
#     plt.legend(velocity.keys(), title='Object ID', bbox_to_anchor=(1.05, 1), loc='upper left')
#
#     plt.subplot(122)
#     for object_id, a in acceleration.items():
#         plt.plot(a, color=colors[object_id % len(colors)])
#     plt.xlabel('Frame')
#     plt.ylabel('Acceleration')
#     plt.title('Object Acceleration')
#     plt.legend(acceleration.keys(), title='Object ID', bbox_to_anchor=(1.05, 1), loc='upper left')
#
#     plt.tight_layout()
#     plt.show()
# txt_file = 'runs/track/exp20/labels/merged_file.txt'  # 替换为你的 txt 文件路径
# velocity, acceleration = calculate_velocity_acceleration(txt_file)
# plot_velocity_acceleration(velocity, acceleration)

import matplotlib as mpl
mpl.use('TkAgg')
print(mpl.get_backend())
import matplotlib.pyplot as plt
import numpy as np
# 读取文件数据
data = np.loadtxt('results.txt')

# 计算每个id每帧的速度和加速度
id_list = list(set(data[:, 1]))
speed_list = []
acceleration_list = []
for id in id_list:
    id_data = data[data[:, 1] == id, :]
    speed = []
    acceleration = []
    for i in range(2, len(id_data)):
        x1, y1 = id_data[i-2, 2:4]
        x2, y2 = id_data[i-1, 2:4]
        x3, y3 = id_data[i, 2:4]
        v1 = ((x2-x1)**2 + (y2-y1)**2)**0.5 / 1
        v2 = ((x3-x2)**2 + (y3-y2)**2)**0.5 / 1
        a = (v2 - v1) / 1
        speed.append(v2)
        acceleration.append(a)
    speed_list.append(speed)
    acceleration_list.append(acceleration)

# 绘制速度和加速度图表
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

for i in range(len(id_list)):

    ax1.plot(speed_list[i], label='fry'+str(int(id_list[i])))

    ax2.plot(acceleration_list[i], label='fry'+str(int(id_list[i])))

ax1.legend()
ax1.set_ylabel('Speed')
ax2.legend()
ax2.set_xlabel('Frame')
ax2.set_ylabel('Acceleration')

# 保存速度和加速度数据到CSV文件
np.savetxt('id_speed_and_acceleration.csv', np.column_stack([id_list, speed_list, acceleration_list]), delimiter=',',fmt ='%s')

plt.show()


