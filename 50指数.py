# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 15:12:41 2018

@author: Administrator
"""

from datetime import datetime
import csv
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
fig = plt.figure(dpi=128, figsize=(10, 5))

def open_file(file):    
    with open(file, encoding='gb18030', errors='ignore') as f:
        reader = csv.reader(f)
        header_row = next(reader)   
        dates, highs = [], []
        for row in reader:
            current_date = datetime.strptime(row[0],'%Y/%m/%d').date()
            dates.append(current_date)
            high = int(row[1])
            highs.append(high)
            #   新的列表每隔3位取一次数字
            new_dates = dates[::3]
        return dates, highs, new_dates


def curve():
    dates, highs, new_dates = open_file(file)   
    plt.title('上证50指数', fontsize=16)
    plt.xlabel('',fontsize=8)
    plt.ylabel('', fontsize=8)
    plt.tick_params(axis='y', which = 'major', labelsize=12)
    plt.tick_params(axis='x', which = 'major', labelsize=8)
    # xticks(locs, [labels], **kwargs)
    plt.xticks(new_dates, new_dates, rotation=90)
    plt.plot(dates, highs, c='red')

 
    
def dotted_line():
    # 上证50按照2015年789点开始计算, 蓝色线是年10%收益
    d1 = datetime(2005, 7, 1)
    d2 = datetime(2018, 7, 1)
    x = [[d1, d2]] 
    y = [[789, 2723]]
    for i in range(len(x)):
        plt.plot(x[i], y[i],linestyle=':', color='b')
        plt.legend(['点位','年收益10%'], loc='upper right', fontsize=10)

        

if __name__ == '__main__':
    file = 'D:/anaconda python/sj/sz502004-2018.csv'
    curve()
    dotted_line()
    plt.show()
    