# import matplotlib.pyplot as plt
# import numpy as np
#
# def calculate_rotation_frequency(txt_file):
#     frequencies = {}
#     with open(txt_file, 'r') as f:
#         lines = f.readlines()
#         for line in lines:
#             data = line.strip().split()
#             object_id = int(data[1])
#             angle = float(data[7])
#             if object_id in frequencies:
#                 frequencies[object_id].append(angle)
#             else:
#                 frequencies[object_id] = [angle]
#     return frequencies
#
# def plot_bar_chart(frequencies):
#     object_ids = list(frequencies.keys())
#     num_objects = len(object_ids)
#
#     angles = list(frequencies.values())
#     max_angle_count = max(len(angle_list) for angle_list in angles)
#
#     # 计算转角频率
#     frequencies = [len(angle_list) / max_angle_count for angle_list in angles]
#
#     colors = plt.cm.get_cmap('hsv', num_objects)  # 使用不同颜色表示每个物体ID
#
#     plt.bar(object_ids, frequencies, color=colors(range(num_objects)))
#
#     for i, v in enumerate(frequencies):
#         plt.text(i + 1, v + 0.01, str(len(angles[i])), color='black', ha='center')
#
#     plt.xlabel('Fry ID')
#     plt.ylabel('Rotation Frequency')
#     plt.title('Rotation Frequency by Fry')
#     plt.xticks(object_ids)
#     plt.show()
#
# txt_file = 'runs/track/exp20/labels/merged_file.txt'  # 替换为你的txt文件路径
# frequencies = calculate_rotation_frequency(txt_file)
# plot_bar_chart(frequencies)
import matplotlib.pyplot as plt
import random

def calculate_turn_counts(txt_file):
    turn_counts = {}
    with open(txt_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = line.strip().split()
            object_id = int(data[1])
            x1, y1, w, h = map(int, data[2:6])
            # 在这里根据具体情况计算转角次数
            # ...

            if object_id in turn_counts:
                turn_counts[object_id] += 1
            else:
                turn_counts[object_id] = 1
    return turn_counts

def plot_bar_chart(turn_counts):
    object_ids = list(turn_counts.keys())
    counts = list(turn_counts.values())

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
    random.shuffle(colors)
    a=[360,350,54,284,360,244,291,358,360,360,360,340,304,262,177,360,360,352,208,0,173,112,25,43,0,0,76,75,68,44,0,33]
    plt.bar(object_ids, counts, color=colors[:len(object_ids)])

    for i, v in enumerate(counts):
            plt.text(i + 1, v + 1, str(v), color='black', ha='center',fontsize=8)
    plt.xlabel('Fry ID')
    plt.ylabel('Turn Counts')
    plt.title('Turn Counts for Fry')
    plt.xticks(fontsize=8)
    plt.xticks(object_ids)
    plt.show()

txt_file = 'results.txt'  # 替换为你的txt文件路径
turn_counts = calculate_turn_counts(txt_file)
plot_bar_chart(turn_counts)

