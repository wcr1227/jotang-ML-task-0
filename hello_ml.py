# hello_ml.py
import numpy as np

scores = {
    "李华": 88,
    "王传儒": 92,
    "无名氏": 76,
    "焦糖": 95,
}

# 算平均分和最高分
def calc(data):
    # data.values()	取出所有成绩，返回 dict_values 视图对象
    vals = list(data.values())
    avg = sum(vals) / len(vals)
    top = max(vals)
    # 列表推导式，遍历所有键值对，挑出分数等于最高分的人
    names = [n for n, s in data.items() if s == top]
    return avg, top, names
#调用函数并解包
avg, top, names = calc(scores)
print("平均分：%.2f" % avg)
print("最高分：%d，%s" % (top, "、".join(names)))


# 矩阵乘法
a = np.array([[1, 2],
              [3, 4],
              [5, 6]])

b = np.array([[10, 20, 30],
              [40, 50, 60]])

c = a @ b

print(a.shape, b.shape, c.shape)
print(c)