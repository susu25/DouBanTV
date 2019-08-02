import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from show_data import get_data_frame
from matplotlib import font_manager

#设置字体
myfont = font_manager.FontProperties(fname='/usr/share/fonts/truetype/arphic/ukai.ttc')

'''
7分以上的电视剧时间的分布,散点图
'''

def _show_tv_date_distribute(rate):
    #获取数据,
    df = get_data_frame()
    # 为现存的每条数据作出统计,即让其数量为1,方便之后分组后的聚合
    count_df = pd.DataFrame(np.ones(shape=(len(df),1)),columns=["count"])
    df = df.join(count_df)
    # 去除没有时间的电视剧
    new_df = df[pd.notnull(df["release_date"])]
    #选择大于7分的电视剧
    new_df = new_df[new_df["rating_value"]>=rate]
    #设置日期为索引
    new_df = new_df.set_index("release_date")
    #只选择count列
    new_df = new_df["count"]
    #调整统计时间的范围,实现重新采样
    new_df = new_df.resample("10D").sum()
    return new_df

def show_tv_date_distribute(rate=7):
    df = _show_tv_date_distribute(rate)
    df = pd.DataFrame(df,columns=["count"])
    plt.figure(figsize=(20,8),dpi=80)
    _x = range(len(df.index))
    _y = df["count"]

    plt.scatter(_x, _y, c="green",alpha=0.7, edgecolors='none')

    #解决xticklable时间带时分秒
    xticklables = [i.strftime('%Y-%m') for i in df.index]
    #解决xticklable刻度太密集
    plt.xticks(range(0,len(df.index),3),xticklables[::3],rotation=45)
    plt.xlabel("时间", fontproperties=myfont)
    plt.ylabel("时间段内的数量合计", fontproperties=myfont)
    plt.title("7分以上的电视剧时间的分布散点图", fontproperties=myfont)
    plt.savefig("7分以上的电视剧时间的分布散点图.png")

    plt.show()

if __name__ == '__main__':
    show_tv_date_distribute()