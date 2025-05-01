import numpy as np
import matplotlib.pyplot as plt


def generate_heatmap(txt_file):
    # 读取txt文件并解析数据
    data = np.loadtxt(txt_file, dtype=int, usecols=(1, 2, 3, 4, 5))
    object_ids = np.unique(data[:, 0])

    # 创建一个矩阵来存储每个ID的位置热力图
    heatmap = np.zeros((data[:, 1].max() + 1, data[:, 2].max() + 1))

    for object_id in object_ids:
        # 选择特定ID的数据
        id_data = data[data[:, 0] == object_id]
        for frame_id, x, y, w, h in id_data:
            # 在位置矩阵上增加计数
            heatmap[y:y + h, x:x + w] += 1

    return heatmap


def plot_heatmap(heatmap):
    plt.imshow(heatmap, cmap='hot', interpolation='nearest')
    plt.colorbar(label='Counts')
    plt.gca().set_facecolor('black')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(0, 1920)
    plt.ylim(0, 1080)
    plt.title('Fry ID Heatmap')
    plt.show()


txt_file = r'F:\Smart Fisheries\change-temp\image\mot.txt'  # 替换为你的txt文件路径
heatmap = generate_heatmap(txt_file)
plot_heatmap(heatmap)






