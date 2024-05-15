import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rc('font',family = 'MicroSoft YaHei')
data = pd.read_excel("C:\\Users\\31066\\Desktop\\新建 XLS 工作表.xls"
                     ,sheet_name='Sheet1')
sns.kdeplot(data)
plt.title('历年产业结构核密度分析')
plt.show()

