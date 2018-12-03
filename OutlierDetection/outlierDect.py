# coding:utf-8
import numpy as np
from sklearn.covariance import EllipticEnvelope

xx, yy = np.meshgrid(np.linspace(-5, 5, 500), np.linspace(-5, 5, 500))
# 生成训练数据
X = 0.3 * np.random.randn(100,2)
X_train = np.r_[X+2, X-2]
