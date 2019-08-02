import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from show_data import get_data_frame
from matplotlib import font_manager
'''
实现功能:不同分类的电视剧数量的统计
'''

myfont = font_manager.FontProperties(fname='/usr/share/fonts/truetype/arphic/ukai.ttc')

def show_tag_count():
    df = get_data_frame()
    df_tag = df[["country", "rating_value", "tag"]]

    # 切割组成集合,tags是一个带集合的列表
    tags = [set(x.split("_")) for x in df_tag["tag"]]
    # 把所有的tag组成一个集合
    tags = set.union(*tags)
    # 设置一个(len(df_tag),len(tags))的全是0元素的2维数组
    dummies = pd.DataFrame(np.zeros((len(df_tag), len(tags))), columns=tags)
    for i, tag in enumerate(df_tag["tag"]):
        dummies.loc[i, tag.split("_")] = 1
    df_new = df_tag.join(dummies)
    # print(df_new)
    # 删除空字符串的那一列
    df_new = df_new.drop("", axis=1)
    # print(df_new.columns)
    tag_list = df_new.columns[3:]
    tag_count = []
    for tag in tag_list:
        tag_count.append([tag,df_new[tag].sum()])
    print(tag_count)
    #排序,让柱状图按照顺序显示
    tag_count.sort(key=lambda x:x[1],reverse=True)
    plt.figure(figsize=(20,8),dpi=80)
    # 画横着的直方图
    plt.barh(range(len(tag_count)), [i[1] for i in tag_count], align="center", color='#EE7600', ecolor='black')
    plt.yticks(range(len(tag_count)), [i[0] for i in tag_count], fontproperties=myfont)
    print(range(len(tag_count)), len([i[0] for i in tag_count]))

    plt.ylabel("分类", fontproperties=myfont)
    # y轴值
    plt.xlabel("数量", fontproperties=myfont)
    # 图的标题
    plt.title("不同分类电视剧的数量统计", fontproperties=myfont)
    plt.savefig("./不同分类电视剧的数量统计.png")
    plt.show()


if __name__ == '__main__':
    show_tag_count()