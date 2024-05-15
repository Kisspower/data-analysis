import numpy as np
import pandas as pd
from pandas import DataFrame
'''标准化'''
def z_stardliziation(data):
    mu = np.mean(data,axis=0)
    sigma = np.std(data,axis=0)
    return (data-mu)/sigma
'''正向指标归一化'''
def positive_normalization(data):
    maxrange = np.max(data)-np.min(data)
    return (data-np.min(data))/maxrange
'''负向指标归一化'''
def negative_normalization(data):
    max_data = np.max(data)
    min_data = np.min(data)
    maxrnage = max_data-min_data
    return (max_data-data)/maxrnage
'''二重耦合协调度'''
def double_coupling(x,y):
    D = 2*(x*y)**0.5/(x+y)
    T = a*x+b*y
    return (D*T)**0.5


if __name__ == '__main__':
    data = pd.read_excel("C:\\Users\\22389\\Desktop\\回归数据表.xlsx", sheet_name='毕业论文数据2011-2021')
    ulgue = data['ULGUE']
    score = data['score']
    print(data.info())
    ulgue1 = positive_normalization(ulgue)
    for i in range(len(ulgue1)):
        if ulgue1[i]==0:
            ulgue1[i]=0.01
    score1 = positive_normalization(score)
    for i in range(len(score1)):
        if score1[i]==0:
            score1[i]=0.01
    a,b= 0.5,0.5
    coupling2 = double_coupling(ulgue1,score1)
    data1 = { '归一化ulgue': ulgue1,'归一化score': score1,'归一化耦合协调度':coupling2}
    df = DataFrame(data1)
    df.to_excel("C:\\Users\\22389\\Desktop\\新建 Microsoft Excel 工作表.xlsx",sheet_name='Sheet1')
