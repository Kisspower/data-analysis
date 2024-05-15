import numpy as np
import pandas as pd
#print(data.info())

#标准化数据
'''正向指标归一化'''
def positive_normalization(data):
    maxrange = np.max(data)-np.min(data)
    return (data-np.min(data))/maxrange

'''负向指标归一化'''
def negative_normalization(data):
    maxrange = np.max(data)-np.min(data)
    return (np.max(data)-data)/maxrange
#计算评价指标的特征比重
def feature_parts(data):
    sum = np.sum(data)
    return data/sum
#计算评价指标的熵值
def entropy(data,data_stardlization):
    data1 = data.replace(0,1e-10)
    return -1 / np.log(len(data_stardlization)) * np.sum(data1 * np.log(data1), axis=0)
#计算综合得分
def Comprehensive_score(data1,data2):
    return data1*data2


if __name__ == '__main__':
    data = pd.read_excel()
    waste_water = data['wastewater']
    so2 = data['so2']
    pm = data['pm']
    data_stardlization1 = negative_normalization(waste_water)#对数据标准化
    for i in range(len(data_stardlization1)):
        if data_stardlization1[i] == 0:
            data_stardlization1[i] = 0.001
    data_stardlization2 = negative_normalization(so2)
    for i in range(len(data_stardlization2)):
        if data_stardlization2[i] == 0:
            data_stardlization2[i] = 0.001
    data_stardlization3 = negative_normalization(pm)
    for i in range(len(data_stardlization3)):
        if data_stardlization3[i] == 0:
            data_stardlization3[i] = 0.0001
    # print(data_stardlization1,data_stardlization2)
    data_parts1 = feature_parts(data_stardlization1)#这里计算评价指标的特征比重
    data_parts2 = feature_parts(data_stardlization2)
    data_parts3 = feature_parts(data_stardlization3)
    '''这里计算熵值'''
    data_entropy1 = entropy(data_parts1,data_stardlization1)
    data_entropy2= entropy(data_parts2,data_stardlization2)
    data_entropy3 = entropy(data_parts3,data_stardlization3)
    '''这里计算评价指标的差异系数'''
    data_DiffCof1 = 1-data_entropy1
    data_DiffCof2 = 1-data_entropy2
    data_DiffCof3 = 1-data_entropy3
    '''计算评价指标的权重'''
    data_w1 = data_DiffCof1/(data_DiffCof2+data_DiffCof1+data_DiffCof3)
    data_w2 = data_DiffCof2/(data_DiffCof2+data_DiffCof1+data_DiffCof3)
    data_w3 = data_DiffCof3/(data_DiffCof2+data_DiffCof1+data_DiffCof3)
    '''计算评价对象的综合得分'''
    score = (Comprehensive_score(data_stardlization1,data_w1) + Comprehensive_score
    (data_stardlization2,data_w2) + Comprehensive_score(data_stardlization3,data_w3))

    output = {'污水-标准化':data_stardlization1,'二氧化硫-标准化':data_stardlization2,'工业粉尘-标准化':data_stardlization3,
              '污水-熵值':data_entropy1,'二氧化硫-熵值':data_entropy2,'工业粉尘-熵值':data_entropy3,
              '污水-权重':data_w1,'二氧化硫-权重':data_w2,'工业粉尘-权重':data_w3,
              '污染综合指数':score
              }
    df = pd.DataFrame(output)
    df.to_excel("C:\\Users\\22389\\Desktop\\熵权法综合评价结果.xlsx",sheet_name='Sheet1')







