import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from data_format import choose_data
from matplotlib import font_manager


'''
四个国家电视剧的平均分
'''

#设置字体
myfont = font_manager.FontProperties(fname='/usr/share/fonts/truetype/arphic/ukai.ttc')

def get_data_frame(): #从数据库获取数据,并且把release_date变成时间格式
    temp_df = pd.DataFrame(choose_data())
    temp_df["release_date"] = pd.to_datetime(temp_df["release_date"])
    return temp_df

def plot_four_country_ave_rating_value():
    plt.figure(figsize=(20,8),dpi=80)
    df = get_data_frame()
    df_country_rating = df[["country","rating_value"]]
    #根据国家分组,并且获取平均值
    grouped_rating = df_country_rating.groupby("country").mean()
    print(grouped_rating)
    y = grouped_rating["rating_value"]
    x = np.arange(len(grouped_rating.index))
    plt.bar(x,y,width=0.3,align="center")
    plt.xticks(x,grouped_rating.index)
    # x轴的值
    plt.xlabel("国家",fontproperties=myfont)
    # y轴值
    plt.ylabel("平均分",fontproperties=myfont)
    # 图的标题
    plt.title("豆瓣电视剧平均分统计",fontproperties=myfont)
    plt.savefig("./4个国家电视剧平均分.png")
    plt.show()


if __name__ == '__main__':
    plot_four_country_ave_rating_value()