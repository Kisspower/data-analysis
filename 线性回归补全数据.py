import numpy as np
from sklearn.linear_model import LinearRegression as LR  # 线性回归
from sklearn.model_selection import train_test_split     # 划分训练测试集
import pandas as pd

df = pd.read_excel("C:\\Users\\31066\\Desktop\\城市土地绿色利用、产业结构升级与财政压力相关文件夹\\284个城市2006-2022年数据.xlsx",
                   sheet_name="城市土地绿色利用效率数据")
Fixed_investment = df["全社会固定资产投资--亿元"]
year = df["year"]

for i in range(len(Fixed_investment)):
    if Fixed_investment[i] == 99999999:
        x = [year[i-1],year[i-2],year[i-3],year[i-4],year[i-5],year[i-6],year[i-7],year[i-8],year[i-9],year[i-10],
             year[i-11],year[i-12],year[i-13],year[i-14]]
        y = [Fixed_investment[i-1],Fixed_investment[i-2],Fixed_investment[i-3],Fixed_investment[i-4],
                  Fixed_investment[i-5],Fixed_investment[i-6],Fixed_investment[i-7],Fixed_investment[i-8],
             Fixed_investment[i-9],Fixed_investment[i-10],Fixed_investment[i-11],Fixed_investment[i-12],
             Fixed_investment[i-13],Fixed_investment[i-14]]
        x1 = [year[i]]
        xtrain = np.array(x).reshape(-1,1)
        ytrain = np.array(y).reshape(-1,1)
        xtest = np.array(x1).reshape(-1,1)
        reg = LR().fit(xtrain,ytrain)
        coef = reg.coef_
        intercept = reg.intercept_
        Fixed_investment[i] = reg.predict(xtest)

output = {"补全后数据":Fixed_investment
          }
dfe = pd.DataFrame(output)
dfe.to_excel("C:\\Users\\31066\\Desktop\\新建文件夹.xlsx",sheet_name='Sheet1')
