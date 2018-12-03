# coding:utf-8
import numpy as np
from sklearn.covariance import EllipticEnvelope

xx, yy = np.meshgrid(np.linspace(-5, 5, 500), np.linspace(-5, 5, 500))
# 生成训练数据
X = 0.3 * np.random.randn(100, 2)
X_train = np.r_[X + 2, X - 2]
# 生成新用于测试的数据
X = 0.3 * np.random.randn(10, 2)
X_test = np.r_[X + 2, X - 2]
# 模拟拟合
clf = EllipticEnvelope()
clf.fit(X_train)
y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)

print("Novelty detection result: ", y_pred_test)
