# def read_tracking_results(file_path):
#     data = []
#     with open(file_path, 'r') as file:
#         for line in file:
#             values = line.strip().split()
#             frame_id = int(values[1])
#             x1, y1, w, h = map(int, values[2:6])
#             data.append((frame_id, x1, y1, w, h))
#     return data
#
# def find_max_dimensions(data):
#     max_dimensions = {}
#     for frame_id, x1, y1, w, h in data:
#         if frame_id not in max_dimensions:
#             max_dimensions[frame_id] = [0, 0]  # 初始化为0
#         if h > max_dimensions[frame_id][0]:
#             max_dimensions[frame_id][0] = h  # 更新最大height
#         if w > max_dimensions[frame_id][1]:
#             max_dimensions[frame_id][1] = w  # 更新最大width
#     return max_dimensions
#
# def compare_dimensions(max_dimensions):
#     result = []
#     for frame_id, dimensions in max_dimensions.items():
#         if dimensions[0] > dimensions[1]:
#             result.append([frame_id, dimensions[0], dimensions[1]])  # [id, height, width]
#         else:
#             result.append([frame_id, dimensions[1], dimensions[0]])  # [id, height, width]
#     return result
#
# # 示例用法
# file_path = 'results.txt'
# data = read_tracking_results(file_path)
# max_dimensions = find_max_dimensions(data)
# result = compare_dimensions(max_dimensions)
# print(result)
import matplotlib.pyplot as plt
import numpy as np


def read_tracking_results(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            values = line.strip().split()
            frame_id = int(values[1])
            x1, y1, w, h = map(int, values[2:6])
            data.append((frame_id, x1, y1, w, h))
    return data


def filter_max_width_height(data):
    id_max_width = {}
    id_max_height = {}
    for frame_id, x1, y1, w, h in data:
        if frame_id in id_max_width:
            if w > id_max_width[frame_id]:
                id_max_width[frame_id] = w
        else:
            id_max_width[frame_id] = w

        if frame_id in id_max_height:
            if h > id_max_height[frame_id]:
                id_max_height[frame_id] = h
        else:
            id_max_height[frame_id] = h

    results = []
    for frame_id in id_max_width:
        width = id_max_width[frame_id]
        height = id_max_height[frame_id]
        results.append([frame_id, height, width])

    return results


def plot_scatter(results):
    ids = [result[0] for result in results]
    heights = [result[1] for result in results]
    widths = [result[2] for result in results]

    cmap = plt.get_cmap('Set1')
    colors = cmap(np.linspace(0, 1, len(ids)))

    plt.figure(figsize=(8, 6))
    for i in range(len(ids)):
        plt.scatter(widths[i], heights[i], color=colors[i])
        plt.text(widths[i], heights[i], str(ids[i]), ha='center', va='bottom', fontsize=8)

    plt.xlabel('Width')
    plt.ylabel('Height')
    plt.title('Max Width vs. Max Height')
    plt.show()


# 示例用法
file_path = 'results.txt'
data = read_tracking_results(file_path)
results = filter_max_width_height(data)
plot_scatter(results)
