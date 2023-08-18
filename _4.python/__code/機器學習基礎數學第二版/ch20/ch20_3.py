# ch20_3.py
import numpy as np

def cosine_similarity(va, vb):
    norm_a = np.linalg.norm(va)                 # 計算向量大小
    norm_b = np.linalg.norm(vb)                 # 計算向量大小
    dot_ab = np.dot(va, vb)                     # 計算向量內積
    return (dot_ab / (norm_a * norm_b))         # 回傳相似度

a = np.array([2, 1, 1, 1, 0, 0, 0, 0])
b = np.array([1, 1, 0, 0, 1, 1, 1, 0])
c = np.array([1, 1, 0, 0, 1, 1, 0, 1])
print('a 和 b 相似度 = {0:5.3f}'.format(cosine_similarity(a, b)))
print('a 和 c 相似度 = {0:5.3f}'.format(cosine_similarity(a, c)))
print('b 和 c 相似度 = {0:5.3f}'.format(cosine_similarity(b, c)))






