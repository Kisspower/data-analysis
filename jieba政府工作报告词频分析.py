import pandas as pd
import jieba

report = pd.read_excel("C:\\Users\\31066\\Desktop\\人工智能、劳动就业质量与居民消费率\\政府工作报告-省级2002-2023.xlsx")
list1 = report['报告全文'].astype(str)

result = {}
for i in range(1,len(list1)):
    text = list1[i]
    words = jieba.lcut(text,cut_all=True)
    acc = ['人工智能','机器人','互联网','数字','大数据']#这里需要输入所需要的关键词
    count = 0
    for j in range(len(acc)):
        if acc[j] in words:
            count = words.count(acc[j])+count
    val = count
    result.setdefault(i,val)

values = result.values()
i = result.keys()
abc = {"keyword":i,"count":values}
df = pd.DataFrame(abc)
df.to_excel("C:\\Users\\31066\\Desktop\\工作报告省级词频分析.xlsx",sheet_name='Sheet1',index=False)