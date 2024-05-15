import pandas
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

data = pandas.read_excel("C:\\Users\\22389\\Desktop\\回归数据表.xlsx",sheet_name='毕业论文数据')
data1 = data['TL']

_lambda = 0.5

# def box_cox_transfor(data):
#     for i in range(len(data)):
#         data1 = (data**_lambda-1)/_lambda
#         return data1

converted_data1 = stats.boxcox(data1)[0] #对数据进行BOX-COX变换
sns.histplot(converted_data1)
plt.show()