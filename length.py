# # import matplotlib.pyplot as plt
# #
# # def read_tracking_results(file_path):
# #     tracking_data = {}
# #     with open(file_path, 'r') as file:
# #         for line in file:
# #             values = line.strip().split()
# #             frame_id = int(values[0])
# #             x1, y1, w, h = map(int, values[1:5])
# #             object_id = values[5]
# #             if object_id not in tracking_data:
# #                 tracking_data[object_id] = []
# #             tracking_data[object_id].append((frame_id, x1, y1, w, h))
# #     return tracking_data
# #
# #
# # def calculate_total_distance(tracking_data):
# #     total_distances = {}
# #     for object_id, frames in tracking_data.items():
# #         total_distance = 0
# #         prev_x, prev_y = frames[0][1], frames[0][2]
# #         for frame in frames[1:]:
# #             x, y = frame[1], frame[2]
# #             distance = ((x - prev_x) ** 2 + (y - prev_y) ** 2) ** 0.5
# #             total_distance += distance
# #             prev_x, prev_y = x, y
# #         total_distances[object_id] = total_distance
# #     return total_distances
# #
# # def plot_total_distances(total_distances):
# #     objects = list(total_distances.keys())
# #     distances = list(total_distances.values())
# #
# #     plt.bar(objects, distances)
# #     plt.xlabel('Object ID')
# #     plt.ylabel('Total Distance')
# #     plt.title('Total Distance Traveled by Objects')
# #     plt.show()
# #
# # # 读取跟踪结果文件
# # tracking_results = read_tracking_results('runs/track/exp20/labels/merged_file.txt')
# #
# # # 计算每个物体的总移动长度
# # total_distances = calculate_total_distance(tracking_results)
# #
# # # 生成每个物体总运动长度的图表
# # plot_total_distances(total_distances)
#
#
# # import matplotlib.pyplot as plt
# #
# # def calculate_total_distance(tracking_file):
# #     object_distances = {}
# #     with open(tracking_file, 'r') as file:
# #         for line in file:
# #             data = line.strip().split()
# #             frame_id = int(data[0])
# #             object_id = int(data[1])
# #             x, y, w, h = map(float, data[2:6])
# #             distance = ((x + w/2) ** 2 + (y + h/2) ** 2) ** 0.5  # 简单地将中心点的欧氏距离作为物体的位移长度
# #             if object_id in object_distances:
# #                 object_distances[object_id].append(distance)
# #             else:
# #                 object_distances[object_id] = [distance]
# #
# #     return object_distances
# #
# # def plot_object_distances(object_distances):
# #     colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # 不同ID对应的颜色列表
# #     plt.figure()
# #     for object_id, distances in object_distances.items():
# #         color = colors[object_id % len(colors)]  # 使用不同颜色绘制不同ID的物体
# #         plt.plot(distances, color=color, label=f'Object {object_id}')
# #
# #     plt.xlabel('Frame')
# #     plt.ylabel('Total Distance')
# #     plt.title('Total Distance Moved by Each Object')
# #     plt.legend()
# #     plt.show()
# #
# # # 用法示例
# # tracking_file = 'runs/track/exp20/labels/merged_file.txt'
# # object_distances = calculate_total_distance(tracking_file)
# # plot_object_distances(object_distances)
# #
# #
# #
# #
# #
# # # Read the tracking results from the txt file
# # with open('runs/track/exp20/labels/merged_file.txt', 'r') as file:
# #     data = file.readlines()
# #
# # # Calculate total distances for each object
# # total_distances = calculate_total_distance(data)
# #
# # # Generate and display the movement plot
# # generate_movement_plot(total_distances)
#
# import colorcet as cc
# import matplotlib.pyplot as plt
# import random
#
# def calculate_total_distance(txt_file):
#     distances = {}
#     with open(txt_file, 'r') as f:
#         lines = f.readlines()
#         for line in lines:
#             data = line.strip().split()
#             object_id = int(data[1])
#             x1, y1, w, h = map(int, data[2:6])
#             distance = w + h  # 简单计算移动长度，可根据具体情况调整
#             if object_id in distances:
#                 distances[object_id] += distance
#             else:
#                 distances[object_id] = distance
#     return distances
#
# def plot_bar_chart(distances):
#     object_ids = list(distances.keys())
#     distances_values = list(distances.values())
#
#     colors = cc.glasbey  # 使用科研配色方案
#     random.shuffle(colors)  # 随机打乱配色顺序
#
#     plt.bar(object_ids, distances_values, color=colors[:len(object_ids)])
#
#     for i, v in enumerate(distances_values):
#         plt.text(i + 1, v + 1, str(v), color='black', ha='center')
#
#     plt.xlabel('Fry ID')
#     plt.ylabel('Total Distance')
#     plt.title('Total Distance Moved by Fry')
#     plt.xticks(object_ids)
#     plt.show()
#
#
#
#
# txt_file = 'runs/track/exp20/labels/merged_file.txt'  # 替换为你的txt文件路径
# distances = calculate_total_distance(txt_file)
# plot_bar_chart(distances)

import numpy as np
import matplotlib.pyplot as plt
import colorcet as cc

def calculate_total_distance(txt_file):
    data = np.loadtxt(txt_file)
    unique_ids = np.unique(data[:, 1])
    total_distances = []

    for object_id in unique_ids:
        object_data = data[data[:, 1] == object_id]
        x = object_data[:, 2]
        y = object_data[:, 3]

        # 计算每个物体的移动总长度
        distances = np.sqrt(np.diff(x)**2 + np.diff(y)**2)
        total_distance = np.sum(distances)
        total_distances.append(total_distance)

    return unique_ids, total_distances

def plot_total_distances(unique_ids, total_distances):
    sorted_indices = np.argsort(unique_ids)  # 根据ID排序的索引
    sorted_ids = unique_ids[sorted_indices]
    sorted_distances = np.array(total_distances)[sorted_indices]
    colors = cc.glasbey

    fig, ax = plt.subplots(figsize=(8, 6))
    a = sorted_distances
    ax.bar(sorted_ids, sorted_distances, color=colors[:len(unique_ids)])
    ax.set_xlabel('Fry ID')
    ax.set_ylabel('Total Distance')
    ax.set_title('Total Distance Traveled by Fry')
    ax.set_xticks(sorted_ids)

    # ax.set_xticklabels(sorted_ids)
    ax.legend()
    for i, v in enumerate(a):
        plt.text(i + 1, v + 1, str(int(v)), color='black', ha='center')
    # 添加ID标签
    # for i, distance in enumerate(sorted_distances):
    #     ax.text(i, distance, str(int(sorted_ids[i])), ha='center', va='bottom')

    plt.show()

txt_file = r'F:\Smart Fisheries\mot - 副本.txt'  # 替换为你的txt文件路径
unique_ids, total_distances = calculate_total_distance(txt_file)
plot_total_distances(unique_ids, total_distances)