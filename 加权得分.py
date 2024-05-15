import pandas as pd
import numpy as np
import 熵权法代码实现 as enp


def z_score(data):
    mean = np.mean(data,axis=0)
    std = np.std(data)
    return (data-mean)/std
'''正、负向指标归一化'''
def positive_normalization(data):
    maxrange = np.max(data)-np.min(data)
    return (data-np.min(data))/maxrange

'''负向指标归一化'''
def negative_normalization(data):
    max_data = np.max(data)
    min_data = np.min(data)
    maxrnage = max_data-min_data
    return (max_data-data)/maxrnage

if  __name__ == '__main__':
    data = pd.read_excel("C:\\Users\\22389\\Desktop\\回归数据表.xlsx",sheet_name='毕业论文数据2011-2021')
    TL1= data['TL']
    TS1 = data['TS']
    TFP1 = data['TFP']
    ts = positive_normalization(TS1)
    for i in range(len(TS1)):
        if ts[i] == 0:
            ts[i] = 0.001
    tl = negative_normalization(TL1)
    for i in range(len(TL1)):
        if tl[i] == 0:
            tl[i] = 0.1
    tfp = positive_normalization(TFP1)
    for i in range(len(TFP1)):
        if tfp[i] == 0:
            tfp[i] = 0.001
    #_tstltfp = ts*tl*tfp #直接相乘求和
    #熵权法求和
    '''特征比重'''
    ts_parts = enp.feature_parts(ts)
    tl_parts = enp.feature_parts(tl)
    tfp_parts = enp.feature_parts(tfp)
    '''熵值计算'''
    ts_entropy = enp.entropy(ts_parts,ts)
    tl_entropy = enp.entropy(tl_parts, tl)
    tfp_entropy = enp.entropy(tfp_parts, tfp)
    '''差异系数计算'''
    ts_DiffCof = 1-ts_entropy
    tl_DiffCof = 1-tl_entropy
    tfp_DiffCof = 1-tfp_entropy
    '''计算指标系数的权重'''
    W = ts_DiffCof+tl_DiffCof+tfp_DiffCof
    ts_w = ts_DiffCof/W
    tl_w = tl_DiffCof/W
    tfp_w = tfp_DiffCof/W
    '''计算综合得分'''
    score = (enp.Comprehensive_score(ts, ts_w) + enp.Comprehensive_score
    (tl, tl_w) + enp.Comprehensive_score(tfp, tfp_w))
    output = {'标准化的高级化':ts,'标准化的合理化':tl,'标准化的高效化':tfp,
              '高级化的权重':ts_w,'合理化的权重':tl_w,'高效化的权重':tfp_w,
              '综合得分':score
              }
    pd.DataFrame(output).to_excel(
        "C:\\Users\\22389\\Desktop\\新建 Microsoft Excel 工作表.xlsx",sheet_name='Sheet1')
