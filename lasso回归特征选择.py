import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 生成一些回归数据（100个样本和10个特征，其中只有2个是信息性的）
X, y = make_regression(n_samples=100, n_features=10, n_informative=2, noise=10, random_state=42)

# 将数据分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建一个Lasso回归模型实例
lasso = Lasso(alpha=0.1)

# 拟合模型
lasso.fit(X_train, y_train)

# 预测测试集的结果
y_pred = lasso.predict(X_test)

# 计算均方误差作为性能指标
mse = mean_squared_error(y_test, y_pred)

# 系数可视化
plt.figure(figsize=(10, 6))
plt.bar(range(len(lasso.coef_)), lasso.coef_)
plt.xlabel('Features')
plt.ylabel('Coefficients')
plt.title('LASSO Coefficients')
plt.show()

# 测试数据实际值与预测值对比
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--k')
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.title('True Values vs Predictions')
plt.show()

# 打印性能指标
print("Mean squared error on test data:", mse)